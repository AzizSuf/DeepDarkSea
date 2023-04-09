import mysql.connector

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

    # Configure MySQL login and database to use in config.py
    config = {
        "host": "localhost",
        "port": 3306,
        "database": "",
        "user": "root",
        "password": "1234",
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }

    main(config)