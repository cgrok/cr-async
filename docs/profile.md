# Profile
?> Represents a clash royale player profile.

#### Methods

##### *coroutine* **`get_clan()`**
  * Returns the full clan object corresponding to the player's clan.    
  Returns ValueError if player is not in a clan

  * Return Type: [Clan](clan.md)

##### **`get_chest(index=0)`**
  * Returns the `index`'th chest of the player.    
  If player's next chest is `Super Magical`, it returns `Super Magical` when you do `profile.get_clan(0)`

  * Return Type: str
  
#### Attributes
> **`tag`** - The player tag associated with the profile    
**Returns:** int
  
> **`name`** - The name of the player.    
**Returns:** str

> **`level`** - The current level the player is at.    
**Returns:** int

> **`experience`** - A tuple of current xp and xp required to level up.    
**Returns:** tuple (int, int)

> **`name_changed`** - Indicates whether or not the player has changed names.    
**Returns:** bool

> **`global_rank`** - The global rank of the player.    
**Returns**: int or None

> **`current_trophies`** - The number of trophies the player is currently at.    
**Returns:** int
  
> **`highest_trophies`** - The highest trophies the player has reached.    
**Returns:** int
  
> **`legend_trophies`** - The amount of legendary trophies the player has.    
**Returns:** int
  
> **`tournament_cards_won`** - The amount of tournament cards won.    
**Returns:** int

> **`challenge_cards_won`** - The amount of challenge cards won.    
**Returns:** int

> **`favourite_card`** - Current favourite card of the player.    
**Returns:** str

> **`total_donations`** - Number of donations player has made to date.    
**Returns:** int

> **`max_wins`** - Highest amount of challenge wins the player has gotten.    
**Returns:** int

> **`games_played`** - The amount of games played by the player.    
**Returns:** int

> **`wins`** - The amount of games won by the player.    
**Returns:** int

> **`losses`** - The amount of games lost by the player.    
**Returns:** int

> **`draws`** - The amount of games drawn by the player.    
**Returns:** int

> **`win_streak`** - The current win streak of the player.    
**Returns:** int

> **`arena`** - An arena object representing the player's arena.    
**Returns:** [Arena](arena.md)

> **`clan_tag`** - The tag of the clan the player is currently in  
**Returns:** int or None

> **`clan_tag`** - The name of the clan the player is currently in    
**Returns:** str or None

> **`clan_role`** - The role of the player in his current clan    
**Returns:** str or None

> **`shop_offers`** - The time taken for each shop offer to come to the player's shop    
**Returns:** Shop

> **`chest_cycle`** - The current chest cycle information about the player    
**Returns:** [Cycle](cycle.md)

> **`deck`** - The player's deck    
**Returns:** list [[Card](card.md), [Card](card.md), [Card](card.md), [Card](card.md), [Card](card.md), [Card](card.md), [Card](card.md), [Card](card.md)]

> **`clan_badge_url`** - The profile's clan's badge url. Returns None if user is not in a clan.    
**Returns:** str or None

> **`seasons`** - Player's previous seasons.    
**Returns:** List [[Season](season.md), [Season](season.md), [Season](season.md)... [Season](season.md)] or None