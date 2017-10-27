# Cycle
?> Represents the chest cycle of a clash royale player.

#### Attributes
> **`position`** - The number of chests the player has opened    
**Returns:** int

> **`super_magical`** - The position of the player's next super magical chest    
**Returns:** int

> **`legendary`** - The position of the player's next legendary chest    
**Returns:** int

> **`epic`** - The position of the player's next epic chest    
**Returns:** int

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