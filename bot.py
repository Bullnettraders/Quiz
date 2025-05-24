import discord
from discord.ext import commands
import os
import random
import asyncio

from fragenpool import quiz_easy, quiz_medium, quiz_hard

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

user_scores = {}
active_questions = {}
quiz_category_name = "Quiz"

@bot.event
async def on_ready():
    print(f"✅ Bot ist eingeloggt als {bot.user}")
    for guild in bot.guilds:
        ranking_channel = discord.utils.get(guild.text_channels, name="ranking")
        if ranking_channel is None:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=True),
                guild.me: discord.PermissionOverwrite(send_messages=True, read_messages=True)
            }
            await guild.create_text_channel("ranking", overwrites=overwrites)

@bot.command()
async def start(ctx):
    await ctx.send(
        f"👋 Hallo {ctx.author.mention}! Willkommen beim **Trading-Quiz**! 🎓\n"
        "Starte mit `!quiz leicht`, `!quiz mittel`, `!quiz schwer` – du bekommst dann einen privaten Quiz-Channel."
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
        await ctx.send("Verwende: `!quiz leicht`, `!quiz mittel`, `!quiz schwer`.")
        return

    guild = ctx.guild
    category = discord.utils.get(guild.categories, name=quiz_category_name)
    if not category:
        category = await guild.create_category(quiz_category_name)

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    quiz_channel = await guild.create_text_channel(
        f"quiz-{ctx.author.name.lower()}",
        overwrites=overwrites,
        category=category
    )

    fragen, punkte = difficulty_map[stufe]
    frage = random.choice(fragen)
    active_questions[ctx.author.id] = (frage, punkte, quiz_channel.id)

    frage_text = f"🎯 **{frage['question']}**\n" + "\n".join(frage['options'])
    await quiz_channel.send(f"{ctx.author.mention}, hier ist deine Frage:\n\n{frage_text}\n\nAntworte mit **A**, **B**, **C**, **D** oder dem Antworttext.")

@bot.command()
async def leicht(ctx):
    await quiz(ctx, "leicht")

@bot.command()
async def mittel(ctx):
    await quiz(ctx, "mittel")

@bot.command()
async def schwer(ctx):
    await quiz(ctx, "schwer")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    if message.author.id in active_questions:
        frage, punkte, channel_id = active_questions[message.author.id]
        if message.channel.id != channel_id:
            return

        user_input = message.content.strip().upper()
        correct_letter = frage["answer"].upper()
        correct_option = next(opt for opt in frage["options"] if opt.startswith(correct_letter))
        correct_text = correct_option[3:].strip().upper()

        if user_input == correct_letter or user_input == correct_text:
            user_scores[message.author.id] = user_scores.get(message.author.id, 0) + punkte
            await message.channel.send(f"✅ Richtig, {message.author.mention}! +{punkte} Punkte!")
        else:
            await message.channel.send(f"❌ Falsch. Richtige Antwort: **{correct_letter} – {correct_text.title()}**")

        del active_questions[message.author.id]
        await message.channel.send("🧹 Channel wird in 10 Sekunden gelöscht...")
        await asyncio.sleep(10)
        await message.channel.delete()

        # Ranking aktualisieren
        guild = message.guild
        ranking_channel = discord.utils.get(guild.text_channels, name="ranking")
        if ranking_channel:
            try:
                ranking_sorted = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
                lines = ["🏆 **Top 10 Spieler:**"]
                for i, (user_id, score) in enumerate(ranking_sorted[:10], 1):
                    try:
                        user = await bot.fetch_user(user_id)
                        username = user.name
                    except:
                        username = f"User-ID {user_id}"
                    lines.append(f"{i}. {username} – {score} Punkte")
                await ranking_channel.purge(limit=10)
                await ranking_channel.send("\n".join(lines))
            except Exception as e:
                print(f"Ranking-Fehler: {e}")

# Bot starten
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ DISCORD_TOKEN fehlt! Bitte in .env eintragen.")
    else:
        bot.run(TOKEN)
