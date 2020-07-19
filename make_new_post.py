#Database imports
import sys,os
sys.path.append(os.getcwd()+'/overview')

import config_parser
from db_connection import OverView_db

from post_article_bot import post_article

#config
config = config_parser.parse_config()
overview_db = OverView_db(config._sections['overview'])


#Gets post from SQL
post = overview_db.get_a_post()

channel_id = config._sections['telegram']['channel_id']
bot_token = config._sections['telegram']['bot_token']


post_article(bot_token, channel_id, post)