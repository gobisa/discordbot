from datetime import datetime

def registerCommands(bot):
    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command(name="bing")
    async def bing(ctx):
        await ctx.send("bong")

    @bot.command(name="day")
    async def day(ctx):
        response = "It is " + datetime.today().strftime("%A")
        await ctx.send(response)

    @bot.command()
    async def add(ctx, a, b):
        # called as "!add arg1 arg2"
        await ctx.send(a + b)
