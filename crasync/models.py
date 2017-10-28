'''
MIT License

Copyright (c) 2017 grokkers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class Base:
    '''
    Base class for models. Only thing that 
    needs to be added is the from_data function
    '''

    def __init__(self, client, data):
        self.client = client
        self.raw_data = data
        self.name = data.get('name')
        self.tag = data.get('tag')
        self.from_data(data)
        endpoint = type(self).__name__.lower()
        self.url = '{0.client.BASE}/{1}/{0.tag}'.format(self, endpoint)
       
    async def from_data(self):
        return NotImplemented

    async def update(self):
        '''Update an object with current info.'''
        async with self.client.session.get(self.url) as resp:
            data = await resp.json()

        self.raw_data = data
        self.from_data(data)

        return self

class ClanChest:
    '''Represents a clan chest'''
    def __init__(self, data):
        self.crowns = data.get('clanChestCrowns')
        self.percent = data.get('clanChestCrownsPercent')
        self.required = data.get('clanChestCrownsRequired')

class Arena:
    '''represents an arena'''
    def __init__(self, data):
        self.raw_data = data
        self.name = data.get('name')
        self.number = data.get('arenaID')
        self.trophies = data.get('trophyLimit')

    @property
    def image_url(self):
        return "http://api.cr-api.com" + self.raw_data.get('imageURL')

    def __str__(self):
        return self.name

class Shop:
    '''Represents shop offers'''
    def __init__(self, data):
        self.legendary = data.get('legendary')
        self.epic = data.get('epic')
        self.arena = data.get('arena')

class Cycle:
    '''Represents your chest cycle'''
    def __init__(self, data):
        self.position = data.get('position')
        self.super_magical = data.get('superMagicalPos')
        self.legendary = data.get('legendaryPos')
        self.epic = data.get('epicPos')

class Card:
    '''Represents a Clash Royale card'''
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
        return '<Card id={0.id}>'.format(self)

class Member:
    '''Represents a member of a clan'''
    def __init__(self, client, clan, data):
        self.clan = clan
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

    def __str__(self):
        return '{self.name} (#{0.tag})'.format(self)

    def __repr__(self):
        return '<Member tag={0.tag}>'.format(self)

    def get_profile(self):
        return self.client.get_profile(self.tag)

class Alliance:
    def __init__(self, data):
        self.roles = data.get('roles')
        self.types = data.get('types')

class Country:
    def __init__(self, data):
        self.name = data.get('name')
        self.is_country = data.get('isCountry')
        
    def __str__(self):
        return self.name

class Rarity:
    def __init__(self, data):
        self.name =  data.get('name')
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
        return self.name

class CardInfo:
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
        return '<Card id={0.id}>'.format(self)

class ClanInfo:
    def __init__(self, client, data):
        self.raw_data = data
        self.name = data.get('name')
        self.tag = data.get('tag')
        self.trophies = data.get('trophies')
        self.region = data.get('region').get('name')
        self.member_count = data.get('memberCount')
        self.rank = data.get('rank')
        self.previous_rank = data.get('previousRank')

    @property
    def badge_url(self):
        url = self.raw_data.get('badge').get('url')
        return "http://api.cr-api.com" + url

    def get_clan(self):
        return self.client.get_clan(self.tag)

    def __repr__(self):
        return '<ClanInfo tag={0.tag}>'.format(self)

    def __str__(self):
        return '{0.name} (#{0.tag})'.format(self)


class Clan(Base):
    '''Represents a clan'''

    def from_data(self, data):
        self.name = data.get('name')
        self.score = data.get('score')
        self.required_trophies = data.get('requiredScore')
        self.donations = data.get('donations')
        self.rank = data.get('currentRank')
        self.description = data.get('description')
        self.type = data.get('type')
        self.type_name = data.get('typeName')
        self.region = data.get('region').get('name')
        self.clan_chest = ClanChest(data.get('clanChest'))
        self.members = [Member(self.client, self, m) for m in data.get('members')]

    @property
    def badge_url(self):
        url = self.raw_data.get('badge').get('url')
        return "http://api.cr-api.com" + url

    def __repr__(self):
        return '<Clan tag={0.tag}>'.format(self)

    def __str__(self):
        return '{0.name} (#{0.tag})'.format(self)
    
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
            return "http://api.cr-api.com" + url

    def get_clan(self):
        return self.client.get_clan(self.clan_tag)

    def __repr__(self):
        return '<Profile tag={0.tag}>'.format(self)

    def __str__(self):
        return '{0.name} (#{0.tag})'.format(self)

class Constants(Base):
    '''Represents the constants from cr-api'''
    def from_data(self, data):
        self.clan = Alliance(data.get('alliance'))
        self.arena = [Arena(c) for c in data.get('arenas')]
        self.badges = data.get('badges')
        self.chest_cycle = [c for c in data.get('chestCycle').get('order')]
        self.country_codes = [Country(c) for c in data.get('countryCodes')]
        self.rarities = [Rarity(c) for c in data.get('rarities')]
        self.card = [CardInfo(c) for c in data.get('rarities')]

    def __repr__(self):
        return '<Clash Royale Constants Object>'

