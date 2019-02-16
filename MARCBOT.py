#this was made by Marcgamer_carbajo#0310

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

Bot = commands.Bot(command_prefix='*')

@Bot.event
async def on_ready():
    print(' I am ready')
    print('I AM RUNNING ON ' + Bot.user.name)
    print('With the ID ' + Bot.user.id)


@Bot.command(pass_context=True)
async def ping(ctx):
    await Bot.say('Pong!')

@Bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await Bot.say('The user name is: {}'.format(user.name))
    await Bot.say('The user ID is: {}'.format(user.id))
    await Bot.say('The user status is: {}'.format(user.status))
    await Bot.say('The user highest role is: {}'.format(user.top_role))
    await Bot.say('The user joined at: {}'.format(user.joined_at))

@Bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await Bot.say('CYA, {}. YA LOSER!'.format(user.name))
    await Bot.kick(user)

@Bot.command(pass_context=True)
async def help(ctx):
    await Bot.say('Commands:')
    await Bot.say('info')
    await Bot.say('kick')
    await Bot.say('ping')
    await Bot.say('Creator')
    await Bot.say('More command comming soon')
    

@Bot.command(pass_context=True)
async def Creator(ctx):
    await Bot.say('I was created BY: @Marcgamer_carbajo#0310')

Bot.run('NTQ2MzE3ODgzOTQxMDYwNjA4.D0mgZw.zOtYnsShVc8CQUmfeKnm5tEQU9Y')
