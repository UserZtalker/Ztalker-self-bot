from discord.ext import commands


class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, text):
        print(f"[-]ERROR something went wrong!({text})")


def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))