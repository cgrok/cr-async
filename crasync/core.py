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
from .errors import RequestError, NotFoundError, ServerError

class Client:

    '''Represents an async client connection to cr-api.com

    Attributes
    ----------
    session:
        The aiohttp ClientSession to be used for requests
    '''

    BASE = 'http://api.cr-api.com'

    def __init__(self, session=None, timeout=10):
        self.timeout = timeout
        self.session = session or aiohttp.ClientSession()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        self.session.close()

    def close(self):
        self.session.close()

    async def request(self, url):
        async with self.session.get(url, timeout=self.timeout) as resp:
            try:
                data = await resp.json()
            except (asyncio.TimeoutError, aiohttp.ClientResponseError):
                raise ServerError(resp, {})

            # Request was successful 
            if 300 > resp.status >= 200:
                return data

            # Tag not found
            if resp.status == 404:
                raise NotFoundError(resp, data)

            # Something wrong with the api servers :(
            if resp.status > 500:
                raise ServerError(resp, data)

            # Everything else
            else:
                raise RequestError(resp, data)


    async def get_profile(self, *tags):
        '''Get a profile object using tag(s)'''
        url = '{0.BASE}/profile/{1}'.format(self, ','.join(tags))

        data = await self.request(url)
                
        if isinstance(data, list):
            return [Profile(self, c) for c in data]
        else:
            return Profile(self, data)

    get_profiles = get_profile

    async def get_clan(self, *tags):
        '''Get a clan object using tag(s)'''
        url = '{0.BASE}/clan/{1}'.format(self, ','.join(tags))

        data = await self.request(url)
                
        if isinstance(data, list):
            return [Clan(self, c) for c in data]
        else:
            return Clan(self, data)

    get_clans = get_clan

    async def get_constants(self):
        '''Get clash royale constants.'''
        url = self.BASE + '/constants'

        data = await self.request(url)

        return Constants(self, data)

    async def get_top_clans(self):
        '''Get a list of top clans, info is only brief, 
        call get_clan() on each of the ClanInfo objects 
        to get full clan info'''
        url = self.BASE + '/top/clans'

        data = await self.request(url)

        return [ClanInfo(self, c) for c in data.get('clans')]