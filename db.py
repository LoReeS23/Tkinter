import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS bills (id INTEGER PRIMARY KEY, item varchar(100),'
                            'price float, VAT_in_percent int(2) DEFAULT 23,'
                            'bill_date date DEFAULT CURRENT_DATE)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, item varchar(100),'
                            'price float, NIP int(10), corporation_name varchar(100), corporation_address varchar(100),'
                            'VAT_in_percent int(2) DEFAULT 23,'
                            'invoice_date date DEFAULT CURRENT_DATE)')
        self.connection.commit()

    def fetch(self):
        self.cursor.execute('select * from bills, invoices')
        rows = self.cursor.fetchall()
        return rows

    def insert_bills(self, item, price, vat):
        self.cursor.execute("INSERT INTO bills (item, price, VAT_in_percent) VALUES (?, ?, ?)", (item, price, vat))
        self.connection.commit()

    def insert_invoices(self, item, nip, corporation_name, corporation_address):
        self.cursor.execute("INSERT INTO invoices VALUES (NULL, ?, ?, ?, ?)",
                            (item, nip, corporation_name, corporation_address))
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
