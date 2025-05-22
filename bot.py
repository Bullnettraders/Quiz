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
    {"question": "Was ist ein 'Stop-Loss'?", "options": ["A) Gewinnziel", "B) Verlustbegrenzung", "C) Ordertyp", "D) Candlestick"]
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

quiz_medium = [
    {"question": "Was ist der RSI?", "options": ["A) Indikator für Volumen", "B) Relative Strength Index", "C) Risikokonto", "D) Fundamentalanalyse"], "answer": "B"},
    {"question": "Was bedeutet eine divergierende RSI-Anzeige?", "options": ["A) Trendbestätigung", "B) Trendumkehr", "C) Volumenanstieg", "D) Seitwärtsphase"], "answer": "B"},
    {"question": "Was ist der MACD?", "options": ["A) Momentum-Indikator", "B) News-Plattform", "C) Broker", "D) Trading-Stil"], "answer": "A"},
    {"question": "Was ist ein Bollinger Band?", "options": ["A) Volumenindikator", "B) Trendband mit Volatilitätsausdruck", "C) Breakout-Signal", "D) Verlustanzeige"], "answer": "B"},
    {"question": "Was ist ein Breakout?", "options": ["A) Kurs steigt stark", "B) Kurs durchbricht Widerstand/Unterstützung", "C) Kurs fällt", "D) Seitwärtsbewegung"], "answer": "B"},
    {"question": "Was zeigt ein Doji?", "options": ["A) Unsicherheit im Markt", "B) Kursanstieg", "C) Trendfortsetzung", "D) Volumenanstieg"], "answer": "A"},
    {"question": "Was ist eine Flagge im Chart?", "options": ["A) Konsolidierungsmuster", "B) Umkehrmuster", "C) News", "D) Trendbruch"], "answer": "A"},
    {"question": "Was beschreibt ein Double Top?", "options": ["A) Fortsetzung", "B) Trendumkehr", "C) Indikator", "D) Volumensignal"], "answer": "B"},
    {"question": "Was ist ein Fibonacci-Retracement?", "options": ["A) Preisziel", "B) Unterstützungs-/Widerstandszonen basierend auf Zahlenfolge", "C) Chartmuster", "D) Leerverkauf"], "answer": "B"},
    {"question": "Was ist ein Volumenindikator?", "options": ["A) Stop-Loss", "B) RSI", "C) On-Balance Volume", "D) Bollinger"], "answer": "C"},
    {"question": "Was ist eine Range?", "options": ["A) Trendrichtung", "B) Seitwärtsphase zwischen zwei Kursgrenzen", "C) Ordertyp", "D) Risiko"], "answer": "B"},
    {"question": "Was ist das Ziel von Technischer Analyse?", "options": ["A) Fundamentaldaten prüfen", "B) Chartmuster erkennen", "C) Broker vergleichen", "D) Volumen messen"], "answer": "B"},
    {"question": "Was ist ein Ausbruch nach oben?", "options": ["A) Rückgang", "B) Preis sinkt", "C) Preis steigt über Widerstand", "D) Konsolidierung"], "answer": "C"},
    {"question": "Was ist ein Dreieck im Chart?", "options": ["A) Seitwärtsmuster", "B) Konsolidierungsmuster mit enger werdender Spanne", "C) Volumenzone", "D) Risikoindikator"], "answer": "B"},
    {"question": "Was ist ein gleitender Durchschnitt (MA)?", "options": ["A) Glättung der Kursbewegung", "B) Volumendurchschnitt", "C) RSI-Alternative", "D) Stop-Loss-Tool"], "answer": "A"},
    {"question": "Was ist ein Volatilitätsindikator?", "options": ["A) Bollinger Bänder", "B) Fibonacci", "C) RSI", "D) Order Flow"], "answer": "A"},
    {"question": "Was ist ein Fakeout?", "options": ["A) Starker Trend", "B) Fehlausbruch", "C) Candlestick", "D) Volumendruck"], "answer": "B"},
    {"question": "Was bedeutet \"Overbought\" im RSI?", "options": ["A) Überverkauft", "B) Stark gestiegener Kurs, mögliches Verkaufssignal", "C) Tradingpause", "D) Signal zum Kaufen"], "answer": "B"},
    {"question": "Was ist eine Korrektur?", "options": ["A) Trendwende", "B) Rücksetzer im laufenden Trend", "C) Long-Einstieg", "D) Short-Auslösung"], "answer": "B"},
    {"question": "Was ist ein Pullback?", "options": ["A) Trendstart", "B) Rücklauf nach Ausbruch", "C) Verlustzone", "D) Hebelverlust"], "answer": "B"}
], "answer": "B"},
    ...
]

