#Database imports
import sys,os
sys.path.append(os.getcwd()+'/overview')

import config_parser
from db_connection import OverView_db

from update_database import update_database

#config
config = config_parser.parse_config()
overview_db = OverView_db(config._sections['overview'])


update_database(overview_db)