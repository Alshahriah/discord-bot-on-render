from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send("The sum is " + str(a + b))

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send("The product is " + str(a * b))

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello there!")

    @commands.command()
    async def bye(self, ctx):
        await ctx.send("Bye bye!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

async def setup(bot):
    await bot.add_cog(Basic(bot))