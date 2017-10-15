import aiohttp
import asyncio


class Base:
    '''
    Base class for models. Only thing that 
    needs to be added is the from_data function
    '''

    def __init__(self, client, data):
        self.client = client
        self.tag = data.get('tag')
        self.from_data(data)
        endpoint = type(self).__name__.lower()
        self.url = f'{client.BASE}/{endpoint}/{self.tag}'
       
    async def from_data(self):
        pass

    async def update(self):

        async with self.client.session.get(self.url) as resp:
            data = await resp.json()

        self.from_data(data)

        return self


class Clan(Base):
    '''Represents a clan'''

    def from_data(self, data):
        pass

class Profile(Base):
    '''Represents a player profile.
    Includes a clan maybe? (requires a seperate request tho)
    '''

    def from_data(self, data):
        pass


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
            data = await resp.json()

        return Profile(self, data)


    async def get_clan(self, tag):
        '''Get a clan object using a tag'''

        url = f'{self.BASE}/clan/{tag}'

        async with self.session.get(url) as resp:
            data = await resp.json()

        return Clan(self, data)

