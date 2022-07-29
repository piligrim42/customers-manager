import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, CustomerN text, CustomerL text, Address text, Telephone text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM customers")
        rows = self.cur.fetchall()
        return rows

    def insert(self, CustomerN, CustomerL, Address, Telephone):
        self.cur.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?, ?)", (CustomerN, CustomerL, 
        Address, Telephone))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM customers WHERE (id=?)", (id,))
        self.conn.commit()


    def update(self, id, CustomerN, CustomerL, Address, Telephone):
        self.cur.execute("UPDATE customers SET CustomerN=?, CustomerL=?, Address=?, Telephone=? WHERE id=?", (CustomerN, CustomerL, Address, Telephone, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()




