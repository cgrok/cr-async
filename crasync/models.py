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
        raise NotImplemented

    async def update(self):

        async with self.client.session.get(self.url) as resp:
            data = await resp.json()

        self.raw_data = data
        self.from_data(data)

        return self

class ClanChest:
    def __init__(self, data):
        self.crowns = data.get('clanChestCrowns')
        self.percent = data.get('clanChestCrownsPercent')
        self.required = data.get('clanChestCrownsRequired')

class Arena:
    def __init__(self, data):
        self.raw_data = data
        self.name = data.get('name')
        self.number = data.get('arenaID')
        self.trophies = data.get('trophyLimit')

    @property
    def image_url(self):
        return f"http://api.cr-api.com{self.raw_data.get('imageURL')}"

    def __str__(self):
        return self.data.get('arena')

class Shop:
    def __init__(self, data):
        self.legendary = data.get('legendary')
        self.epic = data.get('epic')
        self.arena = data.get('arena')

class Cycle:
    def __init__(self, data):
        self.position = data.get('position')
        self.super_magical = data.get('superMagicalPos')
        self.legendary = data.get('legendaryPos')
        self.epic = data.get('epicPos')

class Card:
    def __init__(self, data):
        self.name = data.get('name')
        self.rarity = data.get('rarity')
        self.level = data.get('level')
        self.count = data.get('count')
        self.to_upgrade = data.get('requiredForUpgrade')
        self.id = data.get('card_id')
        self.elixir = data.get('elixir')
        self.type = data.get('type')
        self.arena = data.get('arena')
        self.description = data.get('description')
        self.decklink = data.get('decklink')

    def __repr__(self):
        return f'<Card id={self.id}>'

class Member:
    def __init__(self, client, data):
        self.client = client
        self.name = data.get('name')
        self.arena = Arena(data.get('arena'))
        self.role = data.get('role')
        self.role_name = data.get('roleName')
        self.level = data.get('expLevel')
        self.trophies = data.get('trophies')
        self.donations = data.get('donations')
        self.rank = data.get('currentRank')
        self.crowns = data.get('clanChestCrowns')
        self.tag = data.get('tag')

    def __repr__(self):
        return f'<Member tag={self.tag}>'

    def get_profile(self):
        return self.client.get_profile(self.tag)

class Clan(Base):
    '''Represents a clan'''

    def from_data(self, data):
        self.name = data.get('name')
        self.score = data.get('score')
        self.required_trophies = data.get('required_trophies')
        self.donations = data.get('donations')
        self.rank = data.get('currentRank')
        self.description = data.get('description')
        self.type = data.get('type')
        self.type_name = data.get('typeName')
        self.region = data.get('region').get('name')
        self.clan_chest = ClanChest(data.get('clanChest'))
        self.members = [Member(self.client, m) for m in data.get('members')]

    @property
    def badge_url(self):
        url = self.raw_data.get('badge').get('url')
        return f"http://api.cr-api.com{url}"

    def __repr__(self):
        return f'<Clan tag={self.tag}>'

class Profile(Base):
    '''Represents a player profile.
    Includes a clan maybe? (requires a seperate request tho)
    '''
    def from_data(self, data):
        self.name = data.get('name')
        exp = data.get('experience')
        stats = data.get('stats')
        games = data.get('games')
        clan = data.get('clan')
        self.level = exp.get('level')
        self.experience = (exp.get('xp'), exp.get('xpRequiredForLevelUp'))
        self.xp = (exp.get('xp'), exp.get('xpRequiredForLevelUp'))
        self.name_changed = data.get('nameChanged')
        self.global_rank = data.get('globalRank')
        self.current_trophies = data.get('trophies')
        self.highest_trophies = stats.get('challengeCardsWon')
        self.legend_trophies = data.get('legendaryTrophies')
        self.tournament_cards_won = stats.get('tournamentCardsWon')
        self.challenge_cards_won = stats.get('challengeCardsWon')
        self.favourite_card = stats.get('favoriteCard').title()
        self.total_donations = stats.get('totalDonations')
        self.max_wins = stats.get('challengeMaxWins')
        self.games_played = games.get('total')
        self.wins = games.get('wins')
        self.losses = games.get('losses')
        self.draws = games.get('draws')
        self.arena = Arena(data.get('arena'))
        self.clan_tag = clan.get('tag')
        self.clan_name = clan.get('name')
        self.clan_role = clan.get('role')
        self.shop_offers = Shop(data.get('shopOffers'))
        self.chest_cycle = Cycle(data.get('chestCycle'))
        self.deck = [Card(c) for c in data.get('currentDeck')]

    @property
    def clan_badge_url(self):
        url = self.raw_data.get('clan').get('badge').get('url')
        if not url:
            return None
        else:
            return f"http://api.cr-api.com{url}"

    def __repr__(self):
        return f'<Profile tag={self.tag}>'

    def get_clan(self):
        return self.client.get_clan(self.clan_tag)

class Alliance:
    def __init__(self, data):
        self.roles = [c for c in data.get('roles')]
        self.types = [c for c in data.get('types')]

class Country:
    def __init__(self, data):
        self.is_country = data.get('isCountry')
        
    def __str__(self):
        return self.data.get('name')

class Rarity:
    def __init__(self, data):
        self.balance_multiplier = data.get('balance_multiplier')
        self.chance_weight = data.get('chance_weight')
        self.clone_relative_level = data.get('clone_relative_level')
        self.donate_capacity = data.get('donate_capacity')
        self.donate_reward = data.get('donate_reward')
        self.donate_xp = data.get('donate_xp')
        self.gold_conversion_value = data.get('gold_conversion_value')
        self.max_level = data.get('level_count')
        self.mirror_relative_level = data.get('mirror_relative_level')
        self.power_level_multiplier = [c for c in data.get('power_level_multiplier')]
        self.refund_gems = data.get('refund_gems')
        self.relative_level = data.get('relative_level')
        self.sort_capacity = data.get('sort_capacity')
        self.upgrade_cost = [c for c in data.get('upgrade_cost')]
        self.upgrade_exp = [c for c in data.get('upgrade_exp')]
        self.upgrade_material_count = [c for c in data.get('upgrade_material_count')]

    def __str__(self):
        return self.data.get('name')

class Card_Info:
    def __init__(self, data):
        self.name = data.get('name')
        self.rarity = data.get('rarity')
        self.id = data.get('card_id')
        self.elixir = data.get('elixir')
        self.type = data.get('type')
        self.arena = data.get('arena')
        self.description = data.get('description')
        self.decklink = data.get('decklink')

    def __repr__(self):
        return f'<Card id={self.id}>'

class Constants(Base):
    '''Represents the constants from cr-api'''
    def from_data(self, data):
        self.clan = Alliance(data.get('alliance'))
        self.arena = [Arena(c) for c in data.get('arenas')]
        self.badges = [c for c in data.get('badges')]
        self.chest_cycle = [c for c in data.get('chestCycle').get('order')]
        self.country_codes = [Country(c) for c in data.get('countryCodes')]
        self.rarities = [Rarity(c) for c in data.get('rarities')]
        self.card = [Card_Info(c) for c in data.get('rarities')]