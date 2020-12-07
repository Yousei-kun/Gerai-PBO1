import database_connector as db_con


class Model:
    def __init__(self):
        self.db_connect = db_con.Database_Connect()
        self.db_connect.create_database()
        self.db_connect.create_table()

    def add_item(self, list_input):
        self.db_connect.record_item_value(tuple(list_input))
        print("Barang telah sukses ditambahkan")
    
    def add_warehouse(self, list_input):
        self.db_connect.record_warehouse_value(list_input[0])
        print("Gudang telah sukses ditambahkan")

    def fetch_item(self):
        self.item_data = self.db_connect.get_record_item()

    def fetch_warehouse(self):
        self.db_connect.get_record_warehouse()
    