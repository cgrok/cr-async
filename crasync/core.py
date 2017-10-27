import aiohttp
import asyncio
from .models import Profile, Profiles, Clan, Clans, Constants


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


    async def get_profile(self, *, tags):
        '''Get a profile object using tag(s).'''
        tags = tags.split(',')

        if len(tags) == 1:
            url = f'{self.BASE}/profile/{tags[0]}'

            async with self.session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                else:
                    print('API is down. Please be patient.')
                    return None

            return Profile(self, data)

        taglist = ''
        i = 0
        for tag in tags:
            i += 1
            taglist += tag[1:]
            if i != len(tags):
                taglist += ','

        url = f'{self.BASE}/profile/{taglist}'
        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')
        return Profiles(self, data)

    async def get_clans(self, *, tags):
        '''Get a clan object using tag(s)'''

        tags = ','.join(tags)

        url = f'{self.BASE}/clan/{tags}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')

        if isinstance(data, list):
            return [Clan(self, c) for c in data]
        else:
            return Clan(self, c)

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

