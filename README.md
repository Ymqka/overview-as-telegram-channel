
# Overview As Telegram Channel

> This is unofficial and nonprofit project for https://www.over-view.com.

> The code daily parses posts, updates database and makes a post in telegram channel https://t.me/overview_en.

![Overview](https://www.datocms-assets.com/12893/1571347390-seo-image..jpg)

## Usage

> parse over-view.com/dialy and update postgres database 

```shell
$ python3 overview/get_new_daily.py --config conf/overview.ini
```

> get one random post from postgres database and post it on Telegram channel

```shell
$ python3 overview/make_new_post.py --config conf/overview.ini
```


## Team

| Ymka (Creator) | Jeltorotik| 
| :---: |:---:|
| [![Ymka](https://avatars1.githubusercontent.com/u/21110650?v=3&s=200)](https://github.com/Ymqka)    | [![Jeltorotik](https://avatars0.githubusercontent.com/u/38293253?v=3&s=200)](https://github.com/Jeltorotik) | 
| <a href="https://github.com/Ymqka" target="_blank">`https://github.com/Ymqka`</a> | <a href="https://github.com/Jeltorotik" target="_blank">`https://github.com/Jeltorotik`</a> | 
