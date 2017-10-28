'''
MIT License

Copyright (c) 2017 grokkers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import aiohttp
import asyncio
from .models import Profile, Clan, Constants, ClanInfo

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

        if ', ' in tags:
            raise SyntaxError("Read the docs please")

        tags = ','.join(tags)
        url = f'{self.BASE}/profile/{tags}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')
                
        if 'error' in data:
            raise NameError('Invalid Tag')

        if isinstance(data, list):
            return [Profile(self, c) for c in data]
        else:
            return Profile(self, data)

    async def get_clan(self, *tags):
        '''Get a clan object using tag(s)'''

        if ', ' in tags: #hahaha
            raise SyntaxError("Read the docs please")

        tags = ','.join(tags)
        url = f'{self.BASE}/clan/{tags}'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')
                
        if 'error' in data:
            raise NameError('Invalid Tag')

        if isinstance(data, list):
            return [Clan(self, c) for c in data]
        else:
            return Clan(self, data)

    get_clans = get_clan

    async def get_constants(self):
        '''Get clash royale constants.'''

        url = f'{self.BASE}/constants'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')

        return Constants(self, data)

    async def get_top_clans(self):
        '''Get a list of top clans, info is only brief, 
        call get_clan() on each of the ClanInfo objects 
        to get full clan info'''

        url = f'{self.BASE}/top/clans'

        async with self.session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
            else:
                raise ConnectionError(f'API not responding: {resp.status}')

        return [ClanInfo(self, c) for c in data.get('clans')]