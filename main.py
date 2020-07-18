#Database imports
import sys,os
sys.path.append(os.getcwd()+'/overview')

import config_parser
from db_connection import OverView_db

#from update_database import update_database
from post_article_bot import post_article




#config
config = config_parser.parse_config()
overview_db = OverView_db(config._sections['overview'])


#update_database()


#Gets post from SQL
post = overview_db.get_a_post()


channel_conf = config._sections['telegram']

channel_id = channel_conf['channel_id']
bot_token = channel_conf['bot_token']


post_article(bot_token, channel_id, post)







