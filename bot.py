# coding: UTF-8
import discord
import settings

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is ready!')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(settings.BOT_TOKEN)
