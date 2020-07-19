import config_parser
from db_connection import OverView_db

config = config_parser.parse_config()

overview_db = OverView_db(config._sections['overview'])

posts = [{
    "path_to_image": "/qwe/zzz",
    "post_text": "ya text",
    "post_header": "ya header",
    "coordinates": "123 123 412",
    "posted": "FALSE"
},
{
    "path_to_image": "/home/zzz/log",
    "post_text": "text ti",
    "post_header": "ti header",
    "coordinates": "777 666 555",
    "posted": "TRUE"
}]

# overview_db.add_posts(posts)
overview_db.add_post({
    "path_to_image": "/home/zzz/log",
    "post_text": "text ti",
    "post_header": "ti header",
    "coordinates": "777 666 555",
    "posted": "TRUE"
})

