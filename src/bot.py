import os
import logging
from datetime import datetime
from pytz import timezone

import discord
from discord import Client, Intents, Embed
from discord.ext import commands

from discord_slash import SlashCommand, SlashContext

TOKEN = os.getenv("DISCORD_TOKEN")

LOG = logging.getLogger('discordbot')
LOG.setLevel(logging.DEBUG)  # DEBUG
FMT = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
H = logging.StreamHandler()
H.setFormatter(FMT)
LOG.addHandler(H)

# https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
bot = commands.Bot(command_prefix="!", intents=Intents.default())
slash = SlashCommand(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")

@bot.command(name="bing")
async def bing(ctx):
    await ctx.send("bong")
    
@bot.command(name="nitro")
async def nitro(ctx):
    await ctx.send("Your subscriptions will automatically renew on Sep 22, 2021 and you'll be charged $9.99.")

@bot.command(name="day")
async def day(ctx):
    EST = timezone("US/Eastern")
    day = datetime.now(EST).strftime("%A")
    if day == "Wednesday":
        day += " my dudes"
    response = "It is " + day
    await ctx.send(response)

@bot.command()
async def add(ctx, a, b):
    # called as "!add arg1 arg2"
    await ctx.send(a + b)

# https://github.com/goverfl0w/discord-interactions
# test command, feel free to delete once we have a real slash command
@slash.slash(name="first")
async def first(ctx: SlashContext):
    embed = Embed(title="Embed slash")
    await ctx.send(content="get slashed")

if __name__ == "__main__":
    print("bot starting")
    bot.run(TOKEN)


