import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot logado como {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('----------------------------')

# Comando de teste: !ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong! Latência: {round(bot.latency * 1000)}ms')

# Comando: !ola
@bot.command()
async def ola(ctx):
    await ctx.send(f'Não vem de conversinha, {ctx.author.mention}! 💀')


async def main():
    async with bot:
        await bot.load_extension('cogs.help')  # carrega o help.py
        await bot.start(TOKEN)

asyncio.run(main())