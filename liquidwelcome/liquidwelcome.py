import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        c = self.bot.get_channel('389100476630695946')
        m = 'Hello {}! Welcome to the Official Team Liquid Mobile Discord server. \nPlease look in <#429719437763936256> and add the role for the game you play.\nYou must be a member in one of our official teams to have a member role.\nYou must be an elder, co-leader, or leader in one of our official teams to have a citizen role. \nCheck out our various channels for info on prizes, events, teams, and much more. \nTag an online moderator or DM Liquid Mail if you have any questions.'.format(member.mention)
        await self.bot.send_message(c, m)
    #   m2 ='Hello and welcome to Team Liquid\'s Mobile empire. Please review our new member pamphlet @ https://bit.ly/2px9czy for an introduction to Team Liquid and information on our mobile teams. \n\nIf you are currently in the Team Liquid Mobile empire or you would like to join then please fill out our official member registration located @ https://goo.gl/6kGVPZ - \n\nIf you have any questions then please join one of our community chats or reach out to a Discord moderator'
    #   await self.bot.send_message(member, m2)
        
    #async def on_member_remove(self, member):
    #    c = self.bot.get_channel('414094090070786058')
    #    s = self.bot.get_server('301578535175323658')
    #    m = '**{}** has just left the Server, bye bye<:QooBeeConsole:422749739591794688>... {} members left in the Server'.format(member.name, s.member_count)
    #    await self.bot.send_message(c, m)
        
    @commands.command(pass_context = True, no_pm = True)
    async def liquid(self, ctx):
        """Team Liquid Mobile Information"""
        server = ctx.message.server
        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        em = discord.Embed(colour=discord.Colour(value=colour))
        em.title = "Team Liquid Information"
        em.description = "Welcome to Team Liquid Mobile!"
        if server.icon_url:
            em.set_author(name=server.name, url=server.icon_url)
            em.set_thumbnail(url=server.icon_url)
        em.add_field(name="__GUIDE__", value="**Here is a brief guide to our server to get you started:**\n\n[Team Liquid Mobile New Member Pamphlet](https://bit.ly/2px9czy)\n[Team Liquid Mobile New Member Registration](https://goo.gl/6kGVPZ)\n\n[Team Liquid Mobile Academy Team Pamphlet](https://bit.ly/2uk38PI)\n[Team Liquid Mobile Academy Team Registration](https://bit.ly/2G7YTbA)")
        em.set_footer(text="Thanks for joining Liquid")
        await self.bot.say(embed=em)
        
    @commands.command(pass_context=True, no_pm=True)
    async def who(self, ctx):
        """Find out who is stupid!"""
        channel_id = ctx.message.channel.id
        owner = ctx.message.author
        message = 'Who is stupid?'
        m = await self.bot.send_message(self.bot.get_channel(channel_id), message)
        ms = await self.bot.wait_for_message(check = lambda x : x.author == ctx.message.author)
        IslaNub = '199436790581559296'
        saka = '323543378509824002'
        isla = '<@199436790581559296>'
        if ctx.message.author.id == IslaNub:
            await self.bot.say(f'Oh, my Master! You\'re the brightest person I\'ve ever seen! You definitely are right! {ms.content} really is stupid!')
        elif ctx.message.author.id == saka:
            await self.bot.say(f'Awww saka, since Isla has faith in you I\'m pretty sure you\'re right, {ms.content} is pretty much stupid!')
        elif ms.content == isla:
            await self.bot.say('Idk')
        else:
            await self.bot.say('Are you sure? (yes/no)')
            answer1 = ('yes')
            answer2 = ('no')
            msg = await self.bot.wait_for_message(author=owner)
            if msg.content.lower().strip() in answer1:
                if ms.content == 'I':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'Indeed, you are! Btw it\'s "me", not "I"...')
                elif ms.content == 'You':
                    await self.bot.send_message(self.bot.get_channel(channel_id), 'I am smart enough to understand you tried to troll me... Believe me, the stupid here is you, not me!')
                else:
                    await self.bot.send_message(self.bot.get_channel(channel_id), f'Hmm perhaps, I\'m not sure if {ms.content} is stupid, but I\'m sure YOU are!')
            elif msg.content.lower().strip() in answer2:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'Nice! You\'re right, because you\'re stupid!')
            else:
                await self.bot.send_message(self.bot.get_channel(channel_id), 'What don\'t you understand of "yes/no"??? Look how stupid...')

    @commands.command(pass_context = True, no_pm = True)
    async def msping(self, ctx):
        await self.bot.say(f'Pong! ({self.bot.ws.latency * 1000:.0f} ms)')

def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)

    