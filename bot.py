import discord
from discord.ext import commands
import os
import random
import asyncio
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

# Importiere Fragenpools
try:
    from stufe1 import quiz_stufe1
    from stufe2 import quiz_stufe2
    from stufe3 import quiz_stufe3
    from stufe4 import quiz_stufe4
except ImportError as e:
    print(f"❌ Fehler beim Import der Fragen: {e}")
    quiz_stufe1 = []
    quiz_stufe2 = []
    quiz_stufe3 = []
    quiz_stufe4 = []

load_dotenv()

# --- CONFIG ---
DB_FILE = "quiz_data.db"
QUIZ_CATEGORY_NAME = "📝 QUIZ"
PVP_CATEGORY_NAME = "⚔️ PVP-QUIZ"
STUFEN_NAMEN = {1: "Anfänger", 2: "Fortgeschritten", 3: "Profi", 4: "Experte"}
STUFEN_POOLS = {1: quiz_stufe1, 2: quiz_stufe2, 3: quiz_stufe3, 4: quiz_stufe4}
STUFEN_EMOJIS = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴"}
FRAGEN_PRO_RUNDE = 10
ANTWORT_TIMEOUT = 60  # Sekunden pro Frage

# --- DISCORD SETUP ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Aktive Sessions tracken
active_solo = {}      # user_id -> channel_id
active_pvp = {}       # channel_id -> pvp_data
pvp_challenges = {}   # challenged_user_id -> challenge_data

# ============================================================
#                     DATENBANK
# ============================================================

def init_db():
    """Erstellt alle nötigen Tabellen."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Solo-Fortschritt
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            current_stufe INTEGER DEFAULT 1,
            total_correct INTEGER DEFAULT 0,
            total_answered INTEGER DEFAULT 0,
            total_quizzes INTEGER DEFAULT 0,
            total_perfect INTEGER DEFAULT 0,
            joined_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Solo Quiz-History
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            stufe INTEGER,
            score INTEGER,
            total INTEGER,
            perfect BOOLEAN,
            played_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # PvP Ergebnisse
    c.execute("""
        CREATE TABLE IF NOT EXISTS pvp_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player1_id TEXT,
            player2_id TEXT,
            player1_score INTEGER,
            player2_score INTEGER,
            stufe INTEGER,
            winner_id TEXT,
            played_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # PvP Stats
    c.execute("""
        CREATE TABLE IF NOT EXISTS pvp_stats (
            user_id TEXT PRIMARY KEY,
            username TEXT,
            wins INTEGER DEFAULT 0,
            losses INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0,
            total_correct INTEGER DEFAULT 0,
            total_answered INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

def get_user(user_id, username="Unknown"):
    """Holt oder erstellt User-Daten."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (str(user_id),))
    row = c.fetchone()
    if not row:
        c.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (str(user_id), username))
        conn.commit()
        c.execute("SELECT * FROM users WHERE user_id = ?", (str(user_id),))
        row = c.fetchone()
    else:
        c.execute("UPDATE users SET username = ? WHERE user_id = ?", (username, str(user_id)))
        conn.commit()
    conn.close()
    return {
        "user_id": row[0], "username": row[1], "current_stufe": row[2],
        "total_correct": row[3], "total_answered": row[4],
        "total_quizzes": row[5], "total_perfect": row[6]
    }

