import pyfiglet, ipinfo
import discord, time
from discord.ext import commands
from config import PASSTOKEN
handler = ipinfo.getHandler(PASSTOKEN)

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ip', 'iplook'])
    async def iplookup(self, ctx, ip):
        await ctx.message.delete()
        details = handler.getDetails(ip)

        author = ctx.message.author
        pfp = author.avatar_url
        embed = discord.Embed(title=ip)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="City", value=details.city, inline=True)
        embed.add_field(name="Location", value=details.loc, inline=True)
        embed.add_field(name="Country", value=details.country_name, inline=True)
        embed.add_field(name="HostName", value=details.hostname, inline=True)
        await ctx.send(embed=embed)

        print(f"[>]IPLOOKUP was executed ({ip})")

    @commands.command()
    async def embed(self, ctx, *, text):
        embed = discord.Embed(title="Message", description=text)
        await ctx.send(embed=embed)

        print("[>]EMBED was executed")

    @commands.command()
    async def code(self, ctx, *, text):
        await ctx.message.delete()

        await ctx.send(f"```\n{text}```")

        print(f"[>]CODE was executed")

    @commands.command()
    async def spam(self, ctx, amount=50, text="SPAM"):
        i = 0
        
        await ctx.message.delete()
        try:
            if int(amount)>500:
                   await ctx.send("Sorry 500 is max", delete_after=5.0, mention_author=False)
            elif int(amount)<100 and int(amount)>1:

                while i < int(amount):
                    time.sleep(0.3)
                    await ctx.send(text)
                    i = i + 1

                if text == "SPAM":
                    print(f"[>]SPAM was executed with default settings")
                else:
                    print(f"[>]SPAM was executed {amount} times.")
        except ValueError:
            await ctx.send("Something went wrong!", delete_after=5.0)

    @commands.command()
    async def ascii(self, ctx, *, args):
        await ctx.message.delete()
        text = pyfiglet.figlet_format(args)
        await ctx.send(f'``` {text}```')

        print(f"[>] ASCII was executed")

    @commands.command(aliases=['gp', 'ghost'])
    async def ghostping(self, ctx, text):
        await ctx.message.delete()

        if text == False:
            print(f"[~]GhostPing You must ping someone")
            
        print(f'[>]GhostPING was executed')

    @commands.command()
    async def server(self, ctx):
        await ctx.message.delete()
        author = ctx.message.author
        pfp = author.avatar_url

        embed = discord.Embed(title='ServerInfo', color=0xcc3030)
        embed.set_author(name=author, icon_url=pfp)
        embed.add_field(name="ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="OWNER", value=ctx.guild.owner, inline=True)
        embed.add_field(name="MEMBERS", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="REGION", value=ctx.guild.region, inline=True)
        embed.add_field(name="Created on:", value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
        await ctx.send(embed=embed)

        print(f'[>]SERVER was executed')

        
def setup(bot):
    bot.add_cog(cmd(bot))
