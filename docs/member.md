# Member
?> Represents a member from a clash royale clan.

#### Attributes
> **`name`** - The name of the member.      
**Returns:** str

> **`arena`** - An arena object representing the player's arena.    
**Returns:** [Arena](arena.md)

> **`role`** - The role of the member in his clan.    
**Returns:** int

> **`role_name`** - The role of the member in his clan.    
**Returns:** str

> **`level`** - The member's XP Level.    
**Returns:** int

> **`trophies`** - The number of trophies the member has.     
**Returns:** int

> **`donations`** - The number of cards the member donated to his clan so far in the season.    
**Returns:** int

> **`donations`** - The number of cards the member donated to his clan so far in the season.    
**Returns:** int

> **`currentRank`** - The rank of the member in his clan.    
**Returns:** int

> **`crowns`** - The number of crowns the member contributed to his clan chest.    
**Returns:** int

#### Methods

##### *coroutine* **`get_profile()`**
  * Returns the full player object corresponding to the member.
