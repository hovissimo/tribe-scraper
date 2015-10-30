import schedule, time

from ark import Ark
import data
from log import getLogger
from player import Player

def get_players():
    ark = Ark('FernGully')
    players = ark.get_active_players()
    return players

def submit_player(player, ark):
    fb_path = ark.data_path + '/players/' + player.name
    data.patch_firebase_value(fb_path, player.serialized())

def main():
    logger = getLogger('tribe-scraper.main')
    ark = Ark('FernGully')
    for p in get_players():
        try:
            submit_player(p, ark)
        except Exception as e:
            logger.error(e)

if __name__ == '__main__':
    schedule.every(20).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
