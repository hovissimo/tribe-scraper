from datetime import timedelta
import json

import arrow

class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Player):
            return super().default(obj)

        timestamp = (arrow.utcnow() - timedelta(seconds=obj.time)).timestamp
        return {
            'name': obj.name,
            'last_login_time': int(timestamp),
        }

class Player():
    encoder = PlayerEncoder()

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

    def serialized(self):
        return self.encoder.encode(self)

