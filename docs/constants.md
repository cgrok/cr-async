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

> **`country_codes`** - Information about the various countries in the game.    
**Returns:** list [[Country](country.md), [Country](country.md), [Country](country.md)... [Country](country.md)]

> **`rarities`** - Detailed and technical information about each rarity in the game.    
**Returns:** list [[Rarity](rarity.md), [Rarity](rarity.md), [Rarity](rarity.md)... [Rarity](rarity.md)]

> **`cards`** - Information about each card in the game.    
**Returns:** dict {'knight': [CardInfo](cardinfo.md), 'archers': [CardInfo](cardinfo.md),... 'goblins': [CardInfo](cardinfo.md)]

> **`raw_data`** - Raw dictionary data from the API    
**Returns:** dict

> **`url`** - API Endpoint for the profile    
**Returns:** str

> **`update`** - Update the current object    
**Returns:** [Profile](profile.md)

To get your next chest in cycle, look [here](https://grokkers.github.io/cr-async/#/profile?id=methods)!