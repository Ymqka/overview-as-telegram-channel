import config_parser
from db_connection import OverView_db

config = config_parser.parse_config()

overview_db = OverView_db(config._sections['overview'])

post = overview_db.get_a_post()

