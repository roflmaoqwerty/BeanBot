import discord
import beanbot.config.bot_config as bot_config
from pony.orm import *
from beanbot.db.dbschema import *
import beanbot.db.objects.gamerequests as requests
from discord.ext import commands

db_name = 'lfg.sqlite'


class LFGCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lfg')
    async def lfg(self, ctx: commands.Context, duration):
        if requests.user_exists(ctx.author.id):
            await ctx.send("User exists")
        else:
            await ctx.send("User does not exist. adding user")
            requests.add_user(ctx.author.id, ctx.author.name)


def setup(bot: commands.Bot):
    bot.add_cog(LFGCog(bot))
