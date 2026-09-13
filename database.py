import sqlite3 as sql

def createTable():
    conn = sql.connect("mercado_aurifero.db")
    cur = conn.cursor()
    
    script = """
    CREATE TABLE IF NOT EXISTS gold_price_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        datetime TEXT NOT NULL,
        price REAL NOT NULL
    );
    """

    cur.execute(
        script
    )

    conn.commit()
    conn.close()

def insert_gold_price(datetime, price):
    data = (datetime, price)

    conn = sql.connect("mercado_aurifero.db")
    cur = conn.cursor()

    script = "INSERT INTO gold_price_history (datetime, price) VALUES (?, ?)"

    cur.execute(
        script,
        data
    )
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createTable()