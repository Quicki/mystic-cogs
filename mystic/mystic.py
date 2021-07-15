import discord
import requests
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from redbot.core import Config, commands, checks


class MyCog(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")