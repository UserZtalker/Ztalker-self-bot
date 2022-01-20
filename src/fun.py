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
        
        embed = discord.Embed(title="IP LOOKUP")
        embed.add_field(name="IP:", value=ip, inline=True)
        embed.add_field(name="City:", value=details.city, inline=True)
        embed.add_field(name="Location:", value=details.city, inline=True)
        embed.add_field(name="Country name:", value=details.country_name, inline=True)
        embed.add_field(name="Host name:", value=details.hostname, inline=True)

        await ctx.send(embed=embed)
        print(f"[>]IPLOOKUP was executed ({ip})")


    @commands.command()
    async def embed(self, ctx, *, text):
        await ctx.message.delete()

        embed = discord.Embed(title="", description=text)
        await ctx.send(embed=embed)

        print(f"[>]EMBED was executed")

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

        embed = discord.Embed(title = f"{ctx.guild.name}", color = discord.Colour.blue())
        embed.add_field(name = '~ ID', value = f"{ctx.guild.id}", inline = False)
        embed.add_field(name = '~ Created on', value = ctx.guild.created_at.strftime("%b %d %Y"), inline = False)
        embed.add_field(name = '~ Owner', value = f"{ctx.guild.owner}", inline = False)
        embed.add_field(name = '~ Members', value = f'{ctx.guild.member_count} Members', inline = False)
        embed.add_field(name = '~ Region', value = f'{ctx.guild.region}', inline = False)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=embed, delete_after=15.0)

        print(f'[>]SERVER was executed')

        
def setup(bot):
    bot.add_cog(cmd(bot))