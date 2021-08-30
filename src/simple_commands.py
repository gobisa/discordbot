from datetime import datetime
from discord.ext import commands

class SimpleCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(ctx):
        await ctx.send("pong")

    @commands.command(name="bing")
    async def bing(ctx):
        await ctx.send("bong")

    @commands.command(name="day")
    async def day(ctx):
        response = "It is " + datetime.today().strftime("%A")
        await ctx.send(response)

    @commands.command()
    async def add(ctx, a, b):
        # called as "!add arg1 arg2"
        await ctx.send(a + b)

def setup(bot):
    bot.add_cog(SimpleCommands(bot))