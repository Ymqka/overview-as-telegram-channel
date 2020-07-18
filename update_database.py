def update_database():
	"""
	This function checks out https://www.over-view.com for new articles
	and if so, downloads to PostSQL database a new post
	"""
	# <YOUR CODE HERE> :)

	#######

	print("Database Succesfully updated:")
	print(overview_db.count_posts())
	