# Api Reference

Here you can see stuff

## Client
Represents the connection to the api          
#### Parameters 

##### **session** (*Optional[aiohttp.ClientSession]*) 
  - an *`aiohttp.ClientSession`* to use, if not provided the default one will be created. 

#### Methods
Note: Valid tags may only contain the following characters: `0289PYLQGRJCUV`

##### *coroutine* **`get_profile(tag)`**
  - Returns a `Profile` object that represents the player's profile. 

##### *coroutine* **`get_clan(tag)`**
  - Returns a `Clan` object that represents a clash royale clan.


## Profile
`class crasync.Profile`

#### Attributes

##### **`tag`** 
  - The player tag associated with the profile
  
##### **`name`**
  - The name of the player.
