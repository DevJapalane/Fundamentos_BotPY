# cogs/xp.py
import discord
from discord.ext import commands
import sqlite3
import random
import time

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def xp_para_proximo_nivel(nivel):
    """XP necessário para subir do nível atual para o próximo"""
    return 5 * (nivel ** 2) + 50 * nivel + 100

def calcular_nivel(xp_total):
    """Calcula o nível atual baseado no XP total"""
    nivel = 0
    while xp_total >= xp_para_proximo_nivel(nivel):
        xp_total -= xp_para_proximo_nivel(nivel)
        nivel += 1
    return nivel

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}  # {user_id: timestamp}
        self.criar_tabela()

    def criar_tabela(self):
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                user_id    TEXT PRIMARY KEY,
                guild_id   TEXT,
                xp         INTEGER DEFAULT 0,
                nivel      INTEGER DEFAULT 0,
                mensagens  INTEGER DEFAULT 0
            )
        ''')
        db.commit()
        db.close()

    def get_usuario(self, user_id, guild_id):
        db = get_db()
        user = db.execute(
            'SELECT * FROM usuarios WHERE user_id = ? AND guild_id = ?',
            (str(user_id), str(guild_id))
        ).fetchone()

        if not user:
            db.execute(
                'INSERT INTO usuarios (user_id, guild_id, xp, nivel, mensagens) VALUES (?, ?, 0, 0, 0)',
                (str(user_id), str(guild_id))
            )
            db.commit()
            user = db.execute(
                'SELECT * FROM usuarios WHERE user_id = ? AND guild_id = ?',
                (str(user_id), str(guild_id))
            ).fetchone()

        db.close()
        return user

    def atualizar_xp(self, user_id, guild_id, xp_ganho):
        db = get_db()
        db.execute(
            '''UPDATE usuarios
               SET xp = xp + ?, mensagens = mensagens + 1
               WHERE user_id = ? AND guild_id = ?''',
            (xp_ganho, str(user_id), str(guild_id))
        )
        db.commit()

        user = db.execute(
            'SELECT * FROM usuarios WHERE user_id = ? AND guild_id = ?',
            (str(user_id), str(guild_id))
        ).fetchone()
        db.close()
        return user

    def atualizar_nivel(self, user_id, guild_id, novo_nivel):
        db = get_db()
        db.execute(
            'UPDATE usuarios SET nivel = ? WHERE user_id = ? AND guild_id = ?',
            (novo_nivel, str(user_id), str(guild_id))
        )
        db.commit()
        db.close()

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignora bots e DMs
        if message.author.bot or not message.guild:
            return

        user_id = message.author.id
        agora = time.time()

        # Cooldown de 60 segundos
        if user_id in self.cooldowns:
            if agora - self.cooldowns[user_id] < 60:
                return

        self.cooldowns[user_id] = agora

        # XP aleatório entre 15 e 25
        xp_ganho = random.randint(15, 25)

        usuario_antes = self.get_usuario(user_id, message.guild.id)
        nivel_antes = calcular_nivel(usuario_antes['xp'])

        usuario_depois = self.atualizar_xp(user_id, message.guild.id, xp_ganho)
        nivel_depois = calcular_nivel(usuario_depois['xp'])

        # Subiu de nível?
        if nivel_depois > nivel_antes:
            self.atualizar_nivel(user_id, message.guild.id, nivel_depois)

            embed = discord.Embed(
                title='⬆️ Level Up!',
                description=f'Parabéns {message.author.mention}! Você subiu para o **nível {nivel_depois}**! 🎉',
                color=discord.Color.gold()
            )
            embed.set_thumbnail(url=message.author.avatar.url if message.author.avatar else None)
            await message.channel.send(embed=embed)

    @commands.command()
    async def xp(self, ctx, membro: discord.Member = None):
        """Mostra o XP e nível de um usuário"""
        membro = membro or ctx.author
        usuario = self.get_usuario(membro.id, ctx.guild.id)

        xp_atual = usuario['xp']
        nivel = calcular_nivel(xp_atual)

        # Calcula XP dentro do nível atual
        xp_no_nivel = xp_atual
        for n in range(nivel):
            xp_no_nivel -= xp_para_proximo_nivel(n)

        xp_necessario = xp_para_proximo_nivel(nivel)
        progresso = int((xp_no_nivel / xp_necessario) * 10)
        barra = '█' * progresso + '░' * (10 - progresso)

        embed = discord.Embed(
            title=f'📊 XP de {membro.display_name}',
            color=discord.Color.blue()
        )
        embed.add_field(name='Nível', value=f'`{nivel}`', inline=True)
        embed.add_field(name='XP Total', value=f'`{xp_atual}`', inline=True)
        embed.add_field(
            name=f'Progresso para nível {nivel + 1}',
            value=f'`{barra}` {xp_no_nivel}/{xp_necessario} XP',
            inline=False
        )
        embed.set_thumbnail(url=membro.avatar.url if membro.avatar else None)
        await ctx.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        """Mostra o top 10 do servidor"""
        db = get_db()
        top = db.execute(
            '''SELECT * FROM usuarios WHERE guild_id = ?
               ORDER BY xp DESC LIMIT 10''',
            (str(ctx.guild.id),)
        ).fetchall()
        db.close()

        embed = discord.Embed(
            title=f'🏆 Top 10 — {ctx.guild.name}',
            color=discord.Color.gold()
        )

        medals = ['🥇', '🥈', '🥉']

        for i, row in enumerate(top):
            try:
                membro = await ctx.guild.fetch_member(int(row['user_id']))
                nome = membro.display_name
            except:
                nome = f'Usuário {row["user_id"]}'

            nivel = calcular_nivel(row['xp'])
            icone = medals[i] if i < 3 else f'`#{i+1}`'

            embed.add_field(
                name=f'{icone} {nome}',
                value=f'Nível {nivel} • {row["xp"]} XP',
                inline=False
            )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(XP(bot))