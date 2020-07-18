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

channel_ID = channel_conf['channel_id']
token = channel_conf['bot_token']

bot = telebot.TeleBot(TOKEN)

post_article(bot, channel_ID, post)







