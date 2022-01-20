import discord
from discord.ext import commands
from config import PREFIX

class cmd(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def help(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url

        await ctx.message.delete()
        embed=discord.Embed(title="List", description=f"Don't forget to type `{PREFIX}`", color=0xD22024)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="`[>] fun`:", value='**"FUN"** commands', inline=True)
        embed.add_field(name="`[>] nsfw`:", value='**NSFW** commands', inline=True)
        embed.add_field(name="`[>] haxor`:", value='**HAXOR** commands', inline=True)
        embed.set_image(url="https://media2.giphy.com/media/MM0Jrc8BHKx3y/giphy.gif?cid=ecf05e47yw3wa4kn3eoi7aknziii46yc7rukw80geqf5hbek&rid=giphy.gif&ct=g")
        embed.set_footer(text="This message will be deleted in 15 seconds")
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]HELP was executed")

        
    @commands.command()
    async def fun(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        
        await ctx.message.delete()
        embed=discord.Embed(title="Fun", description=f"Don't forget to use {PREFIX}", color=0xe55757)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="`[>] gp`", value="Ghostping/delete msg after sending it", inline=True)
        embed.add_field(name="`[>] spam <amount>`", value="Spam any message you like 100 times", inline=True)
        embed.add_field(name="`[>] ascii <input>`", value="Send any word in ascii", inline=True)
        embed.add_field(name="`[>] server`", value="Server Information", inline=True)
        embed.add_field(name="`[>] iplookup <input>`", value="Checks data of choosen ip", inline=True)
        embed.set_footer(text="This message will be deleted in 15 seconds")
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]FUN was executed")

    @commands.command()
    async def nsfw(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        
        await ctx.message.delete()
        embed=discord.Embed(title="NSFW", description=f"Don't forget to use {PREFIX}\nrule34 isn't working in this version", color=0xa72ffc)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="`[>] Rule34 <input> / Rule34 <input> <amount>`", value="Rule34 of your choosen \"input\"")
        embed.add_field(name="`[>] minus8`", value="Minus8 dance", inline=True)
        embed.set_footer(text="This message will be deleted in 15 seconds")
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]NSFW was executed")
    
    @commands.command()
    async def haxor(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url
        
        await ctx.message.delete()
        embed=discord.Embed(title="Haxor", description=f"Don't forget to use {PREFIX}")
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="`[>] createchannel <input>`", value="Create's channel", inline=True)
        embed.add_field(name="`[>] nuke <input>`", value="Delete's all channels and make's new one's", inline=True)
        embed.set_footer(text="This message will be deleted in 15 seconds")
        await ctx.send(embed=embed, delete_after=15.0)

        print(f"[>]FUN was executed")

def setup(bot):
    bot.add_cog(cmd(bot))