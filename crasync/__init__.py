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

from .core import Client

############
# METADATA #
############

__version__ = 'v2.0.0'
__title__ = 'crasync'
__license__ = 'MIT'
__author__ = 'verixx'
__github__ = 'https://github.com/grokkers/cr-async'


##########################################################
# EVERYTHING BELOW ARE SHORTCUTS USING TEMPORARY CLIENTS # 
##########################################################

async def get_profile(*tags):
    async with Client() as client:
        return await client.get_profile(*tags)

get_profiles = get_profile

async def get_clan(*tags):
    async with Client() as client:
        return await client.get_clan(*tags)

get_clans = get_clan

async def get_constants():
    async with Client() as client:
        return await client.get_constants()

async def get_top_clans():
    async with Client as client:
        return await client.get_top_clans()