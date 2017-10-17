import asyncio
import crasync
import json

async def main():
    client = crasync.Client()
    profile = await client.get_profile('CVLQ2GV8')
    print(json.dumps(profile.raw_data, indent=4))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

