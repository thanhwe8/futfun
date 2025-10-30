from typing import Protocol, Dict, Any, List, Callable
from datetime import datetime


class Observable:

    def __init__(self):
        self._observers = []
    
    def register(self, obs):
        self._observers.append(obs)

    def notify(self, event):
        for obs in self._observers:
            obs.update(event)

class SeleniumObserver:

    def __init__(self):
        self.count = 0
        self.stats = {
            'search_used':0,
            'bought_players':0,
            'missed_players':0,
            'coin_possesed':0,  # The amount of coin user has
            'coin_used':0,  # The amount of coin user used to buy card
        }
        self.card_stats = {
            'player_name':"",
            "player_rating":"",
            "player_position":""
        }
    def update_search(self):
        self.stats['search_used'] += 1
    
    def update_bought(self):
        self.stats['bought_players'] += 1
    
    def update_missed(self):
        self.stats['missed_players'] += 1

    def get_current_coin_status(self, coin_amount):
        self.stats['coin_possesed'] = coin_amount

    def update_coin_used(self, coin_amount):
        self.stats['coin_used'] += coin_amount

    def get_stats(self):
        return self.stats

    def get_card_stats(self):
        return self.card_stats
