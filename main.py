# coding: UTF-8
import discord
import settings
import commands

client = discord.Client()

APP_ENV = settings.APP_ENV
APP_ENV_PROD = 'prod'
APP_ENV_DEV = 'dev'
BOT_TOKEN = settings.BOT_TOKEN
# 開発検証用チャンネルのID
TEST_CHANNEL_ID = 696641960047542333


def isLocal():
    return APP_ENV == APP_ENV_DEV


def isTestChannel(channel):
    return channel.id == TEST_CHANNEL_ID


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if isLocal() and not isTestChannel(message.channel):
        return
    if not isLocal() and isTestChannel(message.channel):
        return
    if message.content == '/neko':
        await commands.neko(message.channel)
    if message.content == '/members':
        await commands.members(message.guild.members, message.author)
    if message.content == '/roles':
        await commands.roles(message.guild.roles, message.author)

client.run(BOT_TOKEN)
