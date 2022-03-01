import psycopg2


class PyPostgres:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def executarSelect(self,query):

        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result


    def execUpdateOuInsert(self, query):

        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()