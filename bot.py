import discord
import os
import io
import textwrap
from contextlib import redirect_stdout
import traceback
from discord.ext import commands 
bot = commands.Bot(command_prefix='*',description="It's a something bot made by dat banana boi #1982.\n\nHelp Commands",owner_id=277981712989028353)


def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')
    
    
@bot.event
async def on_ready():
   print('Bot is online!') 
   
   
@bot.command()
async def readycheck(ctx):
    """I dare you to guess. I mean, like, to see if I'm working."""
    await ctx.send("You were wrong! Looks like I AM working!")
    
    
@bot.command()
async def ping(ctx):
    """Websocket latency, delivered through premium ping pong."""
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "PoIIIIng! That took:"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)
        
        
@bot.command()
async def say(ctx, *, message: str):
    '''Yea, yea. I'll say what you say.'''
    await ctx.message.delete()
    await ctx.send(message)        
        
        
@bot.command()
async def invite(ctx):
    """Lemme in your server, mate. From here."""
    await ctx.send("Allow me to join the hood: https://discordapp.com/oauth2/authorize?client_id=387706175770198023&scope=bot&permissions=8")        
        
        
@bot.command(pass_context=True, hidden=True, name='eval')
@commands.is_owner()
async def _eval(ctx, *, body: str):
        """Evaluates a code"""

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
   
   
