import asyncio
import crasync
import json

async def main():
    client = crasync.Client()
    clan = await client.get_clan('29GLUPJ')
    print(clan)
    print(clan.description)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

