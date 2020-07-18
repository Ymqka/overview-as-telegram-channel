#Telegram bot imports
import telebot
import telegram

def post_article(bot_token, chat_id, post):
	"""
	Input:
	bot - telegram bot
	id - id of telegram channel to post
	post - OrderedDict:
	post["path_to_image"] - "imgs/img.jpg"
	post["post_text"] - "Information about image"
	post["post_header"] - "title of post"
	post["coordinates"] - e.g. "41.881944°, -87.627778°"
	"""

	post_text = '<b>{post_header}</b>\n\n{post_text}\n\n{coordinates}'.format(**post)

	bot = telebot.TeleBot(bot_token)
	bot.send_photo(chat_id,
					photo = open(post["path_to_image"], 'rb'),
					caption = post_text,
					parse_mode=telegram.ParseMode.HTML
					)


