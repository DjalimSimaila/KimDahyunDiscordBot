import discord
import getgif
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('KIM DAHYUN'):
        await message.channel.send(getGif.getGifFromTenor("kim dahyun"))
client.run('---------------------------------')
