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
        )
        result = url.fetchone()
        con.close()

        return result[0]

    def save_prices(self,
                    project_id,
                    date,
                    average_price,
                    tariff_1,
                    tariff_2,
                    tariff_3,
                    tariff_4,
                    tariff_5):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute(
            "INSERT INTO price"
            "(project_id, input_date, average_price, tariff_1, tariff_2,"
            "tariff_3, tariff_4, tariff_5)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [project_id, date, average_price, tariff_1, tariff_2, tariff_3,
             tariff_4, tariff_5]
        )
        con.commit()
        con.close()
