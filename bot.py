import discord
from discord.ext import commands
import os
import random
import asyncio
import json

from fragenpool import quiz_easy, quiz_medium, quiz_hard

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

SCORE_FILE = "scores.json"
user_scores = {}
active_questions = {}
quiz_category_name = "Quiz"

def load_scores():
    global user_scores
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            user_scores = json.load(f)
    else:
        user_scores = {}

def save_scores():
    with open(SCORE_FILE, "w") as f:
        json.dump(user_scores, f)

@bot.event
async def on_ready():
    print(f"✅ Bot ist eingeloggt als {bot.user}")
    load_scores()
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
    await ctx.message.delete()
    msg = await ctx.send(
        f"👋 Hallo {ctx.author.mention}! Willkommen beim **Trading-Quiz**! 🎓\n"
        "Starte mit `!quiz leicht`, `!quiz mittel`, `!quiz schwer` – du bekommst dann einen privaten Quiz-Channel."
    )
    await asyncio.sleep(10)
    await msg.delete()

@bot.command()
async def quiz(ctx, stufe: str):
    await ctx.message.delete()
    difficulty_map = {
        "leicht": (quiz_easy, 1),
        "mittel": (quiz_medium, 2),
        "schwer": (quiz_hard, 3)
    }

    stufe = stufe.lower()
    if stufe not in difficulty_map:
        msg = await ctx.send("Verwende: `!quiz leicht`, `!quiz mittel`, `!quiz schwer`.")
        await asyncio.sleep(10)
        await msg.delete()
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
    frage_text = f"🎯 **{frage['question']}**
" + "
".join(frage['options'])
    await quiz_channel.send(
        f"{ctx.author.mention}, hier ist deine Frage:

{frage_text}

Antworte mit **A**, **B**, **C**, **D** oder dem Antworttext."
    )
    msg = await ctx.send(f"📬 Dein privater Quiz-Channel wurde erstellt, {ctx.author.mention}!")
    await asyncio.sleep(10)
    await msg.delete()

@bot.command(aliases=['quizleicht'])
async def leicht(ctx):
    await ctx.message.delete()
    await quiz(ctx, "leicht")

@bot.command(aliases=['quizmittel'])
async def mittel(ctx):
    await ctx.message.delete()
    await quiz(ctx, "mittel")

@bot.command(aliases=['quizschwer'])
async def schwer(ctx):
    await ctx.message.delete()
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
            user_scores[str(message.author.id)] = user_scores.get(str(message.author.id), 0) + punkte
            user_scores[str(message.author.id)] = user_scores.get(str(message.author.id), 0) + punkte
            await message.channel.send(f"✅ Richtig, {message.author.mention}! +{punkte} Punkte!")
            await asyncio.sleep(3)
            await message.delete()
        else:
            await message.channel.send(f"❌ Falsch. Richtige Antwort: **{correct_letter} – {correct_text.title()}**")
            await asyncio.sleep(3)
            await message.delete()

        del active_questions[message.author.id]
        await message.channel.send("🧹 Channel wird in 10 Sekunden gelöscht...")
        await asyncio.sleep(10)
        await message.channel.delete()
        save_scores()

        # Ranking aktualisieren
        guild = message.guild
        ranking_channel = discord.utils.get(guild.text_channels, name="ranking")
        if ranking_channel:
            try:
                ranking_sorted = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
                lines = ["🏆 **Top 10 Spieler:**"]
                for i, (user_id, score) in enumerate(ranking_sorted[:10], 1):
                    try:
                        user = await bot.fetch_user(int(user_id))
                        username = user.name
                    except:
                        username = f"User-ID {user_id}"
                    lines.append(f"{i}. {username} – {score} Punkte")
                await ranking_channel.purge(limit=10)
                await ranking_channel.send("\n".join(lines))
            except Exception as e:
                await message.channel.send(f"⚠️ Fehler beim Aktualisieren des Rankings: {e}")

@bot.command()
async def stats(ctx):
    user_id = str(ctx.author.id)
    punkte = user_scores.get(user_id, 0)
    msg = await ctx.send(f"📊 {ctx.author.mention}, du hast aktuell **{punkte} Punkte**.")
    await asyncio.sleep(10)
    await msg.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx, member: discord.Member):
    user_id = str(member.id)
    if user_id in user_scores:
        user_scores[user_id] = 0
        save_scores()
        await ctx.send(f"🔁 Punktestand von {member.mention} wurde zurückgesetzt.")
    else:
        await ctx.send(f"ℹ️ {member.mention} hat noch keine Punkte.")

# Bot starten
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ DISCORD_TOKEN fehlt! Stelle sicher, dass die Umgebungsvariable auf Railway gesetzt ist.")
    else:
        bot.run(TOKEN)
