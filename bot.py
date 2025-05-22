import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# In-Memory Punktesystem
user_scores = {}
active_questions = {}

# Fragenpools
quiz_easy = [
    {"question": "Was ist ein 'Stop-Loss'?", "options": ["A) Gewinnziel", "B) Verlustbegrenzung", "C) Ordertyp", "D) Candlestick"], "answer": "B"},
    {"question": "Was zeigt ein grüner Candlestick?", "options": ["A) Kurs fällt", "B) Markt ist offen", "C) Kurs steigt", "D) Keine Aussage"], "answer": "C"},
    {"question": "Was bedeutet 'Buy Low, Sell High'?", "options": ["A) Leerverkauf", "B) Markt meiden", "C) Günstig kaufen, teuer verkaufen", "D) Nur kaufen bei Ausbruch"], "answer": "C"},
    {"question": "Was ist ein Candlestick?", "options": ["A) Preisalarm", "B) Handelsstrategie", "C) Darstellung von Kursverlauf", "D) Orderart"], "answer": "C"},
    {"question": "Was ist 'Volumen'?", "options": ["A) Anzahl gehandelter Einheiten", "B) Kursbewegung", "C) Chartmuster", "D) Zeiteinheit"], "answer": "A"},
    {"question": "Was bedeutet 'Support'?", "options": ["A) Widerstand", "B) Preisunterstützung", "C) Stop-Loss", "D) Hebel"], "answer": "B"},
    {"question": "Was ist ein Widerstand?", "options": ["A) Kursziel", "B) Preis, an dem Verkäufe zunehmen", "C) Stop-Loss-Zone", "D) Volumenindikator"], "answer": "B"},
    {"question": "Was zeigt ein Doji?", "options": ["A) Unsicherheit", "B) Crash", "C) Ausbruch", "D) Trendbestätigung"], "answer": "A"},
    {"question": "Was ist eine Long-Position?", "options": ["A) Verkauf", "B) Absicherung", "C) Kauf mit steigender Kurs-Erwartung", "D) Verlust"], "answer": "C"},
    {"question": "Was ist ein Short?", "options": ["A) Verkauf leerer Positionen", "B) Kaufstrategie", "C) Stop-Loss", "D) Volumenbegriff"], "answer": "A"},
    {"question": "Was macht ein Trading-Bot?", "options": ["A) Analysiert Märkte", "B) Führt Trades automatisch aus", "C) Sendet News", "D) Gibt Kurse aus"], "answer": "B"},
    {"question": "Was ist ein Broker?", "options": ["A) Marktplatz", "B) Händler", "C) Plattform für Trading", "D) Alles davon"], "answer": "D"},
    {"question": "Was ist ein Hebel (Leverage)?", "options": ["A) Risiko-Reduktion", "B) Kursglättung", "C) Kapitalverstärker", "D) Volumenindikator"], "answer": "C"},
    {"question": "Was ist 'Take Profit'?", "options": ["A) Verlustbegrenzung", "B) Kursziel", "C) Risikomanagement", "D) Trade beenden"], "answer": "B"},
    {"question": "Was ist ein Trend?", "options": ["A) Seitwärtsbewegung", "B) Kursrichtung", "C) Widerstand", "D) Indikator"], "answer": "B"},
    {"question": "Was macht ein Trader?", "options": ["A) Beobachtet nur", "B) Handelt aktiv", "C) Gibt Signale", "D) Erfindet Coins"], "answer": "B"},
    {"question": "Was ist ein Spread?", "options": ["A) Kursbewegung", "B) Unterschied zwischen Kauf-/Verkaufspreis", "C) Trendindikator", "D) Short-Position"], "answer": "B"},
    {"question": "Was ist 'Daytrading'?", "options": ["A) Langfristiges Investieren", "B) Handeln an einem Tag", "C) Scalping", "D) Wochen-Trading"], "answer": "B"},
    {"question": "Was bedeutet 'Liquidität'?", "options": ["A) Handelbarkeit", "B) Kursglätte", "C) Verlustabsicherung", "D) Trendmenge"], "answer": "A"},
    {"question": "Was ist ein Konto mit virtuellem Geld?", "options": ["A) Wallet", "B) Testkonto", "C) Risiko-Konto", "D) Bot-Konto"], "answer": "B"}
]

