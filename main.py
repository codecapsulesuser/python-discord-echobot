import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #check if message isn't from us
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello! I'm an echobot, give it a try.")
    else:
        await message.channel.send(message.content)

client.run(os.getenv('TOKEN'))