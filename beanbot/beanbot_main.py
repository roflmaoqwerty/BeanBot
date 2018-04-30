import discord
from discord.ext import commands
import beanbot.config.bot_config as bot_config


def get_prefix(bot, message):
    prefixes = ['.', '$']
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, description="test bot")


extensions = ['modules.admin']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load Extension {extension}.')


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    bot_config

bot.run(bot_config.token, bot=True, reconnect=True)