quiz_medium = [
    {"question": "Was misst der RSI?", "options": ["A) Volumen", "B) Volatilität", "C) Trendstärke", "D) Überkauft-/Überverkauft-Zonen"], "answer": "D"},
    {"question": "Was ist ein 'Double Top'?", "options": ["A) Bullisches Signal", "B) Konsolidierung", "C) Trendwendemuster nach oben", "D) Trendwendemuster nach unten"], "answer": "D"},
    {"question": "Was ist ein gleitender Durchschnitt (MA)?", "options": ["A) Glättung der Kursbewegung", "B) Volumendurchschnitt", "C) RSI-Alternative", "D) Stop-Loss-Tool"], "answer": "A"},
    # +17 Fragen dazu ergänzen wie oben
]

quiz_hard = [
    {"question": "Was ist ein Drawdown?", "options": ["A) Maximaler Gewinn", "B) Rückgang vom Höchstwert zum Tief", "C) Hebelverlust", "D) Seitwärtsphase"], "answer": "B"},
    {"question": "Was bedeutet 'Risk:Reward Ratio' von 1:3?", "options": ["A) Mehr Risiko als Gewinn", "B) 3-mal so hoher Verlust wie Gewinn", "C) Für 1 Risiko-Einheit werden 3 Gewinn erwartet", "D) 3-mal geringeres Risiko"], "answer": "C"},
    {"question": "Was ist eine 'Bullenfalle'?", "options": ["A) Fehlausbruch nach oben", "B) Reales Kaufsignal", "C) Volumenmangel", "D) Short Squeeze"], "answer": "A"},
    # +17 Fragen dazu ergänzen wie oben
]

difficulty_map = {
    "leicht": (quiz_easy, 1),
    "mittel": (quiz_medium, 2),
    "schwer": (quiz_hard, 3)
}

@bot.event
async def on_ready():
    print(f"✅ Bot aktiv als {bot.user}")

@bot.command()
async def quiz(ctx, stufe: str):
    stufe = stufe.lower()
    if stufe not in difficulty_map:
        await ctx.send("Verwende bitte: `!quiz leicht`, `!quiz mittel` oder `!quiz schwer`")
        return

    fragen, punkte = difficulty_map[stufe]
    frage = random.choice(fragen)
    active_questions[ctx.author.id] = (frage, punkte)

    frage_text = f"🎯 **{frage['question']}**\n"
    frage_text += "\n".join(frage["options"])
    frage_text += "\n\nBitte antworte mit **A**, **B**, **C** oder **D**"
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
                f"✅ Richtig, {message.author.mention}! +{punkte} Punkte für dich! 🎉",
                f"🎯 Nice! Das stimmt! {punkte} Punkte gehen an {message.author.name}!",
                f"🔥 Boom! {message.author.mention} legt nach – +{punkte} Punkte!"
            ]
            await message.channel.send(random.choice(responses))
        else:
            await message.channel.send(f"❌ Leider falsch, {message.author.mention}. Die richtige Antwort war **{frage['answer']}**.")

        del active_questions[message.author.id]

@bot.command()
async def ranking(ctx):
    if not user_scores:
        await ctx.send("Noch keine Punkte vergeben worden.")
        return

    ranking = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    lines = [f"🏆 **Top Trader Quiz-Spieler** 🧠"]
    for i, (user_id, score) in enumerate(ranking[:10], 1):
        user = await bot.fetch_user(user_id)
        lines.append(f"{i}. {user.name} – {score} Punkte")

    await ctx.send("\n".join(lines))

bot.run(os.environ["DISCORD_BOT_TOKEN"])
