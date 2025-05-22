import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

user_scores = {}
active_questions = {}
greeted_users = set()

# Fragenpools
quiz_easy = [
    {"question": "Was ist ein 'Stop-Loss'?", "options": ["A) Gewinnziel", "B) Verlustbegrenzung", "C) Ordertyp", "D) Candlestick"], "answer": "B"},
    {"question": "Was zeigt ein grüner Candlestick?", "options": ["A) Kurs fällt", "B) Markt ist offen", "C) Kurs steigt", "D) Keine Aussage"], "answer": "C"},
    ... (weitere Fragen wie bereits vorhanden)
]

quiz_medium = [
    {"question": "Was ist der RSI?", "options": ["A) Indikator für Volumen", "B) Relative Strength Index", "C) Risikokonto", "D) Fundamentalanalyse"], "answer": "B"},
    ...
]

quiz_hard = [
    {"question": "Was ist ein Drawdown?", "options": ["A) Maximaler Gewinn", "B) Rückgang vom Hoch zum Tief", "C) Hebelverlust", "D) Seitwärtsphase"], "answer": "B"},
    ...
]

@bot.command()
async def start(ctx):
    await ctx.send(
        f"👋 Hallo {ctx.author.mention}! Willkommen beim **Trading-Quiz**! 🎓\n"
        "Du kannst direkt loslegen mit einem der folgenden Befehle:\n"
        "`!quiz leicht` – für Einsteiger\n"
        "`!quiz mittel` – für Fortgeschrittene\n"
        "`!quiz schwer` – für Profis\n\n"
        "Beantworte jede Frage mit `A`, `B`, `C` oder `D`. Viel Erfolg! 💪"
    )

@bot.command()
async def quiz(ctx, stufe: str):
    difficulty_map = {
        "leicht": (quiz_easy, 1),
        "mittel": (quiz_medium, 2),
        "schwer": (quiz_hard, 3)
    }

    stufe = stufe.lower()
    if stufe not in difficulty_map:
        await ctx.send("Verwende bitte: `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`")
        return

    if ctx.author.id not in greeted_users:
        greeted_users.add(ctx.author.id)
        await ctx.send(
            f"👋 Willkommen im Trading-Quiz, {ctx.author.mention}!\n"
            "Beantworte einfach mit A, B, C oder D! 📈"
        )

    fragen, punkte = difficulty_map[stufe]
    frage = random.choice(fragen)
    active_questions[ctx.author.id] = (frage, punkte)

    frage_text = f"🎯 **{frage['question']}**\n"
    frage_text += "\n".join(frage["options"])
    frage_text += "\n\nAntworte mit **A**, **B**, **C** oder **D**"
    await ctx.send(frage_text)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    if message.author.id in active_questions:
        frage, punkte = active_questions[message.author.id]
        user_answer = message.content.strip().upper()

        if user_answer == frage["answer"]:
            user_scores[message.author.id] = user_scores.get(message.author.id, 0) + punkte
            responses = [
                f"✅ Richtig, {message.author.mention}! +{punkte} Punkte! 🎉",
                f"🎯 Stimmt genau! {punkte} Punkte für {message.author.name}!",
                f"🔥 {message.author.mention} trifft ins Schwarze! +{punkte} Punkte!"
            ]
            await message.channel.send(random.choice(responses))
        else:
            await message.channel.send(f"❌ Falsch, {message.author.mention}. Die richtige Antwort war **{frage['answer']}**.")

        score = user_scores.get(message.author.id, 0)
        ranking = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        rank = [uid for uid, _ in ranking].index(message.author.id) + 1
        total = len(ranking)

        await message.channel.send(
            f"📊 Punktestand: **{score}**\n🏆 Rang: **Platz {rank} von {total} Spielern**"
        )

        del active_questions[message.author.id]

@bot.command()
async def ranking(ctx):
    if not user_scores:
        await ctx.send("Noch keine Punkte vergeben worden.")
        return

    ranking = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    lines = ["🏆 **Top 10 Spieler:**"]
    for i, (user_id, score) in enumerate(ranking[:10], 1):
        user = await bot.fetch_user(user_id)
        lines.append(f"{i}. {user.name} – {score} Punkte")

    await ctx.send("\n".join(lines))

@bot.event
async def on_member_join(member):
    try:
        quiz_channel_id = int(os.environ.get("QUIZ_CHANNEL_ID"))
        channel = bot.get_channel(quiz_channel_id)
        if channel:
            await channel.send(
                f"👋 Willkommen im Trading-Quiz, {member.mention}!\n"
                "Starte mit `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`! 🌟"
            )
    except Exception as e:
        print(f"Fehler beim Senden der Willkommensnachricht: {e}")

bot.run(os.environ["DISCORD_BOT_TOKEN"])
