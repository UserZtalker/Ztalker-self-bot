import discord
from config import PREFIX
from discord.ext import commands

class cmd(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send("""```md
1. fun:
>    Fun commands
2. nsfw:
>    NSFW commands
3. hacker:
>    "Hacker" commands```""", delete_after=10.0)
        print(f"[>]HELP was executed")

        
    @commands.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""```md
1. <ip "input">:
>    ~ {PREFIX}ip "STRING"(Something like: 177.188.49.12)
2. <cd "input">:
>    ~ {PREFIX}cd "STRING"(Something like: Your mom)
3. <spam "input">:
>    ~ {PREFIX}spam "STRING"(Something like: Hah get spammed bitches!)```""", delete_after=10.0)

        print(f"[>]FUN was executed")

    @commands.command()
    async def nsfw(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"""```md
1. <r34 "input">:
>    ~ {PREFIX}r34 "STRING"(Something like: Trap)```""", delete_after=10.0)
        
        print(f"[>]NSFW was executed")
    
    @commands.command()
    async def hacker(self, ctx):
        await ctx.message.delete()
        
        await ctx.send(f"""```md
1. <raid "input">:
>    ~ {PREFIX}raid "STRING"(Something like: GET RAIDED)
2. <cch "input">:
>    ~ {PREFIX}cch "STRING"(Something like: General)```""", delete_after=10.0)


        print(f"[>]FUN was executed")

def setup(bot):
    bot.add_cog(cmd(bot))
