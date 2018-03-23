import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio


class liquidwelcome:
    """Welcomes new members to the server in the default channel"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        c = self.bot.get_channel('389100476630695946')
        m = f'Hello {member.mention}! Welcome to the Official Team Liquid Mobile Discord server. We hope you have a good time here. Please add the role for the game you play (+ClashRoyale, +AoV, +BrawlStars). Please tag a moderator and DM Liquid mail if you have any questions.'
        await self.bot.send_message(c, m)
        m2 ='Hello and welcome to Team Liquid\'s Mobile empire. Please review our new member pamphlet @ https://bit.ly/2px9czy for an introduction to Team Liquid and information on our mobile teams. \n\nIf you are currently in the Team Liquid Mobile empire or you would like to join then please fill out our official member registration located @ https://goo.gl/6kGVPZ - \n\nIf you have any questions then please join one of our community chats or reach out to a Discord moderator'
        await self.bot.send_message(member, m2)
        
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)
