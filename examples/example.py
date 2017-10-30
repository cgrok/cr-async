# Inside an async function

import crasync
import asyncio

async def main():
    async with crasync.Client() as client:
        profile = await client.get_profile('2CYUUCC8')

        print(profile)
        print('Current Trophies: ' + str(profile.current_trophies))
        chest_cycle = ', '.join([profile.get_chest(x) for x in range(10)])
        print(chest_cycle) # next 9 chests.

        await profile.update() # updating the info

        try:
            clan = await profile.get_clan() # get the players full clan info
        except ValueError:
            print('No Clan')
        else:
            print('Clan: '+ str(clan))
            print('Members: ' + str(len(clan.members)))
            await clan.update() # updating the info
            highest = await clan.members[0].get_profile() # top player
            print('Clan Top Player: '+ str(highest))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
