import aiohttp
import asyncio
from .models import Profile, Clan, Constants


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


    async def get_profile(self, *tags):
        '''Get a profile object using tag(s)'''

        tags = ','.join(tags)

        url = f'{self.BASE}/profile/{tags}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')
                
        if "error" in data:
            return None

        if isinstance(data, list):
            return [Profile(self, c) for c in data]
        else:
            return Profile(self, data)

    async def get_clan(self, *tags):
        '''Get a clan object using tag(s)'''

        tags = ','.join(tags)

        url = f'{self.BASE}/clan/{tags}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')
                
        if "error" in data:
            return None

        if isinstance(data, list):
            return [Clan(self, c) for c in data]
        else:
            return Clan(self, data)

    get_clans = get_clan

    async def get_constants(self):
        '''Get a profile object using a tag.'''

        url = f'{self.BASE}/constants'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')

        return Constants(self, data)

