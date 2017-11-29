# Clan
?> Represents a clash royale clan.

#### Attributes

> **`tag`** - The tag of the clan.    
**Returns:** str

> **`name`** - The name of the clan.    
**Returns:** str

> **`score`** - The clan's score (throphies)    
**Returns:** int

> **`required_trophies`** - The clan's required trophies    
**Returns:** int

> **`donations`** - The clan's donations/week    
**Returns:** int

> **`rank`** - The clan's position on the global leaderboard (Returns 0 if not on leaderboard)    
**Returns:** int 

> **`description`** - The clan's description    
**Returns:** str

> **`type`** - The clan's type (Open, Invite Only, Closed)    
**Returns:** int

> **`type_name`** - The clan's type (Open, Invite Only, Closed)    
**Returns:** str

> **`region`** - The clan's region    
**Returns:** str

> **`clan_chest`** - The clan's clan chest data    
**Returns:** [ClanChest](clanchest.md)

> **`members`** - The clan's members    
**Returns:** list [[Member](member.md), [Member](member.md), [Member](member.md)... [Member](member.md)]

> **`badge_url`** - The clan's badge url    
**Returns:** str

> **`raw_data`** - Raw dictionary data from the API    
**Returns:** dict

> **`url`** - API Endpoint for the clan    
**Returns:** str

> **`update`** - Update the current object    
**Returns:** [Clan](clan.md)