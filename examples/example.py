# Inside an async function

import crasync
import asyncio

async def main():
    async with crasync.Client() as client:
        profile = await client.get_profile('2CYUUCC8')

        print(profile)
        print(profile.current_trophies)

        await profile.update() # updating the info

        clan = await profile.get_clan() # get the players full clan info

        chests = profile.get_chests()

        print(clan)
        print(len(clan.members))

        await clan.update() # updating the info

        highest = await clan.members[0].get_profile()

        print(highest) # top player
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
