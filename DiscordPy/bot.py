import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import random

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

# Comando de conexão: !ping
@bot.command()
async def ping(ctx):
    RespostasPing = [
        f'🏓 Pong! Latência: {round(bot.latency * 1000)}ms',
        f'🤖 Bip Bop... checando internet... o ping está {round(bot.latency * 1000)}ms',
        f'☝️🤓 o ping na verdade tá {round(bot.latency * 1000)}ms '
    ]
    await ctx.send(random.choice(RespostasPing))

# Comando: !ola
@bot.command()
async def ola(ctx):
    RespostasOla = [
        f'Não vem de conversinha, {ctx.author.mention}! 💀',
        f'Salve {ctx.author.mention} 😎',
        f'Foda-se...?🖕 {ctx.author.mention} ',
        f'Bão? {ctx.author.mention}',
        f'qvs? {ctx.author.mention}'
    ]
    await ctx.send(random.choice(RespostasOla))



async def main():
    async with bot:
        await bot.load_extension('cogs.help')  # carrega o help.py
        await bot.load_extension('cogs.xp') # carrega o xp
        await bot.start(TOKEN)

asyncio.run(main())