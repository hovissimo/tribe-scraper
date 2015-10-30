import logging

def prepare_logging():
    logger = logging.getLogger('tribe-scraper')

    if logger.hasHandlers():
        logger.warning('Logger has already been set up')
        return # This logger is already set up

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('tribe-scraper.log')
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

prepare_logging()
getLogger = logging.getLogger
