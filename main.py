import discord
from discord.ext import commands
import botToken

description = 'test bot'

bot = commands.Bot(command_prefix='$', description= description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def test(ctx):
    await ctx.send('test successful')


bot.run(botToken.token)