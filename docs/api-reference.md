# Client
```py
class crasync.Client(session=None)
```                
### Parameters   
#### **session** (*Optional[aiohttp.ClientSession]*) 
  - an *`aiohttp.ClientSession`* to use, if not provided the default one will be created. 

### Methods
Note: Valid tags may only contain the following characters: `0289PYLQGRJCUV`

#### *coroutine* **`get_profile(tag)`**
  - Returns a `Profile` object that represents the player's profile. 
```py
profile = await client.get_profile('2P0LYQ')
```
#### *coroutine* **`get_clan(tag)`**
  - Returns a `Clan` object that represents a clash royale clan.
```py
clan = await client.get_clan('9RQ928L')
```

# Models
