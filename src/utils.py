import logging


def config_logs(log_name):
    # init
    log = logging.getLogger(log_name)
    # set loglevel
    log.setLevel(level=logging.INFO)
    # set format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s \
            - %(message)s')
    # set handler
    handler = logging.StreamHandler()
    # set handler loglevel
    handler.setLevel(level=logging.DEBUG)
    # set handler formatter
    handler.setFormatter(formatter)
    # set log handler
    log.addHandler(handler)
