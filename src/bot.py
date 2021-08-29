import os
import logging

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

LOG = logging.getLogger('discordbot')
LOG.setLevel(logging.DEBUG)  # DEBUG
FMT = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
H = logging.StreamHandler()
H.setFormatter(FMT)
LOG.addHandler(H)

# https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("pong")

@bot.command(name="bing")
async def bing(ctx):
    await ctx.send("bong")

@bot.command()
async def add(ctx, a, b):
    # called as "!add arg1 arg2"
    await ctx.send(a + b)

if __name__ == "__main__":
    print("bot starting")
    bot.run(TOKEN)


