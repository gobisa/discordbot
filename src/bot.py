import os
import logging

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

command_classes = [
    "simple_commands",
    ]

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

if __name__ == "__main__":
    print("bot starting")
    for extension in command_classes:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)
