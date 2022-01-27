import discord
from discord.ext import commands

class cmd(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title='Help', color=0xcc3030)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="- fun", value='Fun commands', inline=True)
        embed.add_field(name="- nsfw", value='nsfw commands', inline=True)
        embed.add_field(name="- hacker", value='"Hacker" commands', inline=True)
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]HELP was executed")

        
    @commands.command()
    async def fun(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title='Fun', color=0x11d84d)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="- ip <input>", value='Checks information of given IP', inline=True)
        embed.add_field(name="- embed <text>", value='Send\'s given string(text) in embed', inline=True)
        embed.add_field(name="- cd <text>", value='Send\'s given string(text) in codeblock', inline=True)
        embed.add_field(name="- spam <text>", value='spam\'s given text. If no text is set the command will be executed with "spam" set as a message', inline=True)
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]FUN was executed")

    @commands.command()
    async def nsfw(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title='NSFW', color=0xea09c5)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="- r34 <input>", value='Classic nsfw command', inline=True)
        await ctx.send(embed=embed, delete_after=15.0)
        
        print(f"[>]NSFW was executed")
    
    @commands.command()
    async def haxor(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title='Help', color=0x070707)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="- raid <input>", value='If string(input) isn\'t given this command will be executed anyways', inline=True)
        embed.add_field(name="- cch", value='Create\'s channel with your string(input) if input isn\'t given this command will be executed anyways', inline=True)
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]FUN was executed")

def setup(bot):
    bot.add_cog(cmd(bot))
