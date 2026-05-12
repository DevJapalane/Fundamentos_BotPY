# cogs/help.py
import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        """Menu de ajuda do bot"""
        embed = discord.Embed(
            title='📋 Comandos do YLLWSMKs BOT',
            description='Lista de todos os comandos disponíveis:',
            color=discord.Color.blue()
        )

        embed.add_field(
            name='📊 `!xp [@usuário]`',
            value='Mostra seu XP e nível (ou de outro usuário)',
            inline=False
        )

        embed.add_field(
            name='🏆 `!rank`',
            value='Mostra o top 10 do servidor',
            inline=False
        )

        embed.add_field(
            name='🏓 `!ping`',
            value='Mostra a latência do bot',
            inline=False
        )

        embed.add_field(
            name='👋 `!ola`',
            value='O bot te cumprimenta... ou não 💀',
            inline=False
        )

        embed.add_field(
            name='❓ `!help`',
            value='Mostra este menu',
            inline=False
        )

        embed.set_footer(
            text=f'Solicitado por {ctx.author.name}',
            icon_url=ctx.author.avatar.url if ctx.author.avatar else None
        )
        embed.set_thumbnail(
            url=self.bot.user.avatar.url if self.bot.user.avatar else None
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))