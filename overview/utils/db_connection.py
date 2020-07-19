import psycopg2
import psycopg2.extras
from   psycopg2.extensions import AsIs

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
            WHERE epoch_id = %s
        """

        epoch_id = post['epoch_id']

        cursor.execute(update_row_query, [epoch_id])
        self._connection.commit()

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
                epoch_id,
                posted
            )
            VALUES(
                %(path_to_image)s,
                %(post_text)s,
                %(post_header)s,
                %(coordinates)s,
                %(epoch_id)s,
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

        return

    def get_not_parsed_posts_epoch_id(self, epoch_ids):
        cursor = self._cursor

        epoch_ids_str = ','.join(str(x) for x in epoch_ids)

        parsed_posts_epoch_id_query = """
            select
                epoch_id
            from
                posts
            where epoch_id in (%s);
        """ % epoch_ids_str

        cursor.execute(parsed_posts_epoch_id_query, epoch_ids_str)
        db_epoch_ids = [x['epoch_id'] for x in cursor.fetchall()]

        not_parsed_posts_epoch_id = []
        for epoch_id in epoch_ids:
            if epoch_id not in db_epoch_ids:
                not_parsed_posts_epoch_id.append(epoch_id)

        return not_parsed_posts_epoch_id

    def __del__(self):
        self._connection.close()
        self._cursor.close()
