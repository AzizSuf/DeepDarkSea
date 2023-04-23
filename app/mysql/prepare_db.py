import mysql.connector
import os

def main(config):
    con = mysql.connector.Connect(**config)
    cur = con.cursor()

    with open('prepare_db.sql', 'r') as sql_file:
        result_iterator = cur.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            # Will print out a short representation of the query
            print("Running query: ", res)
            print(f"Affected {res.rowcount} rows" )

        # Remember to commit all your changes!
        con.commit()


if __name__ == '__main__':

    config = {
        "host": os.getenv('MYSQL_HOST'),
        "database": os.getenv('MYSQL_DATABASE'),
        "user": os.getenv('MYSQL_USER'),
        "password": os.getenv('MYSQL_PASSWORD'),
        "port": 3306,
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }

    main(config)