from datetime import datetime, timedelta
import json

import arrow
import requests

from log import getLogger

FIREBASE_URI = 'https://busknight.firebaseio.com/tribe-scraper'

def get_firebase_value(fb_path):
    logger = getLogger('tribe-scraper.data')
    uri = FIREBASE_URI + fb_path + '.json'
    logger.info('Fetching Firebase value at "{}"'.format(uri))
    response = requests.get(uri)
    response.raise_for_status()
    value = response.json()
    logger.info('{}: "{}"'.format(response, value))
    return value

def patch_firebase_value(fb_path, value):
    logger = getLogger('tribe-scraper.data')
    uri = FIREBASE_URI + fb_path + '.json'
    logger.info('Patching Firebase value at "{}"'.format(uri))
    response = requests.patch(uri, value)
    response.raise_for_status()
    value = response.json()
    logger.info('{}'.format(value))
