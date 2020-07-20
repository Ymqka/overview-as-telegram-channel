import telebot
import telegram

import logging
import re

def post_article(bot_token, chat_id, post):

	bot = telebot.TeleBot(bot_token)

	post_text = '<b>{post_header}</b>\n\n{post_text}\n\n{coordinates}'.format(**post)

	bot.send_photo(chat_id,
					photo = open(post["path_to_image"], 'rb'),
					caption = post_text,
					parse_mode=telegram.ParseMode.HTML
					)


def alert_developers(bot_token, devs_id, msg=""):
	bot = telebot.TeleBot(bot_token)
	for dev_id in devs_id:
		bot.send_message(dev_id, "ALERT: " + msg)

