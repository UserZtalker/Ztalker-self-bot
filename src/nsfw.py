import discord, random, datetime
from config import PREFIX
from rule34Py import rule34Py
from discord.ext import commands

r34Py = rule34Py()
tm = datetime.datetime.now()

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['r34', 'R34', '34'])
    async def Rule34(self, ctx, text, amount=1):
        if amount==1:
            result_random = r34Py.random_post([text])

            await ctx.reply(f'```md\n<Rule34 ~ {PREFIX}{text} >```\n{result_random.image}')
            print(f"{tm}[>]Rule34 was executed")
        
        elif amount<20 and amount>1:
            i = 0

            while i<amount:
                result_random = r34Py.random_post([text])

                await ctx.reply(f'```md\n<Rule34 ~ {PREFIX}{i+1} >```\n{result_random.image}')
                i = i + 1

            print(f"{tm}[>]Rule34 was executed {amount} times")
        else:
            pass
        


    @commands.command(aliases=['m8', 'minus'])
    async def minus8(self, ctx):
        await ctx.message.delete()

        vids = [
            'https://i.imgur.com/19Zvw92.mp4', 
            'https://i.imgur.com/vgXgFsB.mp4',
            'https://i.imgur.com/j5NEpHa.gif'
            ]
        vids = random.choice(vids)
        await ctx.send(f"```md\n<Minus8> ~ Dance```\n{vids}")
        print("[>]Minus8 was executed")
        

def setup(bot):
    bot.add_cog(cmd(bot))