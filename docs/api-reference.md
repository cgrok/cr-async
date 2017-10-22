# Client
```py
class crasync.Client(session=None)
```                
## Parameters   
#### **session** (*Optional[aiohttp.ClientSession]*) 
  - an *`aiohttp.ClientSession`* to use, if not provided the default one will be created. 

## Methods
#### *coroutine* **`get_profile(tag)`**
  - Returns a `Profile` object that represents the cr player. 
```py
profile = await client.get_profile('2P0LYQ)
```
#### *coroutine* **`get_clan(tag)`**
