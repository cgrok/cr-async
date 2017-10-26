# Welcome!

CR-Async is an **asynchronus** CR API wrapper for Python made to be both fully-featured, object oriented and easy to use.

# Installing

Install it normally from PyPI with pip:
```
pip3 install crasync
```

# Using the Wrapper

Since this is an asynchronus wrapper, the code has to be within an asynchronus function.

A short example to grab a member's name and his clan's tag, and the number of his clan members.

```python
import crasync
import aiohttp
import asyncio

async def main():
    client = crasync.Client()
    profile = await client.get_profile('2P0LYQ')
    print(profile.name)
    print(profile.clan_tag)
    clan = await profile.get_clan()
    print(len(clan.members))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

# What are more things I can do?

Go through the API reference on the side.
