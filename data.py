from datetime import datetime, timedelta
import json

import arrow
import requests

def get_ark_data(ark_server_uri):
    ''' Get ark data from arkservers api '''
    ARK_API_URI_FORMAT = 'https://arkservers.net/api/query/{server_uri}'
    data_uri = ARK_API_URI_FORMAT.format(ark_server_uri)
    return request(data_uri).json()

def get_players(ark_server_uri):
    api_data = get_ark_data(ark_server_uri)
    return [Player(**p) for p in api_data['players']]

class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Player):
            return super().default(self, obj)
        return {
            name: obj.name,
            last_login_time: int(arrow.utcnow() - timedelta(seconds=obj.time)),
        }

class Player():
    def __init__(self, **kwargs):
        self.frags = kwargs.get('Frags', None)
        self.id = kwargs.get('Id', None)
        self.name = kwargs.get('Name', None)
        self.time = kwargs.get('Time', None)
        self.timeF = kwargs.get('TimeF', None)

    def __repr__(self):
        return 'Player(Name={name})'.format(name=self.name)

    @property
    def login_time(self):
        """ When this user last logged in. """
        return arrow.now() - timedelta(seconds=self.time)
