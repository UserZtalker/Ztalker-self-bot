import discord, os
from discord.ext import commands
from config import TOKEN, PREFIX

bot = commands.Bot(command_prefix=PREFIX, self_bot=True, help_command=None)
bot.remove_command(help)

@bot.event
async def on_ready():
    os.system('cls')
    print("""
/ ___|  ___| |/ _|
\___ \ / _ \ | |_ 
 ___) |  __/ |  _|
|____/ \___|_|_|  """)
    print(f"~ TOKEN: {TOKEN}")
    print(f"~ PREFIX: {PREFIX}")
    print("Executed commands:")


#- Help
for filename in os.listdir('./src'):
    if filename.endswith('.py'):
        bot.load_extension(f'src.{filename[:-3]}')

bot.run(TOKEN, bot=False)
