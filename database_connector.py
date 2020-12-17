import mysql.connector

class Database_Connect:
    def __init__(self):

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        )
    
    def create_database(self):
        cursor = self.db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS db_shop;"
        cursor.execute(sql)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_shop"
        )

    def create_table(self):
        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_warehouse (
                WarehouseID BIGINT AUTO_INCREMENT PRIMARY KEY,
                WarehouseAddress VARCHAR(255)
                );"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS tb_items (
                ItemID BIGINT AUTO_INCREMENT PRIMARY KEY,
                ProductName VARCHAR(255),
                CategoryName VARCHAR(255),
                UnitSellPrice double,
                UnitBuyPrice double,
                StockAvailable DOUBLE,
                StockSold DOUBLE,
                WarehouseID BIGINT,
                FOREIGN KEY (WarehouseID) REFERENCES tb_warehouse(WarehouseID)
                );"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tb_level (
                LevelID BIGINT PRIMARY KEY,
                LevelName VARCHAR(255) NOT NULL
                );"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tb_persons(
                PersonID BIGINT AUTO_INCREMENT PRIMARY KEY,
                PersonName VARCHAR(255),
                Username VARCHAR(255) NOT NULL,
                Password VARCHAR(255) NOT NULL,
                PersonAge BIGINT,
                PersonAdress VARCHAR(255),
                LevelID BIGINT NOT NULL,
                FOREIGN KEY (LevelID) REFERENCES tb_level(LevelID)
            );"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tb_transactions(
                TransactionID BIGINT AUTO_INCREMENT PRIMARY KEY,
                TransactionDate DATE,
                PersonID BIGINT NOT NULL,
                FOREIGN KEY (PersonID) REFERENCES tb_persons(PersonID)
        );"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS tb_transaction_details(
                DetailTransactionID BIGINT AUTO_INCREMENT PRIMARY KEY,
                TransactionID BIGINT NOT NULL,
                ItemID BIGINT NOT NULL,
    			StockSold DOUBLE NOT NULL,
                FOREIGN KEY (TransactionID) REFERENCES tb_transactions(TransactionID),
                FOREIGN KEY (ItemID) REFERENCES tb_items(ItemID)
        );"""
        cursor.execute(sql)


    def record_warehouse_value(self, a):
        cursor = self.db.cursor()
        sql = "INSERT INTO tb_warehouse (WarehouseAddress) VALUE (%s)"
        val = (a,)
        cursor.execute(sql,val)
        self.db.commit()

    def record_item_value(self, list_input):
        cursor = self.db.cursor()
        sql = "INSERT INTO tb_items (ProductName,CategoryName,UnitSellPrice,UnitBuyPrice,StockAvailable,StockSold,WarehouseID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = list_input
        cursor.execute(sql, val)
        self.db.commit()

    def record_update_stock(self, id_stock, amount_stock):
        cursor = self.db.cursor()
        sql = """SELECT StockAvailable FROM tb_items WHERE ItemID = %s"""
        val = (id_stock,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        amount_stock += result[0][0]

        cursor = self.db.cursor()
        sql = """UPDATE tb_items
                SET StockAvailable = %s
                WHERE ItemID = %s"""
        val = (amount_stock, id_stock)
        cursor.execute(sql,val)
        self.db.commit()

    def get_record_item(self):

        cursor = self.db.cursor()
        sql = """SELECT *
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = N'tb_items'"""
        cursor.execute(sql)
        headers = cursor.fetchall()
        self.headers_fix = []
        for i in headers:
            self.headers_fix.append(i[3])

        cursor = self.db.cursor()
        sql = "SELECT * FROM tb_items"
        cursor.execute(sql)
        self.results = cursor.fetchall()

        return self.headers_fix, self.results

    def get_record_warehouse(self):

        cursor = self.db.cursor()
        sql = """SELECT *
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = N'tb_warehouse'"""
        cursor.execute(sql)
        headers = cursor.fetchall()
        headers_fix = []
        for i in headers:
            headers_fix.append(i[3])

        cursor = self.db.cursor()
        sql = "SELECT * FROM tb_warehouse"
        cursor.execute(sql)
        results = cursor.fetchall()

        print("{: <15} {: <100}".format(*headers_fix))
        if cursor.rowcount < 0:
            print("No data")
        else:
            for data in results:
                print("{: <15} {: <100}".format(*data))

    def get_item_values(self):
        if len(self.results) == 0:
            print("No data")
        else:
            print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*self.headers_fix))
            for data in self.results:
                print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*data))
            print("")

    def login(self, name):
        try:
            cursor = self.db.cursor()
            query = "SELECT Password FROM tb_persons WHERE Username = %s"
            cursor.execute(query, (name,))
            return  cursor.fetchone()[0]
        except mysql.connector.Error:
            return ""
        except TypeError:
            return ""

    def get_last_id(self):
        cursor = self.db.cursor()
        sql = "select max(TransactionID) from tb_transactions"
        cursor.execute(sql)

        last_id = cursor.fetchall()
        last_id = last_id[0][0]
        if last_id == None:
            last_id = int(1)
        return last_id
    
    def record_transaction(self, date_now, logged_id = 1):
        cursor = self.db.cursor()
        sql = "INSERT INTO tb_transactions (TransactionDate, PersonID) VALUES (%s, %s)"
        val = (date_now, logged_id)
        cursor.execute(sql,val)
        self.db.commit()

    def record_transaction_details(self, temp_storage, last_id):
        for i in range(0, len(temp_storage)):
            cursor = self.db.cursor()
            sql = "INSERT INTO tb_transaction_details (TransactionID, ItemID, StockSold) VALUES (%s,%s,%s)"
            val = (last_id, temp_storage[i][0], temp_storage[i][1])
            cursor.execute(sql,val)
            self.db.commit()

            # update tabel sebelumbyaaaaa biar dia bisa nguyrang seusai yang dibeliu
            cursor = self.db.cursor()
            sql = "UPDATE tb_items SET StockAvailable=%s, StockSold=%s WHERE ItemID=%s"
            val = (temp_storage[i][2], temp_storage[i][1], temp_storage[i][0])
            cursor.execute(sql, val)
            self.db.commit()

    def get_transaction_ids(self):
        headers_fix = ["ID Transaksi", "Tanggal Transaksi", "ID Kasir"]

        cursor = self.db.cursor()
        sql = "SELECT * FROM tb_transactions"
        cursor.execute(sql)
        results = cursor.fetchall()

        print("{: ^15} {: ^20} {: ^15}".format(*headers_fix))
        if cursor.rowcount < 0:
            print("No data")
        else:
            for data in results:
                print("{: ^15} {: ^20} {: ^15}".format(data[0], data[1].strftime("%d/%m/%Y"), data[2]))
        

    def get_record_transaction(self, check_id):
        cursor = self.db.cursor()
        sql = """SELECT t.TransactionID, t.TransactionDate, p.Username, i.ProductName, td.StockSold, td.StockSold*i.UnitSellPrice as HargaTotal
                FROM tb_transactions t
                join tb_persons p
                on t.PersonID = p.PersonID
                join tb_transaction_details td
                on t.TransactionID = td.TransactionID
                join tb_items i
                on td.ItemID = i.ItemID

                WHERE t.TransactionID = %s"""
        val = (check_id,)
        cursor.execute(sql, val)

        self.results = cursor.fetchall()
        return self.results





        



        