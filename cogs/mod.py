import discord
import sys
import os
import io
from discord.ext import commands


class mod:

    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """Escort your DM to someone thru the bot. Usage: *dm [tag person] [msg]"""
        try:
            await user.send(msg)
            await ctx.send("SuccESS! Your DM has made it! :white_check_mark: ")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: *dm [tag person] [msg]")
            
            
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member):
            await ctx.channel.send(f"Be gone {user.name}! Oh, and close the door on the way out :door:.")
            await user.kick()
            
            
    @bot.command()
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, user: discord.Member):
            await ctx.channel.send(f"The ban hammer has fallen. And it has struck {user.name}.")
            await user.ban()
            
            
def setup(bot): 
    bot.add_cog(mod(bot))
