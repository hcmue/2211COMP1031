import pymysql


class DbUtil:
    @staticmethod
    def get_connection():
        try:
            return pymysql.connect(host='localhost', user='root', password='',
                                   database='cnwebcomp103102', cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            return None

    @staticmethod
    def get_data(select_query):
        conn = DbUtil.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(select_query)
            result = cursor.fetchall()
            conn.close()
            return result
        return []

    @staticmethod
    def execute_data(sql_command):
        conn = DbUtil.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(sql_command)
            conn.commit()
            conn.close()
            return True
        return False

    @staticmethod
    def insert_and_get_id(insert_command):
        conn = DbUtil.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(insert_command)
            conn.commit()
            last_id = cursor.lastrowid
            conn.close()
            return last_id
        return None
