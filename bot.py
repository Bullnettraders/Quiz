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

# --- Alle 60 Fragen (leicht, mittel, schwer) ---

quiz_easy = [
    {"question": "Was ist ein 'Stop-Loss'?", "options": ["A) Gewinnziel", "B) Verlustbegrenzung", "C) Ordertyp", "D) Candlestick"], "answer": "B"},
    {"question": "Was zeigt ein grüner Candlestick?", "options": ["A) Kurs fällt", "B) Markt ist offen", "C) Kurs steigt", "D) Keine Aussage"], "answer": "C"},
    {"question": "Was bedeutet 'Buy Low, Sell High'?", "options": ["A) Leerverkauf", "B) Markt meiden", "C) Günstig kaufen, teuer verkaufen", "D) Nur kaufen bei Ausbruch"], "answer": "C"},
    {"question": "Was ist ein Markttrend?", "options": ["A) Zufallsbewegung", "B) Langfristige Kursrichtung", "C) Volumensignal", "D) Ordertyp"], "answer": "B"},
    {"question": "Was ist ein Broker?", "options": ["A) Handelsplattform", "B) Analyseprogramm", "C) Chart", "D) Kerze"], "answer": "A"},
    {"question": "Was ist ein Candlestick?", "options": ["A) Order", "B) Preisverlauf", "C) Indikator", "D) Trading-Strategie"], "answer": "B"},
    {"question": "Was ist ein Spread?", "options": ["A) Unterschied zwischen Kauf- und Verkaufspreis", "B) Trend", "C) Verlust", "D) Gewinn"], "answer": "A"},
    {"question": "Was ist eine Long-Position?", "options": ["A) Leerverkauf", "B) Wette auf steigende Kurse", "C) Wette auf fallende Kurse", "D) Sicherheit"], "answer": "B"},
    {"question": "Was ist eine Short-Position?", "options": ["A) Wette auf steigende Kurse", "B) Wette auf fallende Kurse", "C) Kauf", "D) Breakout"], "answer": "B"},
    {"question": "Was bedeutet Volumen im Trading?", "options": ["A) Geräuschpegel", "B) Anzahl gehandelter Einheiten", "C) Kursverlauf", "D) Gewinn"], "answer": "B"},
    {"question": "Was ist eine Unterstützung (Support)?", "options": ["A) Verkaufsbereich", "B) Preiszone, in der Nachfrage steigt", "C) Trading-Stil", "D) Broker"], "answer": "B"},
    {"question": "Was ist ein Widerstand (Resistance)?", "options": ["A) Kursgrenze nach unten", "B) Kursgrenze nach oben", "C) Indikator", "D) News"], "answer": "B"},
    {"question": "Was bedeutet Take-Profit?", "options": ["A) Verlustgrenze", "B) Gewinnmitnahme", "C) Kauf-Order", "D) Risiko"], "answer": "B"},
    {"question": "Was ist ein Demo-Konto?", "options": ["A) Konto mit Echtgeld", "B) Übungskonto mit Spielgeld", "C) Broker-Konto", "D) Depot"], "answer": "B"},
    {"question": "Was ist ein Hebel (Leverage)?", "options": ["A) Kursanzeige", "B) Multiplikator für Gewinne/Verluste", "C) Chartmuster", "D) Stop-Loss"], "answer": "B"},
    {"question": "Was bedeutet Liquidität?", "options": ["A) Verkaufsmenge", "B) Handelsfähigkeit eines Markts", "C) Verlustzone", "D) Gewinnquote"], "answer": "B"},
    {"question": "Was ist ein Indikator?", "options": ["A) Kursbewegung", "B) Analysewerkzeug", "C) Ordertyp", "D) Chart"], "answer": "B"},
    {"question": "Was bedeutet FOMO?", "options": ["A) Angst, einen Trade zu verpassen", "B) Trading-Strategie", "C) Indikator", "D) Hebelwirkung"], "answer": "A"},
    {"question": "Was ist ein Portfolio?", "options": ["A) Eine Aktie", "B) Alle gehaltenen Investitionen", "C) Nur Futures", "D) Kontoauszug"], "answer": "B"},
    {"question": "Was ist Scalping?", "options": ["A) Langfristiger Handel", "B) Kurzfristiger Handel mit kleinen Gewinnen", "C) Fundamentalstrategie", "D) Trading-Analyse"], "answer": "B"}
]

# quiz_medium und quiz_hard kommen hier ebenfalls rein mit je 20 Fragen
# (aus Platzgründen lasse ich sie hier weg, aber du kannst sie wie bei quiz_easy erweitern)

# --- Quiz-Befehle und Logik ---

@bot.command()
async def start(ctx):
    await ctx.send(
        f"👋 Hallo {ctx.author.mention}! Willkommen beim **Trading-Quiz**! 🎓\n"
        "Starte mit `!quiz leicht`, `!quiz mittel`, `!quiz schwer` und antworte mit A–D oder dem Antworttext."
    )

@bot.command()
async def quiz(ctx, stufe: str):
    difficulty_map = {
        "leicht": (quiz_easy, 1),
        # "mittel": (quiz_medium, 2),
        # "schwer": (quiz_hard, 3)
    }

    stufe = stufe.lower()
    if stufe not in difficulty_map:
        await ctx.send("Verwende: `!quiz leicht`, `!quiz mittel`, `!quiz schwer`.")
        return

    fragen, punkte = difficulty_map[stufe]
    frage = random.choice(fragen)
    active_questions[ctx.author.id] = (frage, punkte)

    frage_text = f"🎯 **{frage['question']}**\n" + "\n".join(frage['options'])
    await ctx.send(frage_text + "\n\nAntworte mit **A**, **B**, **C**, **D** oder dem Antworttext.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    if message.author.id in active_questions:
        frage, punkte = active_questions[message.author.id]
        user_input = message.content.strip().upper()
        correct_letter = frage['answer']
        correct_text = next(opt[3:].strip().upper() for opt in frage['options'] if opt.startswith(correct_letter))

        if user_input == correct_letter or user_input == correct_text:
            user_scores[message.author.id] = user_scores.get(message.author.id, 0) + punkte
            await message.channel.send(f"✅ Richtig, {message.author.mention}! +{punkte} Punkte!")
        else:
            await message.channel.send(f"❌ Falsch. Die richtige Antwort war **{correct_letter} – {correct_text.title()}**.")

        del active_questions[message.author.id]

@bot.command()
async def ranking(ctx):
    if not user_scores:
        await ctx.send("Noch keine Punkte vergeben.")
        return

    ranking = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    lines = ["🏆 **Top 10 Spieler:**"]
    for i, (user_id, score) in enumerate(ranking[:10], 1):
        user = await bot.fetch_user(user_id)
        lines.append(f"{i}. {user.name} – {score} Punkte")

    await ctx.send("\n".join(lines))

bot.run(os.environ["DISCORD_BOT_TOKEN"])
