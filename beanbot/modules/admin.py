import discord
import beanbot.config.bot_config as bot_config
from discord.ext import commands


class AdminCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx: commands.Context):
        await ctx.send("This test has BEAN a success")

    @commands.command(name='mute')
    @commands.has_role('Adminiman')
    async def mute_user(self, ctx: commands.Context, member: discord.Member):
        muted_role = get_role(ctx.guild.roles, bot_config.muted_role)
        await member.add_roles(muted_role)
        await ctx.send('Get Beaned kid')


def setup(bot: commands.Bot):
    bot.add_cog(AdminCog(bot))


def get_role(role_list, role_name):
    for role in role_list:
        if role.name == role_name:
            return role
