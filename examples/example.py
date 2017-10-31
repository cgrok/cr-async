# Inside an async function

import crasync
import asyncio
import time

profiles = []

async def main(loop):
    client = crasync.Client()

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

    constants = await client.get_constants()
    print(constants.cards['knight'].name) # Card constants.

    client.close() # you gotta do this if you finish with it

    #####################
    # Temporary clients #
    #####################

    profile = await crasync.get_profile('8UUC9QYG')
    print(profile)
    clan = await profile.get_clan()
    print(clan)

    # (Less efficient) 
    # In a larger application like a discord bot, 
    # its good to have a persistant client

    print('--------------\n\n')

    # Getting full profiles for each member of the clan.

    tasks = []
    for member in clan.members:
        fut = loop.create_task(get_profile_task(member))
        tasks.append(fut)

    t1 = time.time()
    done, pending = await asyncio.wait(tasks)
    t2 = time.time()

    print(t2-t1)


async def get_profile_task(member):
    p = await member.get_profile()
    print(p)
    profiles.append(p)



loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
