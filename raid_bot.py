# Raid Bot

This is the main bot application code for the Raid Bot.

import discord
from discord.ext import commands

# Initialize bot with command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def raid(ctx):
    await ctx.send('Raid started!')

# To run the bot:
# Insert your token here
bot.run('YOUR_BOT_TOKEN')