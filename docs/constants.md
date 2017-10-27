# Constants
?> Represents the constants from cr-api.

#### Attributes
> **`clan`** - Information about clan roles and types.    
**Returns:** [Alliance](alliance.md)

> **`arena`** - Information about all arenas and leagues in the game.    
**Returns:** list [[Arena](arena.md), [Arena](arena.md), [Arena](arena.md)... [Arena](arena.md)]

> **`badges`** - Information about the different clan badges.    
**Returns:** dict {'16000000': 'Flame\_01', '16000001': 'Flame\_02',... '16000179': 'A\_Char\_Bomb\_02'}

> **`chest_cycle`** - Information about the full length chest cycle.    
**Returns:** list [Silver, Silver, Silver, Gold... Silver]

> **country_codes** - Information about the various countries in the game.    
**Returns:** list [[Country](country.md), [Country](country.md), [Country](country.md)... [Country](country.md)]

> **rarities** - Detailed and technical information about each rarity in the game.    
**Returns:** list [[Rarity](rarity.md), [Rarity](rarity.md), [Rarity](rarity.md)... [Rarity](rarity.md)]

> **rarities** - Information about each card in the game.    
**Returns:** list [[CardInfo](cardinfo.md), [CardInfo](cardinfo.md), [CardInfo](cardinfo.md)... [CardInfo](cardinfo.md)]

To get your next chest in cycle, look below:    
```python
import crasync
import aiohttp
import asyncio

async def main():
    client = crasync.Client()
    profile = await client.get_profile('2P0LYQ')
    constants = await client.get_constants()
    index = profile.chest_cycle.position % len(constants.chest_cycle)
    print(constants.chest_cycle[index])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
This will print your next chest in cycle.    
This is related to [player's chest cycle](cycle.md) as well!