quiz_hard = [
    {"question": "Was ist ein Drawdown?", "options": ["A) Maximaler Gewinn", "B) Rückgang vom Hoch zum Tief", "C) Hebelverlust", "D) Seitwärtsphase"], "answer": "B"},
    {"question": "Was ist eine Margin Call?", "options": ["A) Gewinnmitteilung", "B) Aufforderung, Kapital nachzuzahlen", "C) Verkaufsorder", "D) Tradingstil"], "answer": "B"},
    {"question": "Was ist ein Risk:Reward Ratio von 1:3?", "options": ["A) Weniger Gewinn als Risiko", "B) Mehr Risiko als Gewinn", "C) Für 1 Risiko-Einheit 3 Gewinn-Einheiten", "D) Verhältnis irrelevant"], "answer": "C"},
    {"question": "Was ist Positionsgrößen-Management?", "options": ["A) Anzahl offener Tabs", "B) Regelung des Einsatzes pro Trade", "C) Brokerauswahl", "D) Zeitmanagement"], "answer": "B"},
    {"question": "Was ist psychologischer Widerstand?", "options": ["A) Nicht messbar", "B) Kursgrenze auf runde Zahlen wie 10000", "C) Brokerlimit", "D) Hebelwirkung"], "answer": "B"},
    {"question": "Was ist Trading-Psychologie?", "options": ["A) Börsenstimmung", "B) Emotionale Kontrolle beim Handeln", "C) Analystenmeinung", "D) Kaufdruck"], "answer": "B"},
    {"question": "Was bedeutet Overtrading?", "options": ["A) Zu viele Trades ohne Strategie", "B) News-Handel", "C) Depotanalyse", "D) Verlustbegrenzung"], "answer": "A"},
    {"question": "Was bedeutet Undertrading?", "options": ["A) Zu wenig Aktivität trotz Chancen", "B) Hebelverkauf", "C) Long ohne Stop", "D) Strategiewechsel"], "answer": "A"},
    {"question": "Was ist ein Equity Curve?", "options": ["A) Gewinnkurve eines Portfolios", "B) Kurslinie", "C) Volumenkurve", "D) Breakout-Muster"], "answer": "A"},
    {"question": "Was ist Drawdown-Limit?", "options": ["A) Technischer Indikator", "B) Maximal erlaubter Kapitalverlust", "C) Broker-Feature", "D) Risikozone"], "answer": "B"},
    {"question": "Was ist ein Trading-Journal?", "options": ["A) Zeitung", "B) Aufzeichnung aller Trades zur Analyse", "C) Kalender", "D) Broker-Dashboard"], "answer": "B"},
    {"question": "Was ist ein Backtest?", "options": ["A) Chartanalyse live", "B) Rückwirkende Strategietestung", "C) Broker-Test", "D) Margin-Test"], "answer": "B"},
    {"question": "Was ist Alpha im Trading?", "options": ["A) Handelsplattform", "B) Überschussrendite gegenüber Benchmark", "C) Short-Strategie", "D) Marginwert"], "answer": "B"},
    {"question": "Was ist Beta im Trading?", "options": ["A) Risikoindikator im Verhältnis zum Markt", "B) Marginwert", "C) Volumenwert", "D) Trendkurve"], "answer": "A"},
    {"question": "Was ist eine Stop-Loss-Kaskade?", "options": ["A) Mehrere Stop-Loss-Levels nacheinander", "B) Gewinnstrategie", "C) Volumenkurve", "D) Brokerstruktur"], "answer": "A"},
    {"question": "Was ist ein Swing-High?", "options": ["A) Langfristiger Hochpunkt", "B) Zwischenhoch in Bewegung", "C) Tief", "D) Konsolidierung"], "answer": "B"},
    {"question": "Was ist ein Dead Cat Bounce?", "options": ["A) Bullischer Ausbruch", "B) Kurze Gegenbewegung nach starkem Abverkauf", "C) Chartfehler", "D) Gewinnphase"], "answer": "B"},
    {"question": "Was ist ein Gap Fill?", "options": ["A) Ausfüllen von Kurslücken", "B) Chartmuster", "C) Verlust", "D) Indikator"], "answer": "A"},
    {"question": "Was bedeutet \"Risk per Trade\"?", "options": ["A) Gewinnziel", "B) Kapitalrisiko je Trade", "C) Ordergröße", "D) Brokerkosten"], "answer": "B"},
    {"question": "Was ist ein Portfolio Drawdown?", "options": ["A) Gewinn", "B) Gesamtverlust bezogen auf das Depot", "C) Ein Trade", "D) Margin-Handel"], "answer": "B"}
], "answer": "B"},
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
