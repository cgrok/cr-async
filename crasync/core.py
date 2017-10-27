import aiohttp
import asyncio
from .models import Profile, Clan


class Client:

    '''Represents an async client connection to cr-api.com

    Attributes
    ----------
    session:
        The aiohttp ClientSession to be used for requests
    '''

    BASE = 'http://api.cr-api.com'

    def __init__(self, session=None):
        self.session = session or aiohttp.ClientSession()


    async def get_profile(self, tag):
        '''Get a profile object using a tag.'''

        url = f'{self.BASE}/profile/{tag}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                print('API is down. Please be patient.')
                return None

        return Profile(self, data)


    async def get_clan(self, tag):
        '''Get a clan object using a tag'''

        url = f'{self.BASE}/clan/{tag}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                print('API is down. Please be patient.')
                return None

        return Clan(self, data)

    async def get_constants(self):
        '''Get a profile object using a tag.'''

        url = f'{self.BASE}/constants'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                print('API is down. Please be patient.')
                return None

        return Constants(self, data)

