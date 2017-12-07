import discord
import sys
import os
import io
from discord.ext import commands


class utility:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def ping(self, ctx):
        """Websocket latency, delivered through premium ping pong."""
        em = discord.Embed(color=discord.Color(value=0x00ff00))
        em.title = "PoIIIIng! That took:"
        em.description = f'{bot.ws.latency * 1000:.4f} ms'
        await ctx.send(embed=em)
    
def setup(bot): 
    bot.add_cog(Utility(bot))
