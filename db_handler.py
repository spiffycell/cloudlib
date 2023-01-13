# standard import
import logging

# non-standard import
from postgres import Postgres

# logging config
logging.basicConfig(level=logging.INFO)

# initialize our pg database
pg = Postgres(db_config)
