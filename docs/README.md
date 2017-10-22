# Welcome!

crasync is an **asynchronus** CR API wrapper for Python made to be both fully-featured and easy to use.

Run `pip3 install crasync` and `pip3 install aiohttp` in your console.

# Installing

Install it normally from PyPI with pip:
```elm
pip3 install crasync
```
Install `aiohttp` as well
```elm
pip3 install aiohttp
```

# Using the Wrapper

Since this is an asynchronus wrapper, the code has to be within an asynchronus function.

A short example to grab a member's name and his clan's tag, and the number of his clan members.

```py
import crasync
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

Look through the [API Reference](api-reference.md)!
