import psycopg2
import psycopg2.extras
# conn = psycopg2.connect(dbname='overview', user='ymka', 
#                         password='1w2', host='localhost')

class OverView_db:
    def __init__(self, conn_data):
        self._connection = psycopg2.connect(dbname = conn_data['db'], user = conn_data['user'],
                                            password = conn_data['pass'], host = conn_data['host'])
        self._cursor = self._connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    def get_a_post(self):
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

        return post

    def add_posts(posts):
        

    def __del__(self):
        self._connection.close()
        self._cursor.close()


# cursor = conn.cursor()

# cursor.execute('select * from posts')

# posts = cursor.fetchall()

# print(posts)

# cursor.close()
# conn.close()