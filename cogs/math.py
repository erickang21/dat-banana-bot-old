import discord
import sys
import os
import io
import math
import operator
from discord.ext import commands


class math:

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def add(ctx, self, num: int, num2: int):
        '''It...ADDS? Yea. Usage: *add [no.1] [no.2]'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *add [no.1] [no.2]")
        else:
            await ctx.send(num + num2)
        
        
@commands.command()
async def subtract(ctx, self, num: int, num2: int):
        '''It...SUBTRACTS? Yea. Usage: *subtract [no.1] [no.2]'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *subtract [no.1] [no.2]")
        else:
            await ctx.send(num - num2)
        
        
@commands.command()
async def multiply (ctx, self, num: int, num2: int):
        '''It...MULTIPLIES? Yea. Usage: *multiply [no.1] [no.2]'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *multiply [no.1] [no.2]")
        else:
            await ctx.send(num * num2)
        
        
@commands.command()
async def divide (ctx, self, num: int, num2: int):
        '''It...DIVIDES? Yea. Usage: *divide [no.1] [no.2]'''
        if num is None:
            await ctx.send("Aren't you stupid enough? Usage: *divide [no.1] [no.2]")
        else:
            await ctx.send(num / num2)


def setup(bot): 
    bot.add_cog(math(bot))            
