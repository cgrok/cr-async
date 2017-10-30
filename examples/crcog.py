import discord
from discord.ext import commands
import crasync


class ClashCog:
    '''
    Example discord.py cog for a discord bot.
    '''
    def __init__(self, bot):
        self.bot = bot
        session = getattr(bot, 'session', None)
        self.cr = crasync.Client(session) # The client.

    def check_valid_tag(self, tag):
        return all(x in 'PYLQGRJCUV0289' for x in tag)

    def cdir(self, obj):
        return [x for x in dir(obj) if not x.startswith('_')]

    @commands.command()
    async def profile(self, ctx, tag):
        '''Example command for use inside a discord bot cog.'''
        if not self.check_valid_tag(tag):
            return await ctx.send('Invalid tag!')

        profile = await self.cr.get_profile(tag)

        em = discord.Embed(color=0x00FFFFF)
        em.set_author(name=str(profile), icon_url=profile.clan_badge_url)
        em.set_thumbnail(url=profile.arena.badge_url)

        # Example of adding data. (Bad)
        for attr in self.cdir(profile):
            value = getattr(profile, attr) 
            if not callable(val):
                em.add_field(
                    name=attr.replace('_').title(), 
                    value=str(value)
                    )

        await ctx.send(embed=em)


def setup(bot):
    cog = ClashCog(bot)
    bot.add_cog(cog)