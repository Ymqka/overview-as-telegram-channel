#!/bin/bash -e

docker run --rm --network=overview -v $HOME/Docker/volumes/overview/imgs:/usr/local/share/overview/imgs -v $HOME/Docker/images/overview-as-telegram-channel:/usr/local/share/overview/overview-as-telegram-channel --env-file $HOME/Docker/images/overview-as-telegram-channel/env.list post_a_post
