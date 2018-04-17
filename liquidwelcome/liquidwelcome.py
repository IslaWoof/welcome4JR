import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice
from random import randint
import asyncio

class liquidwelcome:
    """Welcomes new members to Team Liquid Mobile"""

    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        ser = self.bot.get_server('301578535175323658')
        #nv = discord.utils.get(ser.roles, name = 'Not Verified')
        cr = discord.utils.get(ser.roles, name = 'Clash Royale')
        bs = discord.utils.get(ser.roles, name = 'Brawl Stars')
        aov = discord.utils.get(ser.roles, name = 'Arena of Valor')
        #cj = self.bot.get_channel('432157348371628042')
        #mj = '**{}** has joined the Server! <:liquid3:425779102927290388>\n```{} members in the Server.```'.format(member.name, ser.member_count)
        #await self.bot.send_message(cj, mj)
        await self.bot.add_roles(member, cr)
        await self.bot.add_roles(member, aov)
        await self.bot.add_roles(member, bs)                        
        #await self.bot.add_roles(member, nv)
        #c = self.bot.get_channel('432154053825265684')
        #m = '**Hello {}! Welcome to the Official Team Liquid Mobile Discord server.**\n\n<:tl:429889965397245964>Please look in <#429719437763936256> and add the role for the game you play.\n<:tl:429889965397245964>You must be a member in one of our official teams to have a member role.\n<:tl:429889965397245964>Check out our various channels for info on prizes, events, teams, and much more.\n<:tl:429889965397245964>Tag an online moderator or DM Liquid Mail if you have any questions.\n***__By clicking on the "✅" reaction you will get access to the Server and you declare that you have read the Server rules.__***'.format(member.mention)
        #emojis = ['✅']
        #ms = await self.bot.send_message(c, m)
        #for e in emojis:
        #    await self.bot.add_reaction(ms, e)
        #try:
        #    r, u = await self.bot.wait_for_reaction(emoji = emojis, user = member, message = ms, timeout = 600)
        #except TypeError:
        #    await self.bot.delete_message(ms) 
        #    await self.bot.remove_roles(member, nv)
        #    await self.bot.add_roles(member, dumb)
        #    await self.bot.remove_roles(member, nv)
        #else:
        #    if r.emoji == emojis[0]:
        #        await self.bot.delete_message(ms) 
        #        await self.bot.remove_roles(member, nv)
        
    async def on_member_remove(self, member):
        c = self.bot.get_channel('432157348371628042')
        s = self.bot.get_server('301578535175323658')
        m = '**{}** has left the Server, bye bye... <:QooBeeConsole:422749739591794688>\n```{} members left in the Server.```'.format(member.name, s.member_count)
        await self.bot.send_message(c, m)
        
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

    @commands.command(pass_context = True, no_pm = True) 
    async def addacademy(self, ctx, user : discord.Member):
        """Adds Academy role to user."""
        ser = self.bot.get_server('301578535175323658')
        ac = discord.utils.get(ser.roles, id = '430495770014253056')
        s = discord.utils.get(ser.roles, id = '432550860229443594')
        ma = discord.utils.get(ser.roles, id = '430493433669353483')
        u = ctx.message.author
        if s in u.roles:
            await self.bot.add_roles(user, ma)
            await self.bot.say('Added "{}" role to {}.'.format(ma.name, user.mention))
        else:
            await self.bot.say('You don\'t have permissions to use this command.')
        
    @commands.command(pass_context = True, no_pm = True) 
    async def removeacademy(self, ctx, user : discord.Member):
        """Removes Academy role from user."""
        ser = self.bot.get_server('301578535175323658')
        ac = discord.utils.get(ser.roles, id = '430495770014253056')
        s = discord.utils.get(ser.roles, id = '432550860229443594')
        ma = discord.utils.get(ser.roles, id = '430493433669353483')
        u = ctx.message.author
        if s in u.roles:
            await self.bot.remove_roles(user, ma)
            await self.bot.say('Removed "{}" role from {}.'.format(ma.name, user.mention))
        else:
            await self.bot.say('You don\'t have permissions to use this command.')
        
        
    @commands.command(pass_context=True)
    async def remindme(self, ctx,  quantity : int, time_unit : str, *, text : str):
        """Sends you <text> when the time is up
        Accepts: minutes, hours, days, weeks, month
        Example:
        [p]remindme 3 days Have sushi with Asu and JennJenn"""
        time_unit = time_unit.lower()
        author = ctx.message.author
        s = ""
        if time_unit.endswith("s"):
            time_unit = time_unit[:-1]
            s = "s"
        if not time_unit in self.units:
            await self.bot.say("Invalid time unit. Choose minutes/hours/days/weeks/month")
            return
        if quantity < 1:
            await self.bot.say("Quantity must not be 0 or negative.")
            return
        if len(text) > 1960:
            await self.bot.say("Text is too long.")
            return
        seconds = self.units[time_unit] * quantity
        future = int(time.time()+seconds)
        self.reminders.append({"ID" : author.id, "FUTURE" : future, "TEXT" : text})
        logger.info("{} ({}) set a reminder.".format(author.name, author.id))
        await self.bot.say("I will remind you that in {} {}.".format(str(quantity), time_unit + s))
        fileIO("data/remindme/reminders.json", "save", self.reminders)
        
        
def setup(bot):
    n = liquidwelcome(bot)
    bot.add_cog(n)

    
    
