import config_parser
from db_connection import OverView_db

#config
args   = config_parser.parse_arguments()
config = config_parser.parse_config(args.config)


overview_db = OverView_db(config['overview'])



post_1 = {
    "path_to_image" : "imgs/adelaide-canola-flowers.jpg",
    "post_text" : "Chicago is the most populous city in the state of Illinois and the third most populous city in the United States, with upwards of 2.7 million people. Located on the shores of Lake Michigan, the city’s gridded avenues stretch from the vibrant waters. For a sense of scale, O’Hare International Airport, which covers 11.9 square miles (30.8 square km), is visible in the bottom left.",
    "post_header" : "Chicago and Lake Michigan",
    "coordinates" : "41.881944°, -87.627778°",
    "posted" : "FALSE",
    "epoch_id" : 123
    #"link" : "https://www.over-view.com/overviews/adelaide-canola-flowers"
}

if __name__ == '__main__':
	#overview_db.add_post(post_1)
	print(overview_db.count_posts())
	#overview_db.delete_all_posts()