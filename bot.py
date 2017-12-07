import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import aiohttp
import pip
import random
import textwrap
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix='*',description="It's a something bot made by dat banana boi #1982.\n\nHelp Commands",owner_id=277981712989028353)
bot.load_extension("cogs.math")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.utility")


def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')
    
    
@bot.event
async def on_ready():
   print('Bot is online!') 

def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
    if id in devs:
        return True
    return False
        
        
@bot.event
async def on_guild_join(guild):
    print("Banana has joined a new guild: {}".format(guild.name))
    
@bot.event
async def on_ready():
        """Shows bot's status"""
        print("Logged in as:")
        print("Name : {}".format(bot.user.name))
        print("ID : {}".format(bot.user.id))
        print("----------------")
        server = len(bot.guilds)
        users = sum(1 for _ in bot.get_all_members())
        while 1==1:
            await bot.change_presence(game=discord.Game(name='with {} servers'.format(server)))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='with {} users'.format(users)))
            await asyncio.sleep(10)                         
            await bot.change_presence(game=discord.Game(name='PREFIX = *'))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='*help | *invite'))
            await asyncio.sleep(10)
            await bot.change_presence(game=discord.Game(name='Banana bot!'))
            await asyncio.sleep(25)
            
                        
@bot.command()
async def readycheck(ctx):
    """I dare you to guess. I mean, like, to see if I'm working."""
    await ctx.send("You were wrong! Looks like I AM working!")

    
@bot.command(name='presence')
@commands.is_owner()
async def _set(ctx, Type=None,*,thing=None):
  """Tell me what I'm doing and I'll show it."""
  if Type is None:
    await ctx.send('Butter do it right. Usage: `*presence [game/stream] [message]`')
  else:
    if Type.lower() == 'stream':
      await bot.change_presence(game=discord.game(name=thing,type=1,url='https://www.twitch.tv/a'),status='online')
      await ctx.send(f'Set presence to. `Streaming {thing}`')
    elif Type.lower() == 'game':
      await bot.change_presence(game=discord.game(name=thing))
      await ctx.send(f'Set presence to `Playing {thing}`')
    elif Type.lower() == 'clear':
      await bot.change_presence(game=None)
      await ctx.send('Cleared Presence')
    else:
      await ctx.send('Usage: `.presence [game/stream] [message]`')
    
  
@bot.command()
async def textface(ctx, Type):
    """Get that lenny, tableflip or shrug face in here!"""
    if Type is None:
        await ctx.send('That is NOT a textface! Usage: *textface [lenny/tableflip/shrug]')
    else:
        if Type.lower() == 'lenny':
          await ctx.send('( ° ʖ °)')
        elif Type.lower() == 'tableflip':
          await ctx.send('(ノಠ益ಠ)ノ彡┻━┻')
        elif Type.lower() == 'shrug':
          await ctx.send('¯\_(ツ)_/¯')
        else:
          await ctx.send('That is NOT a textface! Usage: *textface [lenny/tableflip/shrug]')
        
        
@bot.command()
async def say(ctx, *, message: str):
    '''Yea, yea. I'll say what you say.'''
    await ctx.message.delete()
    await ctx.send(message)        
        
        
@bot.command()
async def invite(ctx):
    """Lemme in your server, mate. From here."""
    await ctx.send("Allow me to join the hood: https://discordapp.com/oauth2/authorize?client_id=387706175770198023&scope=bot&permissions=8")        
        
        
@bot.command()
async def discord(ctx):
    """Join our Discord server!"""
    await ctx.send("Your turn to enter the hood. https://discord.gg/wvkVknA")
        
        
@bot.command(hidden=True, name='eval')
async def _eval(ctx, *, body: str):
    
    if not dev_check(ctx.author.id):
        return

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        try:
            await ctx.message.add_reaction('\u2705')
        except:
            pass

        if ret is None:
            if value:
                await ctx.send(f'```py\n{value}\n```')
        else:
            await ctx.send(f'```py\n{value}{ret}\n```')    
   

if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
   
   
