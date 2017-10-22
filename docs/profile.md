# Profile
?> Represents a clash royale player profile.

#### Attributes

> **`tag`** - The player tag associated with the profile
  
> **`name`** - The name of the player.

> **`level`** - The current level the player is at.

> **`experience`** - A tuple of current xp and xp required to level up.

> **`name_changed`** - Indicates whether or not the player has changed names.

> **`global_rank`** - The global rank of the player.

> **`current_trophies`** - The number of trophies the player is currently at.
  
> **`highest_trophies`** - The highest trophies the player has reached.
  
> **`legend_trophies`** - The amount of legendary trophies the player has.
  
> **`tournament_cards_won`** - The amount of tournament cards won.

> **`challenge_cards_won`** - The amount of challenge cards won.

> **`favourite_card`** - Current favourite card of the player.

> **`total_donations`** - Number of donations player has made to date.

> **`max_wins`** - Highest amount of challenge wins the player has gotten.

> **`games_played`** - The amount of games played by the player.

> **`wins`** - The amount of games won by the player.

> **`losses`** - The amount of games lost by the player.

> **`draws`** - The amount of games drawn by the player.

> **`arena`** - An arena object representing the player's arena.


#### Methods

##### *coroutine* **`get_clan()`**
  * Returns the full clan object corresponding to the player's clan.
