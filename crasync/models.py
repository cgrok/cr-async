class Base:
    '''
    Base class for models. Only thing that 
    needs to be added is the from_data function
    '''

    def __init__(self, client, data):
        self.client = client
        self.raw_data = data
        self.tag = data.get('tag')
        self.from_data(data)
        endpoint = type(self).__name__.lower()
        self.url = f'{client.BASE}/{endpoint}/{self.tag}'

    def __str__(self):
        return f'{self.name} (#{self.tag})'
       
    async def from_data(self):
        pass

    async def update(self):

        async with self.client.session.get(self.url) as resp:
            data = await resp.json()

        self.raw_data = data
        self.from_data(data)

        return self


class Clan(Base):
    '''Represents a clan'''

    def from_data(self, data):
        pass

class Arena:
    def __init__(self, data):
        self.raw_data = data
        self.name = data.get('name')
        self.number = data.get('arenaID')
        self.trophies = data.get('trophyLimit')

    def __str__(self):
        return self.data.get('arena')

class Profile(Base):
    '''Represents a player profile.
    Includes a clan maybe? (requires a seperate request tho)
    '''
    def from_data(self, data):
        self.name = data.get('name')
        exp = data.get('experience')
        self.level = exp.get('level')
        self.experience = (exp.get('xp'), exp.get('xpRequiredForLevelUp'))
        self.name_changed = data.get('nameChanged')
        self.global_rank = data.get('globalRank')
        self.current_trophies = data.get('trophies')
        self.highest_trophies = data.get('stats').get('challengeCardsWon')
        self.legend_trophies = data.get('legendaryTrophies')
        self.arena = Arena(data.get('arena'))
        self.clan_tag = data.get('clan').get('tag')
        self.clan_name = data.get('clan').get('name')
        self.clan_role = data.get('clan').get('role')

    def get_clan(self):
        return self.client.get_clan(self.clan_tag)




