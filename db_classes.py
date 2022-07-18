import sqlite3

DB_NAME = 'db_parser.db'

class ConnectDB:
    def __init__(self):
        self.db_name = DB_NAME

    def get_all_projects(self):
        pass

    def get_url(self, project_id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        url = cur.execute(
            "SELECT project_url FROM projects WHERE id=:id", {'id': project_id}
            # "SELECT * FROM projects"
        )
        result = url.fetchone()
        con.close()

        return result[0]

    # def insert_prices_data(self, project_id, date, discount_price, price, installment_price):