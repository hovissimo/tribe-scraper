from datetime import timedelta
import json

import arrow

class PlayerEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Player):
            return super().default(obj)

        timestamp = obj.login_time.to('UTC').timestamp
        return {
            'name': obj.name,
            'last_login_time': int(timestamp),
        }

class Player():
    encoder = PlayerEncoder(ensure_ascii=False)

    def __init__(self, **kwargs):
        self.frags = kwargs.get('Frags', None)
        self.id = kwargs.get('Id', None)
        self.name = kwargs.get('Name', "___unknown___")
        self.time = kwargs.get('Time', None)
        self.timeF = kwargs.get('TimeF', None)
        self.login_time = arrow.now() - timedelta(seconds=self.time)

    def __repr__(self):
        return 'Player(Name={name})'.format(name=self.name)

    def serialized(self):
        return self.encoder.encode(self)

