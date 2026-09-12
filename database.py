import sqlite3 as sql

def createDB():
    conn = sql.connect("mercado_aurifero_db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("mercado_aurifero_db")
    cursor = conn.cursor()
    
    cursor.execute(
        """CREATE TABLE gold_price_history IF NOT EXISTS(
            id int PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
            datetime TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )