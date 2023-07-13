import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'word' in message.content.lower():
        # Marca a mensagem do autor
        response = f'{message.author.mention}, você mencionou a palavra!'

        # Lista de URLs de GIFs
        gif_urls = [
            '',
            '',
            '',
            # Adicione mais URLs de GIFs aqui
        ]

        # Seleciona aleatoriamente um GIF da lista
        gif_url = random.choice(gif_urls)

        # Envia o GIF para o canal
        await message.channel.send(response)
        await message.channel.send(gif_url)

    await bot.process_commands(message)

bot.run('bot_token')
