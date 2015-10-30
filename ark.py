import logging
import requests

import data
from log import getLogger
from player import Player

class Ark():
    def __init__(self, name):
        self.name = name
        self._server_uri = None
        self._api_uri = None

    def __str__(self):
        return '(Ark: {})'.format(self.name)

    @property
    def data_path(self):
        return '/arks/{}'.format(self.name)

    @property
    def api_uri(self):
        if not self._api_uri:
            logger = getLogger('tribe-scraper.ark')
            logger.debug('First time: Getting {} api_uri_format from firebase'.format(self))
            api_uri_format = data.get_firebase_value('/configuration/api-uri-format')
            self._api_uri = api_uri_format.format(self.server_uri)
        return self._api_uri

    @property
    def server_uri(self):
        if not self._server_uri:
            logger = getLogger('tribe-scraper.ark')
            logger.debug('First time: Getting {} server_uri from firebase'.format(self))
            self._server_uri = data.get_firebase_value(self.data_path + '/connect_uri')
        return self._server_uri

    def get_active_players(self):
        logger = getLogger('tribe-scraper.ark')
        logger.info('Getting player list from {}'.format(self.api_uri))
        response = requests.get(self.api_uri)
        response.raise_for_status()
        players = [Player(**p) for p in response.json()['players']]
        logger.info('{}: {} player(s)'.format(response, len(players)))
        return players

