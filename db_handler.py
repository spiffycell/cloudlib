# standard import
import logging
import os

# non-standard import
from postgres import Postgres

# env vars
POSTGRES_USER = os.getenv("POSTGRES_USER", None)
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", None)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_DB = os.getenv("POSTGRES_DB", "test")

# logging config
logging.basicConfig(level=logging.INFO)

# we set the db_config so we can pass it into our
# postgres object in order to init a connection
db_config = {"username": POSTGRES_USER, \
        "password": POSTGRES_PASSWORD, \
        "host": POSTGRES_HOST, \
        "port": POSTGRES_PORT, \
        "database":POSTGRES_DB \
        }

# initialize our pg database
pg = Postgres(db_config)