def save_quiz_result(user_id, stufe, score, total):
    """Speichert ein Quiz-Ergebnis und aktualisiert den User."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    perfect = score == total

    c.execute("""
        INSERT INTO quiz_history (user_id, stufe, score, total, perfect)
        VALUES (?, ?, ?, ?, ?)
    """, (str(user_id), stufe, score, total, perfect))

    c.execute("""
        UPDATE users SET
            total_correct = total_correct + ?,
            total_answered = total_answered + ?,
            total_quizzes = total_quizzes + 1,
            total_perfect = total_perfect + ?
        WHERE user_id = ?
    """, (score, total, int(perfect), str(user_id)))

    # Aufstieg bei 10/10
    if perfect and stufe < 4:
        c.execute("""
            UPDATE users SET current_stufe = ?
            WHERE user_id = ? AND current_stufe = ?
        """, (stufe + 1, str(user_id), stufe))

    conn.commit()
    conn.close()
    return perfect

def save_pvp_result(p1_id, p2_id, p1_score, p2_score, stufe):
    """Speichert PvP-Ergebnis."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    if p1_score > p2_score:
        winner = str(p1_id)
    elif p2_score > p1_score:
        winner = str(p2_id)
    else:
        winner = "draw"

    c.execute("""
        INSERT INTO pvp_results (player1_id, player2_id, player1_score, player2_score, stufe, winner_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (str(p1_id), str(p2_id), p1_score, p2_score, stufe, winner))

    for uid in [p1_id, p2_id]:
        c.execute("SELECT * FROM pvp_stats WHERE user_id = ?", (str(uid),))
        if not c.fetchone():
            c.execute("INSERT INTO pvp_stats (user_id, username) VALUES (?, ?)", (str(uid), ""))

    c.execute("""
        UPDATE pvp_stats SET total_correct = total_correct + ?, total_answered = total_answered + ?
        WHERE user_id = ?
    """, (p1_score, FRAGEN_PRO_RUNDE, str(p1_id)))

    c.execute("""
        UPDATE pvp_stats SET total_correct = total_correct + ?, total_answered = total_answered + ?
        WHERE user_id = ?
    """, (p2_score, FRAGEN_PRO_RUNDE, str(p2_id)))

    if winner == "draw":
        for uid in [p1_id, p2_id]:
            c.execute("UPDATE pvp_stats SET draws = draws + 1 WHERE user_id = ?", (str(uid),))
    else:
        loser = str(p2_id) if winner == str(p1_id) else str(p1_id)
        c.execute("UPDATE pvp_stats SET wins = wins + 1 WHERE user_id = ?", (winner,))
        c.execute("UPDATE pvp_stats SET losses = losses + 1 WHERE user_id = ?", (loser,))

    conn.commit()
    conn.close()

def get_solo_ranking(limit=15):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT user_id, username, current_stufe, total_correct, total_answered, total_perfect
        FROM users WHERE total_quizzes > 0
        ORDER BY current_stufe DESC, total_perfect DESC, total_correct DESC
        LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_pvp_ranking(limit=15):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT user_id, username, wins, losses, draws, total_correct, total_answered
        FROM pvp_stats WHERE (wins + losses + draws) > 0
        ORDER BY wins DESC, total_correct DESC
        LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

# ============================================================
#                     HILFSFUNKTIONEN
# ============================================================

async def get_or_create_category(guild, name):
    category = discord.utils.get(guild.categories, name=name)
    if not category:
        category = await guild.create_category(name)
    return category

def build_result_embed(user, stufe, fragen, antworten, score):
    """Erstellt das Ergebnis-Embed nach einem Quiz."""
    perfect = score == FRAGEN_PRO_RUNDE
    emoji = STUFEN_EMOJIS[stufe]
    name = STUFEN_NAMEN[stufe]

    if perfect:
        if stufe < 4:
            title = f"🎉 PERFEKT! Aufstieg zu Stufe {stufe + 1}!"
            color = 0x00ff00
        else:
            title = "🏆 PERFEKT! Du bist ein Trading-Experte!"
            color = 0xffd700
    elif score >= 7:
        title = f"👏 Gut gemacht! {score}/{FRAGEN_PRO_RUNDE}"
        color = 0x3498db
    elif score >= 5:
        title = f"📊 Solide! {score}/{FRAGEN_PRO_RUNDE}"
        color = 0xf39c12
    else:
        title = f"📚 Weiter üben! {score}/{FRAGEN_PRO_RUNDE}"
        color = 0xe74c3c

    embed = discord.Embed(title=title, color=color)
    embed.set_author(name=f"{emoji} Stufe {stufe}: {name}")

    filled = "🟩" * score
    empty = "🟥" * (FRAGEN_PRO_RUNDE - score)
    embed.add_field(name="Score", value=f"{filled}{empty}\n**{score}/{FRAGEN_PRO_RUNDE}**", inline=False)

    result_text = ""
    for i, (frage, user_ans) in enumerate(zip(fragen, antworten), 1):
        correct = frage["answer"]
        correct_opt = next((o for o in frage["options"] if o.startswith(correct)), "?")
        if user_ans == correct:
            result_text += f"✅ **F{i}:** {frage['question']}\n   Deine Antwort: **{user_ans})** ✓\n\n"
        elif user_ans == "⏰":
            result_text += f"⏰ **F{i}:** {frage['question']}\n   Zeit abgelaufen! Richtig: **{correct_opt}**\n\n"
        else:
            result_text += f"❌ **F{i}:** {frage['question']}\n   Deine Antwort: **{user_ans})** → Richtig: **{correct_opt}**\n\n"

    chunks = []
    current_chunk = ""
    for line in result_text.split("\n"):
        if len(current_chunk) + len(line) + 1 > 1020:
            chunks.append(current_chunk)
            current_chunk = line + "\n"
        else:
            current_chunk += line + "\n"
    if current_chunk:
        chunks.append(current_chunk)

    for idx, chunk in enumerate(chunks):
        label = "Auswertung" if idx == 0 else f"Auswertung (Fort.)"
        embed.add_field(name=label, value=chunk, inline=False)

    if perfect and stufe < 4:
        next_emoji = STUFEN_EMOJIS[stufe + 1]
        next_name = STUFEN_NAMEN[stufe + 1]
        embed.add_field(
            name="🆙 Aufstieg!",
            value=f"Du bist jetzt in **{next_emoji} Stufe {stufe + 1}: {next_name}**!\nStarte mit `!quiz` um die nächste Stufe zu spielen.",
            inline=False
        )
    elif not perfect:
        embed.set_footer(text=f"Du brauchst 10/10 um aufzusteigen. Versuche es mit !quiz erneut!")

    return embed

# ============================================================
#                     BOT EVENTS
# ============================================================

@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")
    init_db()
    print(f"✅ Datenbank initialisiert")
    print(f"✅ Fragen geladen: S1={len(quiz_stufe1)} S2={len(quiz_stufe2)} S3={len(quiz_stufe3)} S4={len(quiz_stufe4)}")

# ============================================================
#                     SOLO QUIZ
# ============================================================

@bot.command(name="quiz")
async def quiz_cmd(ctx):
    """Startet ein Solo-Quiz auf deiner aktuellen Stufe."""
    try:
        await ctx.message.delete()
    except:
        pass

    user_id = ctx.author.id

    if user_id in active_solo:
        msg = await ctx.send(f"❌ {ctx.author.mention}, du hast bereits ein aktives Quiz!")
        await asyncio.sleep(5)
        await msg.delete()
        return

    user_data = get_user(user_id, ctx.author.display_name)
    stufe = user_data["current_stufe"]
    pool = STUFEN_POOLS.get(stufe, [])

    if not pool:
        await ctx.send("❌ Keine Fragen für diese Stufe gefunden!")
        return

    # Privaten Kanal erstellen
    category = await get_or_create_category(ctx.guild, QUIZ_CATEGORY_NAME)
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, read_message_history=True
        ),
        ctx.guild.me: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, manage_channels=True,
            manage_messages=True, read_message_history=True
        )
    }
    quiz_channel = await ctx.guild.create_text_channel(
        f"quiz-{ctx.author.name.lower()}", overwrites=overwrites, category=category
    )

    active_solo[user_id] = quiz_channel.id

    hint = await ctx.send(f"📬 {ctx.author.mention}, dein Quiz wartet in {quiz_channel.mention}!")
    await asyncio.sleep(8)
    try:
        await hint.delete()
    except:
        pass

    # Quiz starten
    fragen = random.sample(pool, min(FRAGEN_PRO_RUNDE, len(pool)))
    antworten = []
    score = 0
    emoji = STUFEN_EMOJIS[stufe]
    name = STUFEN_NAMEN[stufe]

    welcome = discord.Embed(
        title=f"{emoji} Stufe {stufe}: {name}",
        description=(
            f"Hallo {ctx.author.mention}!\n\n"
            f"**{FRAGEN_PRO_RUNDE} Fragen** warten auf dich.\n"
            f"⏱️ Du hast **{ANTWORT_TIMEOUT} Sekunden** pro Frage.\n"
            f"🎯 **10/10 richtig** = Aufstieg zur nächsten Stufe!\n\n"
            f"Antworte mit **A**, **B**, **C** oder **D**.\n"
            f"Das Quiz startet in **5 Sekunden**..."
        ),
        color=0x3498db
    )
    await quiz_channel.send(embed=welcome)
    await asyncio.sleep(5)

    for i, frage in enumerate(fragen, 1):
        frage_embed = discord.Embed(
            title=f"Frage {i}/{FRAGEN_PRO_RUNDE}",
            description=f"**{frage['question']}**",
            color=0x9b59b6
        )
        options_text = "\n".join(frage["options"])
        frage_embed.add_field(name="Antwortmöglichkeiten", value=options_text, inline=False)
        frage_embed.set_footer(text=f"⏱️ {ANTWORT_TIMEOUT}s | Score: {score}/{i-1} | Stufe {stufe}")

        await quiz_channel.send(embed=frage_embed)

        def check(m):
            return (
                m.author.id == user_id
                and m.channel.id == quiz_channel.id
                and m.content.strip().upper() in ["A", "B", "C", "D"]
            )

        try:
            msg = await bot.wait_for("message", timeout=ANTWORT_TIMEOUT, check=check)
            user_ans = msg.content.strip().upper()
        except asyncio.TimeoutError:
            user_ans = "⏰"
            await quiz_channel.send("⏰ **Zeit abgelaufen!**")

        correct = frage["answer"]
        if user_ans == correct:
            score += 1
            await quiz_channel.send(f"✅ **Richtig!** ({score}/{i})")
        elif user_ans == "⏰":
            correct_opt = next((o for o in frage["options"] if o.startswith(correct)), "?")
            await quiz_channel.send(f"➡️ Richtige Antwort: **{correct_opt}**")
        else:
            correct_opt = next((o for o in frage["options"] if o.startswith(correct)), "?")
            await quiz_channel.send(f"❌ **Falsch!** Richtig wäre: **{correct_opt}**")

        antworten.append(user_ans)

        if i < FRAGEN_PRO_RUNDE:
            await asyncio.sleep(2)

    # Ergebnis speichern
    perfect = save_quiz_result(user_id, stufe, score, FRAGEN_PRO_RUNDE)

    await asyncio.sleep(1)
    result_embed = build_result_embed(ctx.author, stufe, fragen, antworten, score)
    await quiz_channel.send(embed=result_embed)

    del active_solo[user_id]

    await quiz_channel.send("🧹 Dieser Kanal wird in **30 Sekunden** gelöscht...")
    await asyncio.sleep(30)
    try:
        await quiz_channel.delete()
    except:
        pass

    await update_ranking_channel(ctx.guild)

# ============================================================
#                     PVP QUIZ
# ============================================================

@bot.command(name="pvp")
async def pvp_cmd(ctx, opponent: discord.Member = None):
    """Fordere einen Spieler zum PvP-Quiz heraus: !pvp @Spieler"""
    try:
        await ctx.message.delete()
    except:
        pass

    if not opponent:
        msg = await ctx.send("❌ Nutze: `!pvp @Spieler` um jemanden herauszufordern!")
        await asyncio.sleep(8)
        await msg.delete()
        return

    if opponent.bot or opponent.id == ctx.author.id:
        msg = await ctx.send("❌ Ungültiger Gegner!")
        await asyncio.sleep(5)
        await msg.delete()
        return

    if ctx.author.id in active_solo or opponent.id in active_solo:
        msg = await ctx.send("❌ Einer der Spieler hat bereits ein aktives Quiz!")
        await asyncio.sleep(5)
        await msg.delete()
        return

    if opponent.id in pvp_challenges:
        msg = await ctx.send(f"❌ {opponent.mention} hat bereits eine offene Herausforderung!")
        await asyncio.sleep(5)
        await msg.delete()
        return

    # Stufe = niedrigere der beiden
    p1_data = get_user(ctx.author.id, ctx.author.display_name)
    p2_data = get_user(opponent.id, opponent.display_name)
    stufe = min(p1_data["current_stufe"], p2_data["current_stufe"])

    pvp_challenges[opponent.id] = {
        "challenger": ctx.author,
        "opponent": opponent,
        "stufe": stufe,
        "guild": ctx.guild,
        "channel": ctx.channel
    }

    emoji = STUFEN_EMOJIS[stufe]
    challenge_embed = discord.Embed(
        title="⚔️ PvP Quiz-Herausforderung!",
        description=(
            f"{ctx.author.mention} fordert {opponent.mention} heraus!\n\n"
            f"**{emoji} Stufe {stufe}: {STUFEN_NAMEN[stufe]}**\n"
            f"**{FRAGEN_PRO_RUNDE} Fragen** – Wer antwortet mehr richtig?\n\n"
            f"{opponent.mention}, antworte mit `!accept` oder `!decline`\n"
            f"⏱️ Die Herausforderung läuft in **60 Sekunden** ab."
        ),
        color=0xe74c3c
    )
    challenge_msg = await ctx.send(embed=challenge_embed)

    await asyncio.sleep(60)
    if opponent.id in pvp_challenges:
        del pvp_challenges[opponent.id]
        try:
            await challenge_msg.edit(embed=discord.Embed(
                title="⏰ Herausforderung abgelaufen",
                description=f"{opponent.mention} hat nicht rechtzeitig geantwortet.",
                color=0x95a5a6
            ))
        except:
            pass

@bot.command(name="accept")
async def accept_pvp(ctx):
    """Nimmt eine PvP-Herausforderung an."""
    try:
        await ctx.message.delete()
    except:
        pass

    if ctx.author.id not in pvp_challenges:
        msg = await ctx.send("❌ Du hast keine offene Herausforderung!")
        await asyncio.sleep(5)
        await msg.delete()
        return

    challenge = pvp_challenges.pop(ctx.author.id)
    challenger = challenge["challenger"]
    opponent = challenge["opponent"]
    stufe = challenge["stufe"]
    guild = challenge["guild"]

    pool = STUFEN_POOLS.get(stufe, [])
    if not pool:
        await ctx.send("❌ Keine Fragen verfügbar!")
        return

    # PvP-Kanal erstellen
    category = await get_or_create_category(guild, PVP_CATEGORY_NAME)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(view_channel=False),
        challenger: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, read_message_history=True
        ),
        opponent: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, read_message_history=True
        ),
        guild.me: discord.PermissionOverwrite(
            view_channel=True, send_messages=True, manage_channels=True,
            manage_messages=True, read_message_history=True
        )
    }
    pvp_channel = await guild.create_text_channel(
        f"pvp-{challenger.name}-vs-{opponent.name}", overwrites=overwrites, category=category
    )

    active_solo[challenger.id] = pvp_channel.id
    active_solo[opponent.id] = pvp_channel.id

    hint = await ctx.send(f"⚔️ PvP-Match startet in {pvp_channel.mention}!")
    await asyncio.sleep(5)
    try:
        await hint.delete()
    except:
        pass

    # PvP starten
    fragen = random.sample(pool, min(FRAGEN_PRO_RUNDE, len(pool)))
    emoji = STUFEN_EMOJIS[stufe]
    scores = {challenger.id: 0, opponent.id: 0}
    p1_answers = []
    p2_answers = []

    welcome = discord.Embed(
        title=f"⚔️ PvP Quiz – {emoji} Stufe {stufe}",
        description=(
            f"**{challenger.mention}** vs **{opponent.mention}**\n\n"
            f"**{FRAGEN_PRO_RUNDE} Fragen** – Beide antworten gleichzeitig!\n"
            f"⏱️ **{ANTWORT_TIMEOUT} Sekunden** pro Frage.\n"
            f"Antwortet mit **A**, **B**, **C** oder **D**.\n\n"
            f"Das Match startet in **5 Sekunden**..."
        ),
        color=0xe74c3c
    )
    await pvp_channel.send(embed=welcome)
    await asyncio.sleep(5)

    for i, frage in enumerate(fragen, 1):
        frage_embed = discord.Embed(
            title=f"⚔️ Frage {i}/{FRAGEN_PRO_RUNDE}",
            description=f"**{frage['question']}**",
            color=0xe74c3c
        )
        options_text = "\n".join(frage["options"])
        frage_embed.add_field(name="Antwortmöglichkeiten", value=options_text, inline=False)
        frage_embed.set_footer(
            text=f"⏱️ {ANTWORT_TIMEOUT}s | {challenger.display_name}: {scores[challenger.id]} | {opponent.display_name}: {scores[opponent.id]}"
        )
        await pvp_channel.send(embed=frage_embed)

        # Beide Antworten sammeln
        answered = {}

        def check_pvp(m):
            return (
                m.channel.id == pvp_channel.id
                and m.author.id in [challenger.id, opponent.id]
                and m.author.id not in answered
                and m.content.strip().upper() in ["A", "B", "C", "D"]
            )

        timeout_at = asyncio.get_event_loop().time() + ANTWORT_TIMEOUT

        while len(answered) < 2:
            remaining = timeout_at - asyncio.get_event_loop().time()
            if remaining <= 0:
                break
            try:
                msg = await bot.wait_for("message", timeout=remaining, check=check_pvp)
                answered[msg.author.id] = msg.content.strip().upper()
                try:
                    await msg.delete()
                except:
                    pass
                await pvp_channel.send(f"✔️ {msg.author.mention} hat geantwortet!")
            except asyncio.TimeoutError:
                break

        p1_ans = answered.get(challenger.id, "⏰")
        p2_ans = answered.get(opponent.id, "⏰")
        p1_answers.append(p1_ans)
        p2_answers.append(p2_ans)

        correct = frage["answer"]
        correct_opt = next((o for o in frage["options"] if o.startswith(correct)), "?")

        if p1_ans == correct:
            scores[challenger.id] += 1
        if p2_ans == correct:
            scores[opponent.id] += 1

        p1_icon = "✅" if p1_ans == correct else ("⏰" if p1_ans == "⏰" else "❌")
        p2_icon = "✅" if p2_ans == correct else ("⏰" if p2_ans == "⏰" else "❌")

        await pvp_channel.send(
            f"Richtige Antwort: **{correct_opt}**\n"
            f"{p1_icon} {challenger.display_name}: **{p1_ans}**\n"
            f"{p2_icon} {opponent.display_name}: **{p2_ans}**"
        )

        if i < FRAGEN_PRO_RUNDE:
            await asyncio.sleep(3)

    # Ergebnis speichern
    save_pvp_result(challenger.id, opponent.id, scores[challenger.id], scores[opponent.id], stufe)

    p1_score = scores[challenger.id]
    p2_score = scores[opponent.id]

    if p1_score > p2_score:
        winner_text = f"🏆 **{challenger.display_name}** gewinnt!"
        color = 0x00ff00
    elif p2_score > p1_score:
        winner_text = f"🏆 **{opponent.display_name}** gewinnt!"
        color = 0x00ff00
    else:
        winner_text = "🤝 **Unentschieden!**"
        color = 0xf39c12

    result_embed = discord.Embed(title="⚔️ PvP Ergebnis", description=winner_text, color=color)

    p1_bar = "🟩" * p1_score + "🟥" * (FRAGEN_PRO_RUNDE - p1_score)
    p2_bar = "🟩" * p2_score + "🟥" * (FRAGEN_PRO_RUNDE - p2_score)

    result_embed.add_field(
        name=challenger.display_name, value=f"{p1_bar}\n**{p1_score}/{FRAGEN_PRO_RUNDE}**", inline=True
    )
    result_embed.add_field(
        name=opponent.display_name, value=f"{p2_bar}\n**{p2_score}/{FRAGEN_PRO_RUNDE}**", inline=True
    )

    detail = ""
    for i, frage in enumerate(fragen):
        correct = frage["answer"]
        correct_opt = next((o for o in frage["options"] if o.startswith(correct)), "?")
        p1_icon = "✅" if p1_answers[i] == correct else "❌"
        p2_icon = "✅" if p2_answers[i] == correct else "❌"
        detail += f"**F{i+1}:** {p1_icon} vs {p2_icon} — {correct_opt}\n"

    if len(detail) <= 1024:
        result_embed.add_field(name="Auswertung", value=detail, inline=False)

    await pvp_channel.send(embed=result_embed)

    active_solo.pop(challenger.id, None)
    active_solo.pop(opponent.id, None)

    await pvp_channel.send("🧹 Dieser Kanal wird in **30 Sekunden** gelöscht...")
    await asyncio.sleep(30)
    try:
        await pvp_channel.delete()
    except:
        pass

    await update_ranking_channel(guild)

@bot.command(name="decline")
async def decline_pvp(ctx):
    """Lehnt eine PvP-Herausforderung ab."""
    try:
        await ctx.message.delete()
    except:
        pass

    if ctx.author.id in pvp_challenges:
        challenge = pvp_challenges.pop(ctx.author.id)
        msg = await ctx.send(f"❌ {ctx.author.mention} hat die Herausforderung von {challenge['challenger'].mention} abgelehnt.")
        await asyncio.sleep(8)
        await msg.delete()
    else:
        msg = await ctx.send("❌ Du hast keine offene Herausforderung!")
        await asyncio.sleep(5)
        await msg.delete()

# ============================================================
#                     RANKINGS
# ============================================================

async def update_ranking_channel(guild):
    """Aktualisiert den Ranking-Kanal."""
    ranking_channel = discord.utils.get(guild.text_channels, name="quiz-ranking")
    if not ranking_channel:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=True),
            guild.me: discord.PermissionOverwrite(send_messages=True, read_messages=True, manage_messages=True)
        }
        ranking_channel = await guild.create_text_channel("quiz-ranking", overwrites=overwrites)

    try:
        await ranking_channel.purge(limit=20)
    except:
        pass

    # Solo Ranking
    solo_data = get_solo_ranking()
    solo_embed = discord.Embed(
        title="🏆 Solo Quiz Ranking", description="Top-Spieler nach Stufe und perfekten Runden", color=0x3498db
    )

    if solo_data:
        medals = ["🥇", "🥈", "🥉"]
        lines = []
        for i, (uid, uname, stufe, correct, answered, perfects) in enumerate(solo_data):
            medal = medals[i] if i < 3 else f"**{i+1}.**"
            emoji = STUFEN_EMOJIS.get(stufe, "⚪")
            pct = round(correct / answered * 100) if answered > 0 else 0
            lines.append(f"{medal} **{uname}** — {emoji} Stufe {stufe} | {perfects}x 🌟 | {pct}% ({correct}/{answered})")
        solo_embed.add_field(name="Rangliste", value="\n".join(lines), inline=False)
    else:
        solo_embed.add_field(name="Rangliste", value="Noch keine Spieler! Starte mit `!quiz`", inline=False)

    await ranking_channel.send(embed=solo_embed)

    # PvP Ranking
    pvp_data = get_pvp_ranking()
    pvp_embed = discord.Embed(
        title="⚔️ PvP Quiz Ranking", description="Top-Spieler nach Siegen", color=0xe74c3c
    )

    if pvp_data:
        lines = []
        medals = ["🥇", "🥈", "🥉"]
        for i, (uid, uname, wins, losses, draws, correct, answered) in enumerate(pvp_data):
            medal = medals[i] if i < 3 else f"**{i+1}.**"
            total_games = wins + losses + draws
            winrate = round(wins / total_games * 100) if total_games > 0 else 0
            lines.append(f"{medal} **{uname}** — {wins}W / {losses}L / {draws}D | {winrate}% WR")
        pvp_embed.add_field(name="Rangliste", value="\n".join(lines), inline=False)
    else:
        pvp_embed.add_field(name="Rangliste", value="Noch keine PvP-Matches! Starte mit `!pvp @Spieler`", inline=False)

    await ranking_channel.send(embed=pvp_embed)

@bot.command(name="ranking")
async def ranking_cmd(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    await update_ranking_channel(ctx.guild)
    msg = await ctx.send("📊 Ranking aktualisiert! Schau in #quiz-ranking")
    await asyncio.sleep(5)
    await msg.delete()

# ============================================================
#                     STATS & INFO
# ============================================================

@bot.command(name="stats")
async def stats_cmd(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    user_data = get_user(ctx.author.id, ctx.author.display_name)
    stufe = user_data["current_stufe"]
    emoji = STUFEN_EMOJIS[stufe]
    name = STUFEN_NAMEN[stufe]

    embed = discord.Embed(title=f"📊 Stats: {ctx.author.display_name}", color=0x9b59b6)
    pct = round(user_data["total_correct"] / user_data["total_answered"] * 100) if user_data["total_answered"] > 0 else 0

    embed.add_field(name="Aktuelle Stufe", value=f"{emoji} **Stufe {stufe}: {name}**", inline=False)
    embed.add_field(name="Quizze gespielt", value=f"**{user_data['total_quizzes']}**", inline=True)
    embed.add_field(name="Perfekte Runden", value=f"**{user_data['total_perfect']}** 🌟", inline=True)
    embed.add_field(name="Trefferquote", value=f"**{pct}%** ({user_data['total_correct']}/{user_data['total_answered']})", inline=True)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT wins, losses, draws FROM pvp_stats WHERE user_id = ?", (str(ctx.author.id),))
    pvp = c.fetchone()
    conn.close()

    if pvp:
        total_pvp = pvp[0] + pvp[1] + pvp[2]
        pvp_wr = round(pvp[0] / total_pvp * 100) if total_pvp > 0 else 0
        embed.add_field(name="⚔️ PvP", value=f"**{pvp[0]}W / {pvp[1]}L / {pvp[2]}D** ({pvp_wr}% WR)", inline=False)

    progress = ""
    for s in range(1, 5):
        if s < stufe:
            progress += f"{STUFEN_EMOJIS[s]} Stufe {s}: ✅ Abgeschlossen\n"
        elif s == stufe:
            progress += f"{STUFEN_EMOJIS[s]} Stufe {s}: 🔄 **Aktuell**\n"
        else:
            progress += f"{STUFEN_EMOJIS[s]} Stufe {s}: 🔒 Gesperrt\n"
    embed.add_field(name="Fortschritt", value=progress, inline=False)

    msg = await ctx.send(embed=embed)
    await asyncio.sleep(20)
    try:
        await msg.delete()
    except:
        pass

@bot.command(name="hilfe")
async def hilfe_cmd(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(title="📖 Trading Quiz – Befehle", description="Teste dein Trading-Wissen!", color=0x3498db)
    embed.add_field(name="🎮 Solo Quiz", value="`!quiz` — Quiz starten\n`!stats` — Deine Statistiken\n`!ranking` — Ranking anzeigen", inline=False)
    embed.add_field(name="⚔️ PvP Quiz", value="`!pvp @Spieler` — Herausfordern\n`!accept` — Annehmen\n`!decline` — Ablehnen", inline=False)
    embed.add_field(name="ℹ️ Info", value="`!stufen` — Alle Stufen\n`!hilfe` — Diese Übersicht", inline=False)
    embed.add_field(name="🔑 Admin", value="`!setup_quiz` — Quiz-Info Kanal erstellen\n`!reset_user @User` — User zurücksetzen\n`!set_stufe @User <1-4>` — Stufe setzen", inline=False)
    embed.add_field(name="📋 Regeln", value=(
        f"• **{FRAGEN_PRO_RUNDE} Fragen** pro Runde, **{ANTWORT_TIMEOUT}s** pro Frage\n"
        "• **10/10** = Aufstieg zur nächsten Stufe\n"
        "• 🟢 Anfänger → 🟡 Fortgeschritten → 🟠 Profi → 🔴 Experte"
    ), inline=False)

    msg = await ctx.send(embed=embed)
    await asyncio.sleep(30)
    try:
        await msg.delete()
    except:
        pass

@bot.command(name="stufen")
async def stufen_cmd(ctx):
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(title="📊 Quiz-Stufen", color=0x3498db)
    info = {
        1: "Grundlagen, Ordertypen, Candlesticks, Sessions, Basis-Indikatoren",
        2: "Fibonacci, SMC/ICT, Elliott-Wellen, Fortgeschrittene Indikatoren, Risk Management",
        3: "Wyckoff, VSA, Order Flow, Market Profile, Optionen-Greeks, Makro",
        4: "Stochastische Modelle, Finanzmathematik, Marktmikrostruktur, Quant"
    }
    for s in range(1, 5):
        embed.add_field(
            name=f"{STUFEN_EMOJIS[s]} Stufe {s}: {STUFEN_NAMEN[s]}",
            value=f"{info[s]}\n*{len(STUFEN_POOLS.get(s, []))} Fragen*", inline=False
        )

    msg = await ctx.send(embed=embed)
    await asyncio.sleep(20)
    try:
        await msg.delete()
    except:
        pass

# ============================================================
#                     ADMIN
# ============================================================

@bot.command(name="reset_user")
@commands.has_permissions(administrator=True)
async def reset_user_cmd(ctx, member: discord.Member):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE users SET current_stufe=1, total_correct=0, total_answered=0, total_quizzes=0, total_perfect=0 WHERE user_id=?", (str(member.id),))
    c.execute("DELETE FROM quiz_history WHERE user_id = ?", (str(member.id),))
    conn.commit()
    conn.close()
    await ctx.send(f"🔁 {member.mention} wurde zurückgesetzt.")
    await update_ranking_channel(ctx.guild)

@bot.command(name="set_stufe")
@commands.has_permissions(administrator=True)
async def set_stufe_cmd(ctx, member: discord.Member, stufe: int):
    if stufe < 1 or stufe > 4:
        await ctx.send("❌ Stufe muss zwischen 1 und 4 sein!")
        return
    get_user(member.id, member.display_name)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE users SET current_stufe = ? WHERE user_id = ?", (stufe, str(member.id)))
    conn.commit()
    conn.close()
    await ctx.send(f"✅ {member.mention} → {STUFEN_EMOJIS[stufe]} **Stufe {stufe}: {STUFEN_NAMEN[stufe]}**")

@bot.command(name="setup_quiz")
@commands.has_permissions(administrator=True)
async def setup_quiz_cmd(ctx):
    """Erstellt den Quiz-Info-Kanal mit allen Erklärungen."""
    try:
        await ctx.message.delete()
    except:
        pass

    guild = ctx.guild

    # Kanal finden oder erstellen
    info_channel = discord.utils.get(guild.text_channels, name="quiz-info")
    if not info_channel:
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(
                send_messages=False, read_messages=True, add_reactions=True
            ),
            guild.me: discord.PermissionOverwrite(
                send_messages=True, read_messages=True, manage_messages=True, embed_links=True
            )
        }
        info_channel = await guild.create_text_channel("quiz-info", overwrites=overwrites)
    else:
        try:
            await info_channel.purge(limit=50)
        except:
            pass

    # ─── EMBED 1: WILLKOMMEN ───
    embed1 = discord.Embed(
        title="📚 BullNet Trading Quiz",
        description=(
            "Willkommen beim **BullNet Trading Quiz**! 🎓\n\n"
            "Teste dein Trading-Wissen in **4 Schwierigkeitsstufen** mit über **600 Fragen** "
            "zu allen Bereichen des Tradings – von Grundlagen bis Quant-Level.\n\n"
            "Spiele **Solo** oder fordere andere Mitglieder im **PvP-Modus** heraus! ⚔️"
        ),
        color=0x2b2d31
    )
    embed1.set_image(url="https://i.imgur.com/8QqK0Yj.png")  # Platzhalter
    await info_channel.send(embed=embed1)

    # ─── EMBED 2: WIE FUNKTIONIERT ES? ───
    embed2 = discord.Embed(
        title="🎮 Wie funktioniert das Quiz?",
        color=0x3498db
    )
    embed2.add_field(name="📌 So startest du", value=(
        "Tippe `!quiz` in einen beliebigen Kanal.\n"
        "Der Bot erstellt einen **privaten Kanal** nur für dich.\n"
        "Niemand anderes kann deine Fragen oder Antworten sehen!"
    ), inline=False)
    embed2.add_field(name="📝 Ablauf", value=(
        "• Du bekommst **10 zufällige Fragen** aus deiner aktuellen Stufe\n"
        "• Für jede Frage hast du **60 Sekunden** Zeit\n"
        "• Antworte einfach mit **A**, **B**, **C** oder **D**\n"
        "• Nach jeder Frage siehst du sofort ob es richtig war\n"
        "• Am Ende bekommst du eine **komplette Auswertung** mit allen richtigen Antworten"
    ), inline=False)
    embed2.add_field(name="🎯 Ziel", value=(
        "Beantworte alle **10 Fragen richtig** (10/10) um zur nächsten Stufe aufzusteigen!\n"
        "Schaffst du es nicht, bleibst du auf deiner Stufe und kannst es erneut versuchen."
    ), inline=False)
    await info_channel.send(embed=embed2)

    # ─── EMBED 3: DIE 4 STUFEN ───
    embed3 = discord.Embed(
        title="📊 Die 4 Stufen",
        description="Jede Stufe hat **150 einzigartige Fragen**. Du startest auf Stufe 1.",
        color=0x9b59b6
    )
    embed3.add_field(name="🟢 Stufe 1: Anfänger", value=(
        "Grundlagen des Tradings\n"
        "• Ordertypen (Market, Limit, Stop)\n"
        "• Candlesticks & Charttypen\n"
        "• Sessions (London, NY, Asia)\n"
        "• Basis-Indikatoren (RSI, MACD, MA)\n"
        "• Forex-Grundlagen, Pips, Lots\n"
        "• Wirtschaftskalender (NFP, CPI)\n"
        "*150 Fragen*"
    ), inline=False)
    embed3.add_field(name="🟡 Stufe 2: Fortgeschritten", value=(
        "Technische Analyse & Konzepte\n"
        "• Fibonacci Retracement & Extensions\n"
        "• Smart Money Concepts (BOS, ChoCh, Orderblocks, FVG)\n"
        "• ICT-Konzepte (Kill Zones, OTE, Silver Bullet)\n"
        "• Elliott-Wellen & Harmonische Muster\n"
        "• Fortgeschrittene Indikatoren (ADX, ATR, VWAP, Ichimoku)\n"
        "• Risk Management & Position Sizing\n"
        "*150 Fragen*"
    ), inline=False)
    embed3.add_field(name="🟠 Stufe 3: Profi", value=(
        "Institutionelles Trading & Makro\n"
        "• Wyckoff-Methodik komplett (Akkumulation, Distribution, Spring)\n"
        "• Volume Spread Analysis (VSA)\n"
        "• Order Flow & Footprint Charts\n"
        "• Market Profile & Auction Market Theory\n"
        "• Optionen-Greeks (Delta, Gamma, Theta, Vega)\n"
        "• Makroökonomie (Yield Curve, QE/QT, Credit Spreads)\n"
        "• Statistik (Sharpe Ratio, Monte Carlo, Kelly Criterion)\n"
        "*150 Fragen*"
    ), inline=False)
    embed3.add_field(name="🔴 Stufe 4: Experte", value=(
        "Quant-Level & Finanzmathematik\n"
        "• Stochastische Modelle (GARCH, Heston, Jump-Diffusion)\n"
        "• Finanzmathematik (Itô's Lemma, Martingale, Girsanov)\n"
        "• Marktmikrostruktur (Kyle-Lambda, VPIN, HFT)\n"
        "• Exotische Optionen (Barrier, Asian, Lookback)\n"
        "• FED Liquidity Plumbing (TGA, RRP, Repo)\n"
        "• Fixed Income (Convexity, DV01, Swap Spreads)\n"
        "• Strukturierte Produkte (CDOs, CDS, XVA)\n"
        "*150 Fragen*"
    ), inline=False)
    await info_channel.send(embed=embed3)

    # ─── EMBED 4: PVP MODUS ───
    embed4 = discord.Embed(
        title="⚔️ PvP Modus – Spieler gegen Spieler",
        description="Fordere andere Mitglieder heraus und zeig wer der bessere Trader ist!",
        color=0xe74c3c
    )
    embed4.add_field(name="So funktioniert PvP", value=(
        "1️⃣ Tippe `!pvp @Spieler` um jemanden herauszufordern\n"
        "2️⃣ Der Gegner hat **60 Sekunden** um mit `!accept` anzunehmen\n"
        "3️⃣ Ein **privater PvP-Kanal** wird erstellt (nur ihr zwei)\n"
        "4️⃣ Beide beantworten **dieselben 10 Fragen** gleichzeitig\n"
        "5️⃣ Antworten werden **sofort gelöscht** – kein Abgucken möglich! 👀\n"
        "6️⃣ Am Ende wird der **Gewinner** mit kompletter Auswertung gezeigt"
    ), inline=False)
    embed4.add_field(name="📋 PvP Regeln", value=(
        "• Die Stufe richtet sich nach dem **niedrigeren Level** beider Spieler\n"
        "• PvP zählt **nicht** für den Stufen-Aufstieg\n"
        "• PvP hat ein **eigenes Ranking** mit Wins, Losses & Draws\n"
        "• Mit `!decline` kannst du eine Herausforderung ablehnen"
    ), inline=False)
    await info_channel.send(embed=embed4)

    # ─── EMBED 5: RANKING ───
    embed5 = discord.Embed(
        title="🏆 Ranking-System",
        description="Zwei separate Rankings für Solo und PvP!",
        color=0xf1c40f
    )
    embed5.add_field(name="🏆 Solo-Ranking", value=(
        "Sortiert nach:\n"
        "1. **Höchste Stufe** erreicht\n"
        "2. **Perfekte Runden** (10/10) 🌟\n"
        "3. **Trefferquote** insgesamt\n\n"
        "Das Ranking wird automatisch in **#quiz-ranking** aktualisiert."
    ), inline=True)
    embed5.add_field(name="⚔️ PvP-Ranking", value=(
        "Sortiert nach:\n"
        "1. **Anzahl Siege**\n"
        "2. **Richtige Antworten** insgesamt\n"
        "3. **Winrate** in Prozent\n\n"
        "Wer wird der PvP-Champion? 👑"
    ), inline=True)
    await info_channel.send(embed=embed5)

    # ─── EMBED 6: ALLE BEFEHLE ───
    embed6 = discord.Embed(
        title="⌨️ Alle Befehle",
        color=0x2ecc71
    )
    embed6.add_field(name="🎮 Solo Quiz", value=(
        "```\n"
        "!quiz          Startet ein Quiz auf deiner Stufe\n"
        "!stats         Zeigt deine persönlichen Statistiken\n"
        "!ranking       Aktualisiert das Ranking\n"
        "!stufen        Zeigt alle Stufen-Details\n"
        "!hilfe         Zeigt alle Befehle\n"
        "```"
    ), inline=False)
    embed6.add_field(name="⚔️ PvP Quiz", value=(
        "```\n"
        "!pvp @Spieler  Fordere jemanden heraus\n"
        "!accept        Herausforderung annehmen\n"
        "!decline       Herausforderung ablehnen\n"
        "```"
    ), inline=False)
    embed6.add_field(name="🔑 Admin", value=(
        "```\n"
        "!setup_quiz         Quiz-Info Kanal erstellen\n"
        "!reset_user @User   User komplett zurücksetzen\n"
        "!set_stufe @User 3  Stufe eines Users setzen\n"
        "```"
    ), inline=False)
    await info_channel.send(embed=embed6)

    # ─── EMBED 7: TIPPS ───
    embed7 = discord.Embed(
        title="💡 Tipps & Hinweise",
        color=0xe67e22
    )
    embed7.add_field(name="📖 Lernstrategie", value=(
        "• Spiele regelmäßig – Wiederholung ist der Schlüssel!\n"
        "• Lies dir die **richtigen Antworten** am Ende genau durch\n"
        "• Recherchiere Themen, bei denen du unsicher warst\n"
        "• Die Fragen werden **zufällig** ausgewählt – jedes Quiz ist anders\n"
        "• Es gibt **keine Strafe** für falsche Antworten – also probiere es!"
    ), inline=False)
    embed7.add_field(name="⚠️ Wichtig", value=(
        "• Dein Quiz-Kanal ist **nur für dich sichtbar**\n"
        "• Der Kanal wird **30 Sekunden** nach dem Quiz automatisch gelöscht\n"
        "• Dein Fortschritt wird **permanent gespeichert**\n"
        "• Du kannst das Quiz **beliebig oft** wiederholen\n"
        "• Bei Problemen wende dich an einen Admin"
    ), inline=False)
    await info_channel.send(embed=embed7)

    # ─── EMBED 8: START ───
    embed8 = discord.Embed(
        title="🚀 Bereit? Los geht's!",
        description=(
            "Tippe **`!quiz`** in einen beliebigen Kanal und starte dein erstes Quiz!\n\n"
            "Viel Erfolg und viel Spaß! 💪📈"
        ),
        color=0x00ff00
    )
    await info_channel.send(embed=embed8)

    msg = await ctx.send(f"✅ Quiz-Info Kanal erstellt: {info_channel.mention}")
    await asyncio.sleep(5)
    try:
        await msg.delete()
    except:
        pass

# ============================================================
#                     START
# ============================================================

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ FEHLER: DISCORD_TOKEN nicht in .env gefunden!")
    else:
        bot.run(TOKEN)
