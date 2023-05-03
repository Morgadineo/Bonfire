import discord
import pyodbc
from settings import *

# Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

dados_de_conexao = (
    "Driver={SQLite3 ODBC Driver};"
    "Server=localhost;"
    "Database=Textos.db"
)

conexao = pyodbc.connect(dados_de_conexao)
cursor = conexao.cursor()

@client.event
async def on_ready():
    print("O SOL BRILHA EM MEIO O ABISMO!")

@client.event
async def on_disconnect():
    print("O abismo...venceu...")
    cursor.close()
    conexao.close()


# Message events
@client.event
async def on_message(message):
    content = message.content.capitalize()
    channel = message.channel
    author = message.author

    # Random generator
    if content == 'Gerar frase':
        await channel.send(get_random_dsquote())
    elif content == 'Gerar nome':
        await channel.send(get_random_name())
    elif content == 'Gerar guilda':
        await channel.send(get_random_covenant())
    elif content == 'Gerar memoria':
        await channel.send(get_random_memory())
    elif content == 'Gerar personagem':
        await channel.send(get_random_npc())

    elif content == 'Ficha':
        await channel.send(show_person())
    elif content == 'Gerar inimigo':
        await channel.send(get_random_enemy())
    elif content == 'Gerar arma':
        await channel.send(get_random_common_weapon())
    elif content == 'Limpar chat':
        await message.channel.purge(limit=50)


# Deleted message event
@client.event
async def on_message_delete(message):
    channel = message.channel
    author = message.author.mention
    await channel.send(f"{author}, {get_random_deletedquote()}")


# Bot run and token
# keep_alive()

if __name__ == '__main__':
    client.run('MTAwODIyMzk5MzQ5NDUxOTg2OA.GVrLaU.yY5Cps3UXsLZYGUZoAfYhqmnrjcquPWp-o1MfU')
