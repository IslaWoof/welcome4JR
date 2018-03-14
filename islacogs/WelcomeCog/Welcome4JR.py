import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio


class Welcome:
    """Welcomes new members to the server in the default channel"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        emojis = []
        numbers = [1, 2, 3, 4, 5]
        for n in numbers:
            emojis.append('{}⃣'.format(str(n)))
        message = f'Hello {member.mention}! Welcome to the Official Team Liquid Mobile discord server. Please choose one of these options.\n1. I want to join a Team Liquid Clan.\n2. I am already in a Team Liquid clan, I need to register as an official player.\n3. I need a specific Team Liquid Mobile Discord role.\n4. I have a questions.\n5. Just visiting.'
        channel_id = '389100476630695946'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        for e in emojis:
            await self.bot.add_reaction(m, e)
            await asyncio.sleep(0.5)
        try:
            r, u = await self.bot.wait_for_reaction(emoji=emojis, user=member, message=m, timeout=99999999999999999999)
        except TypeError:
            await self.bot.clear_reactions(m)
        else:
            await self.bot.clear_reactions(m)
            if r.emoji == emojis[0]:
                c = self.bot.get_channel('389100476630695946')
                await self.bot.send_message(c, 'Thanks for your interest! Here is the Google Form to Liquid:\nhttps://docs.google.com/forms/d/e/1FAIpQLSdl65dcN6ROYdtMKCfR6C8_b6T-shOJTsmi0UY7juEAUutY1Q/viewform?usp=sf_link')
                await self.bot.send_message(m, f'Sent Google Form in DM to {member.mention}.')
            elif r.emoji == emojis[1]:
                c = self.bot.get_channel('389100476630695946')
                MMod = '<@&325720548527308800>'
                await self.bot.send_message(c, f'{member.mention} please send a photo of your profile and let me summon a {MMod}.')
            elif r.emoji == emojis[2]:
                c = self.bot.get_channel('389100476630695946')
                s = await self.bot.send_message(c, 'I\'m going to ask to you a couple of questions, please just answer in chat.')
                q1 = await self.bot.send_message(c, '1) What\'s your In Game Name?')
                a1 = await self.bot.wait_for_message(author=member)
                q2 = await self.bot.send_message(c, '2) What game do you need a Discord role?')
                a2 = await self.bot.wait_for_message(author=member)
                q3 = await self.bot.send_message(c, '3) What clan are you in?')
                a3 = await self.bot.wait_for_message(author=member)
                q4 = await self.bot.send_message(c, '4) What is your current rank?')
                a4 = await self.bot.wait_for_message(author=member)
                q5 = await self.bot.send_message(c, '5) Anything else you like to add?')
                a5 = await self.bot.wait_for_message(author=member)
                em = discord.Embed()
                em.title = f'Informations for "{member.name}"'
                em.description = f'**__In-Game Name:__**\n{a1.content}\n\n**__Game:__**\n{a2.content}\n\n**__Clan:__**\n{a3.content}\n\n**__Current rank:__**\n{a4.content}\n\n**__Notes:__**\n{a5.content}'
                messages = (q1, q2, q3, q4, q5, a1, a2, a3, a4, a5, s)
                await self.bot.delete_messages(messages)
                await self.bot.send_message(c, embed = em)
            elif r.emoji == emojis[3]:
                c = self.bot.get_channel('389100476630695946')
                ModMail = '<@422438974859116544>'
                await self.bot.send_message(c, f'{member.mention} if you have any question regarding Liquid send a message in private to {ModMail}.')
            elif r.emoji == emojis[4]:
                server = self.bot.get_server('301578535175323658')
                c = self.bot.get_channel('389100476630695946')
                v = discord.utils.get(server.roles, name='Visitors')
                s = await self.bot.send_message(c, 'I\'m going to ask to you a couple of questions, please just answer in chat.')
                q1 = await self.bot.send_message(c, '1) What games do you play?')
                a1 = await self.bot.wait_for_message(author = member)
                q2 = await self.bot.send_message(c, '2) What\'s your In Game Name?')
                a2 = await self.bot.wait_for_message(author = member)
                q3 = await self.bot.send_message(c, '3) What team are you on?')
                a3 = await self.bot.wait_for_message(author = member)
                q4 = await self.bot.send_message(c, '4) Anything else you would like to add?')
                a4 = await self.bot.wait_for_message(author = member)
                em = discord.Embed()
                em.title = f'Informations for "{member.name}"'
                em.description = f'**__Games:__**\n{a1.content}\n\n**__In-Game Name:__**\n{a2.content}\n\n**__Team:__**\n{a3.content}\n\n**__Notes:__**\n{a4.content}'
                messages = (q1, q2, q3, q4, a1, a2, a3, a4, s)
                await self.bot.delete_messages(messages)
                await self.bot.send_message(c, embed = em)
                await self.bot.add_roles(member, v)
                await self.bot.send_message(c, f'Added Visitors Role to {member.mention}')
def setup(bot):
    bot.add_cog(Welcome(bot))
    

# 1) What games do you play?
# 2) In Game Name
# 3) What team are you on?
# 4) Anything else you would like to add?


# 1) In Game Name
# 2) What game do you need a Discord role?
# 3) What clan are you in?
# 4) What is your current rank?
# 5) Anything else you like to add?


# t = discord.utils.get(member.server.roles, name='Trusted')
# await self.bot.add_roles(member, t)
# await self.bot.edit_message(m, f'Added Trusted Role to {member.mention}, you can ask for a Role here.')
