# Api Reference

The following section outlines the api of crasync.

## Client
Represents the connection to the api, this class is used to interact with cr-api.com
          
#### Parameters 

##### **session** (*Optional[aiohttp.ClientSession]*) 
  - an *`aiohttp.ClientSession`* to use, if not provided the default one will be created. 

#### Methods
Note: Valid tags may only contain the following characters: `0289PYLQGRJCUV`

##### *coroutine* **`get_profile(tag)`** - Returns a [Profile](#profile) object that represents the player's profile. 

##### *coroutine* **`get_clan(tag)`** - Returns a [Clan](#clan) object that represents a clash royale clan.


## Profile
Represents a clash royale player profile.

#### Attributes

##### **`tag`** 
  - The player tag associated with the profile
  
##### **`name`**
  - The name of the player.

##### **`level`**
  - The current level the player is at.

##### **`experience`**
  - A tuple consisting of current experience and experience required to level up.



