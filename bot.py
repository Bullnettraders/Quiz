import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Wichtig für on_member_join

bot = commands.Bot(command_prefix="!", intents=intents)

# Datenstrukturen
user_scores = {}
active_questions = {}
greeted_users = set()

# Channel-ID deines Quiz-Channels (ersetzen mit deiner echten ID)
quiz_channel_id = 123456789012345678  # <-- Hier deine Channel-ID einsetzen

# Fragenpools (jeweils nur 3 beispielhaft - du kannst bis 20 pro Block ergänzen)
quiz_easy = [
    {"question": "Was ist ein 'Stop-Loss'?", "options": ["A) Gewinnziel", "B) Verlustbegrenzung", "C) Ordertyp", "D) Candlestick"], "answer": "B"},
    {"question": "Was zeigt ein grüner Candlestick?", "options": ["A) Kurs fällt", "B) Markt ist offen", "C) Kurs steigt", "D) Keine Aussage"], "answer": "C"},
    {"question": "Was bedeutet 'Buy Low, Sell High'?", "options": ["A) Leerverkauf", "B) Markt meiden", "C) Günstig kaufen, teuer verkaufen", "D) Nur kaufen bei Ausbruch"], "answer": "C"}
]

quiz_medium = [
    {"question": "Was misst der RSI?", "options": ["A) Volumen", "B) Volatilität", "C) Trendstärke", "D) Überkauft-/Überverkauft-Zonen"], "answer": "D"},
    {"question": "Was ist ein 'Double Top'?", "options": ["A) Bullisches Signal", "B) Konsolidierung", "C) Trendwendemuster nach oben", "D) Trendwendemuster nach unten"], "answer": "D"},
    {"question": "Was ist ein gleitender Durchschnitt (MA)?", "options": ["A) Glättung der Kursbewegung", "B) Volumendurchschnitt", "C) RSI-Alternative", "D) Stop-Loss-Tool"], "answer": "A"}
]

quiz_hard = [
    {"question": "Was ist ein Drawdown?", "options": ["A) Maximaler Gewinn", "B) Rückgang vom Höchstwert zum Tief", "C) Hebelverlust", "D) Seitwärtsphase"], "answer": "B"},
    {"question": "Was bedeutet 'Risk:Reward Ratio' von 1:3?", "options": ["A) Mehr Risiko als Gewinn", "B) 3-mal so hoher Verlust wie Gewinn", "C) Für 1 Risiko-Einheit werden 3 Gewinn erwartet", "D) 3-mal geringeres Risiko"], "answer": "C"},
    {"question": "Was ist eine 'Bullenfalle'?", "options": ["A) Fehlausbruch nach oben", "B) Reales Kaufsignal", "C) Volumenmangel", "D) Short Squeeze"], "answer": "A"}
]

difficulty_map = {
    "leicht": (quiz_easy, 1),
    "mittel": (quiz_medium, 2),
    "schwer": (quiz_hard, 3)
}

@bot.event
async def on_ready():
    print(f"✅ Bot aktiv als {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(quiz_channel_id)
    if channel:
        await channel.send(
            f"👋 Willkommen im Trading-Quiz, {member.mention}!\n"
            "Starte mit `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`! 🌟"
        )

@bot.command()
async def quiz(ctx, stufe: str):
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
    lines = [f"🏆 **Top 10 Spieler:**"]
    for i, (user_id, score) in enumerate(ranking[:10], 1):
        user = await bot.fetch_user(user_id)
        lines.append(f"{i}. {user.name} – {score} Punkte")

    await ctx.send("\n".join(lines))

# Bot starten (Token über Umgebungsvariable in Railway setzen)
bot.run(os.environ["DISCORD_BOT_TOKEN"])
