import MySQLdb


class DB(object):
    conn = None

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

        self.connect()

    def connect(self):
        self.conn = MySQLdb.connect(self.host, self.user, self.password, self.db) # noqa

    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except MySQLdb.OperationalError:  # Upon connection timed out etc.
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
        return cursor

    def try_commit(self):
        try:
            self.conn.commit()
        except BaseException:
            self.conn.rollback()
            raise

    def __del__(self):
        self.conn.close()

    def update_task_status(self, task_id, status):
        self.query(
            """UPDATE task SET status='%s' WHERE id=%s;""" % (status, task_id)
        )
        self.try_commit()

    def add_task_msg(self, task_id, msg):
        self.query(
            """INSERT INTO task_msg VALUES (NULL, '%s', '%s', NOW());""" % (task_id, msg) # noqa
        )
        self.try_commit()
