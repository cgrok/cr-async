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
import json
from os import path
from . import core
from .helpers import *

_path = path.join(
    path.dirname(path.realpath(__file__)), 
    'chests.json'
    )

with open(_path.replace('\\','/')) as f:
    CHESTS = json.load(f)

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
        if self.tag is None:
            self.url = '{0.client.BASE}/{1}'.format(self, endpoint)
       
    async def from_data(self, data):
        return NotImplemented

    async def update(self):
        '''Update an object with current info.'''
        if self.client.session.closed:
            async with core.Client() as client:
                data = await client.request(self.url)
        else:
            data = await self.client.request(self.url)

        self.raw_data = data
        self.from_data(data)

        return self

class ClanChest:
    '''Represents a clan chest'''
    def __init__(self, data):
        self.crowns = data.get('clanChestCrowns')
        self.percent = data.get('clanChestCrownsPercent')
        self.required = data.get('clanChestCrownsRequired')
        
class Season:
    '''Represents a Season'''
    def __init__(self, data):
        self.number = data.get('seasonNumber')
        self.highest = data.get('seasonHighest')
        self.ending = data.get('seasonEnding')
        self.end_global = data.get('seasonEndGlobalRank')
        
    def __str__(self):
        return "Season {}".format(self.number)

class Arena:
    '''Represents an arena'''
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
        self.legendary = 0 if data.get('legendary') is None or data.get('legendary', 0) < 0 else data.get('legendary')
        self.epic = 0 if data.get('epic') is None or data.get('epic', 0) < 0 else data.get('epic')
        self.arena = 0 if data.get('arena') is None or data.get('arena', 0) < 0 else data.get('arena')

class Cycle:
    '''Represents your chest cycle'''
    def __init__(self, data):
        self.position = data.get('position')
        self.super_magical = data.get('superMagicalPos')
        self.legendary = data.get('legendaryPos')
        self.epic = data.get('epicPos')

    @property
    def magical(self):
        index = self.position % len(CHESTS)
        count = 0
        x = None
        while x != 'Magic':
            count += 1 
            index += 1
            if index == len(CHESTS):
                index = 0 
            x = CHESTS[index]
        return count+self.position

    @property
    def giant(self):
        index = self.position % len(CHESTS)
        count = 0
        x = None
        while x != 'Giant':
            count += 1 
            index += 1
            if index == len(CHESTS):
                index = 0
            x = CHESTS[index]
        return count+self.position

class CardInfo:
    '''Represents a Clash Royale card'''
    def __init__(self, data):
        self.raw_data = data
        self.name = data.get('name')
        self.rarity = data.get('rarity')
        self.card_id = data.get('card_id')
        self.key = data.get('key')
        self.elixir = data.get('elixir')
        self.type = data.get('type')
        self.arena = data.get('arena')
        self.description = data.get('description')
        self.deck_link = data.get('decklink')
        self.image_url = 'https://cr-api.github.io/cr-api-assets/card/{}.png'.format(self.key)

    def __repr__(self):
        return '<Card id={0.card_id}>'.format(self)

class PlayerCard(CardInfo):

    def __init__(self, data):
        super().__init__(data)
        self.level = data.get('level')
        self.count = data.get('count')
        self.to_upgrade = data.get('requiredForUpgrade')


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
        return '{0.name} (#{0.tag})'.format(self)

    def __repr__(self):
        return '<Member tag={0.tag}>'.format(self)

    def get_profile(self):
        if self.client.session.closed:
            return get_profile(self.tag)
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
        self.name = data.get('name')
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


class ClanInfo:
    def __init__(self, client, data):
        self.raw_data = data
        self.client = client
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
        if self.client.session.closed:
            return get_clan(self.tag)
        else:
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
        self.experience = (
            exp.get('xp'), 
            exp.get('xpRequiredForLevelUp')
            )
        self.xp = self.experience
        self.name_changed = data.get('nameChanged')
        self.global_rank = data.get('globalRank')
        self.current_trophies = data.get('trophies')
        self.highest_trophies = stats.get('maxTrophies')
        self.legend_trophies = data.get('legendaryTrophies')
        self.tournament_cards_won = stats.get('tournamentCardsWon')
        self.challenge_cards_won = stats.get('challengeCardsWon')
        self.favourite_card = stats.get('favoriteCard').title()
        self.total_donations = stats.get('totalDonations')
        self.max_wins = stats.get('challengeMaxWins')
        self.three_crown_wins = stats.get('threeCrownWins')
        self.games_played = games.get('total')
        self.wins = games.get('wins')
        self.losses = games.get('losses')
        self.draws = games.get('draws')
        self.win_streak = 0
        if games.get('currentWinStreak') > 0:
            self.win_streak = games.get('currentWinStreak')
        self.arena = Arena(data.get('arena'))
        self.shop_offers = Shop(data.get('shopOffers'))
        self.chest_cycle = Cycle(data.get('chestCycle'))
        self.deck = [PlayerCard(c) for c in data.get('currentDeck')]
        self.deck_link = 'https://link.clashroyale.com/deck/en?deck='
        for card in self.deck:
            self.deck_link += card.deck_link + ';'
        self.deck_link = self.deck_link[:-1]
        self.clan_tag = None
        self.clan_name = None
        self.clan_role = None
        if clan is not None:
            self.clan_tag = clan.get('tag')
            self.clan_name = clan.get('name')
            self.clan_role = clan.get('role')
        self.seasons = None if data.get('previousSeasons') == [] else [Season(season) for season in data.get('previousSeasons')]

    @property
    def clan_badge_url(self):
        '''Returns clan badge url'''
        if self.clan_tag is None:
            return None
        url = self.raw_data.get('clan').get('badge').get('url')
        if not url:
            return None
        return "http://api.cr-api.com" + url

    def get_chest(self, index=0):
        '''Get your current chest +- the index'''
        
        index += self.chest_cycle.position

        if index == self.chest_cycle.super_magical:
            return 'Super Magical'
        if index == self.chest_cycle.epic:
            return 'Epic'
        if index == self.chest_cycle.legendary:
            return 'Legendary'

        return CHESTS[index % len(CHESTS)]

    def get_clan(self):
        if self.clan_tag is None:
            raise ValueError('Profile has no Clan')
        if self.client.session.closed:
            return get_clan(self.clan_tag)
        else:
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
        self.cards = {c['name'].lower().replace('.','').replace('-',''):CardInfo(c) for c in data.get('cards')}

    def __repr__(self):
        return '<Clash Royale Constants Object>'
