# coding: UTF-8
import discord
import settings

client = discord.Client()

APP_ENV = settings.APP_ENV
APP_ENV_PROD = 'prod'
APP_ENV_DEV = 'dev'
BOT_TOKEN = settings.BOT_TOKEN
# 開発検証用チャンネルのID
TEST_CHANNEL_ID = 696641960047542333


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if filterMessage(message):
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')


def filterMessage(message):
    return message.author.bot or (APP_ENV == APP_ENV_PROD and message.channel.id == TEST_CHANNEL_ID) or (APP_ENV == APP_ENV_DEV and message.channel.id != TEST_CHANNEL_ID)


client.run(BOT_TOKEN)
