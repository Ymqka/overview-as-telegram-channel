import utils
#imports overVieww_db, parse_config() and post_article

import os
from boto.s3.connection import S3Connection

import time
import sys
import logging

logging.basicConfig(
    filename = 'overview.log',
    level=logging.INFO, 
    format= '[%(asctime)s] %(levelname)s - %(message)s {%(pathname)s:%(lineno)d}',
    datefmt='%Y-%m-%d %H:%M:%S'
)


#config
args   = utils.parse_arguments()
config = utils.parse_config(args.config)

channel_id = config['telegram']['channel_id']
bot_token = os.environ['bot_token']
devs_id = os.environ['devs_id'].split(',')


overview_db = utils.OverView_db(config['overview'])


number_of_posts = overview_db.count_posts()

if number_of_posts['not_posted'] > 0:

	
	post = overview_db.get_a_post()

	try:
		utils.post_article(bot_token, channel_id, post)

	except Exception as e:
		logging.error("Bot failed to post", exc_info=e)
		utils.alert_developers(bot_token, devs_id)

	logging.info("A post with epoch ID: " + post['epoch_id'] + " was succesfully posted")
else:
	logging.error('No posts: ' + str(number_of_posts))
	utils.alert_developers(bot_token, devs_id)
