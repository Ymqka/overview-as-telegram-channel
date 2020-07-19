import psycopg2
import psycopg2.extras
from   psycopg2.extensions import AsIs
# conn = psycopg2.connect(dbname='overview', user='ymka',
#                         password='1w2', host='localhost')

import os
import glob

import datetime
from logger import logger


class OverView_db:
    def __init__(self, conn_data):
        self._connection = psycopg2.connect(dbname = conn_data['db'], user = conn_data['user'],
                                            password = conn_data['pass'], host = conn_data['host'])
        self._cursor = self._connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)


    def count_posts(self):

        cursor = self._cursor
        cursor.execute("select count(*) from posts")
        number_of_posts = list(cursor)[0]['count']

        cursor.execute("select count(*) from posts where posted = FALSE")
        number_of_unposted = list(cursor)[0]['count']

        result = {"Total" : number_of_posts,
                    "not_posted" : number_of_unposted}

        return result


    def delete_all_posts(self):

        cursor = self._cursor

        cursor.execute("Delete from posts *")
        self._connection.commit()

        #Removes all the images in imgs folder
        files = glob.glob(os.getcwd()+"/imgs/*")
        for f in files:
            os.remove(f)

        logger("Successfully deleted all the data")
        return


    def get_a_post(self):   
        #Check is there any post that weren't posted yet
        count = self.count_posts()
        if count['not_posted'] == 0:
            logger('ERROR: No posts left ' + str(count))
            return 

        cursor = self._cursor

        get_one_line_query = """
            select
                *
            from
                posts
            where posted = FALSE
            limit 1;
        """

        cursor.execute(get_one_line_query)
        post = cursor.fetchone()

        update_row_query = """
            UPDATE
                posts
            set
                posted = TRUE
            WHERE id = %s
        """

        post_id = post['id']

        cursor.execute(update_row_query, [post_id])
        self._connection.commit()

        logger('Post with id {} was sent to the bot'.format(post_id))
        return post


    def add_posts(self, posts):
        cursor = self._cursor
        conn   = self._connection

        cursor.executemany("""
            INSERT INTO posts(
                path_to_image,
                post_text,
                post_header,
                coordinates,
                posted
            )
            VALUES(
                %(path_to_image)s,
                %(post_text)s,
                %(post_header)s,
                %(coordinates)s,
                %(posted)s
            )
        """, posts)

        conn.commit()

        return


    def add_post(self, post):
        cursor = self._cursor
        conn   = self._connection

        columns = post.keys()
        values  = [post[column] for column in columns]

        insert_statement = 'insert into posts (%s) values %s'
        args_str = cursor.mogrify(insert_statement, (AsIs(','.join(columns)), tuple(values)))

        cursor.execute(args_str)

        conn.commit()
        logger("Post {} was successfully added".format("") + str(self.count_posts()))
        return


    def __del__(self):
        self._connection.close()
        self._cursor.close()


# cursor = conn.cursor()

# cursor.execute('select * from posts')

# posts = cursor.fetchall()

# print(posts)

# cursor.close()
# conn.close()
