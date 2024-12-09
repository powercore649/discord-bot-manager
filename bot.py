import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté comme {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTI5NDAwODA3ODI2OTgwODY2MQ.Gg1OzN.boi69zUuLMZYkny_pjuZ0_j0-G5OjIRCeammLw")
