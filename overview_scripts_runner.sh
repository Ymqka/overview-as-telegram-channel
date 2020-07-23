#!/bin/bash -e

python3 /usr/local/share/overview/overview-as-telegram-channel/overview/get_new_daily.py --config /usr/local/share/overview/overview-as-telegram-channel/conf/overview.ini
python3 /usr/local/share/overview/overview-as-telegram-channel/overview/make_new_post.py --config /usr/local/share/overview/overview-as-telegram-channel/conf/overview.ini
# python3 /usr/local/share/overview/overview-as-telegram-channel/overview/test.py --config /usr/local/share/overview/overview-as-telegram-channel/conf/overview.ini
