import discord
from discord.ext import commands
import os
import random
import asyncio
import json
from dotenv import load_dotenv

# Importiere den Fragenpool aus der separaten Datei
try:
    from fragenpool import quiz_easy, quiz_medium, quiz_hard
except ImportError:
    print("❌ Fehler: fragenpool.py wurde nicht gefunden oder enthält Fehler!")

# Lade Umgebungsvariablen (für Token)
load_dotenv()

# Discord-Intents konfigurieren
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Konfigurations-Variablen
SCORE_FILE = "scores.json"
QUIZ_CATEGORY_NAME = "QUIZ"
user_scores = {}
active_questions = {}

# --- Datenverwaltung ---

def load_scores():
    """Lädt die Punktestände aus der JSON-Datei."""
    global user_scores
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                user_scores = json.load(f)
        except Exception as e:
            print(f"❌ Fehler beim Laden der Scores: {e}")
            user_scores = {}
    else:
        user_scores = {}

def save_scores():
    """Speichert die Punktestände in der JSON-Datei."""
    try:
        with open(SCORE_FILE, "w") as f:
            json.dump(user_scores, f, indent=4)
    except Exception as e:
        print(f"❌ Fehler beim Speichern der Scores: {e}")

# --- Bot Events ---

@bot.event
async def on_ready():
    print(f"✅ Bot ist eingeloggt als {bot.user}")
    load_scores()
    
    # Automatische Erstellung des Ranking-Kanals in allen Servern
    for guild in bot.guilds:
        ranking_channel = discord.utils.get(guild.text_channels, name="ranking")
        if ranking_channel is None:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=True),
                guild.me: discord.PermissionOverwrite(send_messages=True, read_messages=True)
            }
            await guild.create_text_channel("ranking", overwrites=overwrites)
            print(f"📢 Ranking-Kanal in {guild.name} erstellt.")

# --- Quiz Befehle ---

@bot.command()
async def start(ctx):
    """Willkommensnachricht."""
    await ctx.message.delete()
    msg = await ctx.send(
        f"👋 Hallo {ctx.author.mention}! Willkommen beim **Trading-Quiz**! 🎓\n"
        "Starte mit `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`.\n"
        "Ich erstelle dir dann einen privaten Kanal für deine Frage."
    )
    await asyncio.sleep(15)
    await msg.delete()

@bot.command()
async def quiz(ctx, stufe: str = None):
    """Startet eine Quiz-Frage in einem neuen Kanal."""
    if stufe:
        await ctx.message.delete()
    
    difficulty_map = {
        "leicht": (quiz_easy, 1),
        "mittel": (quiz_medium, 2),
        "schwer": (quiz_hard, 3)
    }

    stufe = stufe.lower() if stufe else ""
    if stufe not in difficulty_map:
        msg = await ctx.send("❌ Bitte nutze: `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`.")
        await asyncio.sleep(10)
        await msg.delete()
        return

    # Kategorie finden oder erstellen
    guild = ctx.guild
    category = discord.utils.get(guild.categories, name=QUIZ_CATEGORY_NAME)
    if not category:
        category = await guild.create_category(QUIZ_CATEGORY_NAME)

    # Privaten Kanal erstellen
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }

    quiz_channel = await guild.create_text_channel(
        f"quiz-{ctx.author.name.lower()}",
        overwrites=overwrites,
        category=category
    )

    # Frage auswählen
    fragen, punkte = difficulty_map[stufe]
    frage = random.choice(fragen)
    active_questions[ctx.author.id] = (frage, punkte, quiz_channel.id)

    # Nachricht im Quiz-Kanal senden
    frage_text = f"🎯 **{frage['question']}**\n\n" + "\n".join(frage['options'])
    await quiz_channel.send(
        f"{ctx.author.mention}, hier ist deine Frage:\n\n{frage_text}\n\n"
        "Antworte mit **A**, **B**, **C** oder **D**."
    )

    msg = await ctx.send(f"📬 {ctx.author.mention}, dein Quiz wartet in {quiz_channel.mention}!")
    await asyncio.sleep(10)
    await msg.delete()

# Aliase für die Schwierigkeitsgrade
@bot.command()
async def leicht(ctx): await quiz(ctx, "leicht")

@bot.command()
async def mittel(ctx): await quiz(ctx, "mittel")

@bot.command()
async def schwer(ctx): await quiz(ctx, "schwer")

# --- Logik für Antworten ---

@bot.event
async def on_message(message):
    # Commands ganz normal verarbeiten
    await bot.process_commands(message)
    
    if message.author.bot:
        return

    # Prüfen, ob der User gerade ein aktives Quiz in diesem Kanal hat
    if message.author.id in active_questions:
        frage, punkte, channel_id = active_questions[message.author.id]
        
        if message.channel.id != channel_id:
            return

        user_input = message.content.strip().upper()
        correct_letter = frage["answer"].upper()
        
        # Richtige Antwort finden für den Vergleich des Textes
        correct_option = next(opt for opt in frage["options"] if opt.startswith(correct_letter))
        correct_text = correct_option[3:].strip().upper()

        # Validierung
        if user_input == correct_letter or user_input == correct_text:
            user_scores[str(message.author.id)] = user_scores.get(str(message.author.id), 0) + punkte
            await message.channel.send(f"✅ **Richtig!** +{punkte} Punkte wurden gutgeschrieben.")
        else:
            await message.channel.send(f"❌ **Falsch.** Die richtige Antwort war: **{correct_option}**")

        # Quiz beenden
        del active_questions[message.author.id]
        save_scores()
        
        await message.channel.send("🧹 Dieser Kanal wird in 10 Sekunden automatisch gelöscht...")
        await asyncio.sleep(10)
        await message.channel.delete()

        # Ranking-Kanal im Server aktualisieren
        await update_ranking(message.guild)

async def update_ranking(guild):
    """Aktualisiert die Top 10 Liste im Ranking-Kanal."""
    ranking_channel = discord.utils.get(guild.text_channels, name="ranking")
    if ranking_channel:
        ranking_sorted = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        lines = ["🏆 **TRADING-QUIZ RANKING** 🏆", "---"]
        
        for i, (user_id, score) in enumerate(ranking_sorted[:10], 1):
            try:
                user = await bot.fetch_user(int(user_id))
                name = user.display_name
            except:
                name = f"Unbekannter User ({user_id})"
            lines.append(f"**{i}. {name}** — {score} Punkte")
        
        await ranking_channel.purge(limit=5) # Alte Nachrichten löschen
        await ranking_channel.send("\n".join(lines))

# --- Statistiken & Admin ---

@bot.command()
async def stats(ctx):
    """Zeigt den eigenen Punktestand."""
    await ctx.message.delete()
    punkte = user_scores.get(str(ctx.author.id), 0)
    msg = await ctx.send(f"📊 {ctx.author.mention}, du hast aktuell **{punkte} Punkte**.")
    await asyncio.sleep(10)
    await msg.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx, member: discord.Member):
    """Setzt Punkte eines Users zurück (Nur Admins)."""
    user_id = str(member.id)
    if user_id in user_scores:
        user_scores[user_id] = 0
        save_scores()
        await ctx.send(f"🔁 Punktestand von {member.mention} wurde zurückgesetzt.")
        await update_ranking(ctx.guild)
    else:
        await ctx.send(f"ℹ️ {member.mention} hat noch keine Punkte.")

# --- Start ---

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ FEHLER: DISCORD_TOKEN nicht gefunden!")
    else:
        bot.run(TOKEN)
