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

To get your next chest, look below:    
```python
import json
import crasync
import asyncio

async def main():
    client = crasync.Client()
    profile = await client.get_profile('2P0LYQ')
    async with ctx.session.get('http://api.cr-api.com/constants') as f:
        constants = await f.json()
    index = profile.chest_cycle.position % len(constants['chestCycle']['order'])
    print(constants['chestCycle'][index])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
This will print your next chest in cycle.