# from optparse import OptionParser
import inspect
import telebot
import telegram
import os

channel_id = "-1001308741280"
bot_token = os.environ['bot_token']

bot = telebot.TeleBot(bot_token)


bot.send_photo(channel_id,
                photo =  open('/usr/local/share/overview/imgs/1560989945-arcdetriomphe.jpg', 'rb'),
                caption =  "asdfsas",
                parse_mode = telegram.ParseMode.HTML
                )

# print('hello world')