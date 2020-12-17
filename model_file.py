import database_connector as db_con
import datetime


class Model:
    def __init__(self):
        self.db_connect = db_con.Database_Connect()
        self.db_connect.create_database()
        self.db_connect.create_table()
        self.receipt_header = ["No", "Nama Barang", "Jumlah Beli", "Total"]
        self.temp_storage = []
        self.payment = 0

    def login(self, username, password):
        login_credentioal = self.db_connect.login(username)
        if login_credentioal == password:
            self.logged_username = username
            self.logged_id = 1
            return True
        else:
            return False

    def add_item(self, list_input):
        self.db_connect.record_item_value(tuple(list_input))
        print("Barang telah sukses ditambahkan")
    
    def add_warehouse(self, list_input):
        self.db_connect.record_warehouse_value(list_input[0])
        print("Gudang telah sukses ditambahkan")

    def update_stock(self, id_stock, amount_stock):
        self.db_connect.record_update_stock(id_stock, amount_stock)
        print("Sukses")

    def fetch_item(self):
        self.header_data, self.item_data = self.db_connect.get_record_item()
    
    def print_item_values(self):
        self.db_connect.get_item_values()

    def print_search_item(self,val):
        filtered_item_data = []

        for i in range(0, len(self.item_data)):
            if val.lower() in self.item_data[i][1].lower() or val.lower() in self.item_data[i][2].lower():
                filtered_item_data.append(self.item_data[i])

        if len(filtered_item_data) == 0:
            print("Produk tidak ditemukan")
        else:
            print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*self.header_data))
            for data in filtered_item_data:
                print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*data))
            print("")

    def fetch_warehouse(self):
        self.db_connect.get_record_warehouse()
    
    def print_sorted_item(self):

        sorted_item_data = self.item_data

        for i in range(0,len(sorted_item_data)-1): 
            # Last i elements are already in place 
            for j in range(0, len(sorted_item_data)-1-i): 
                if sorted_item_data[j][3] < sorted_item_data[j+1][3] : 
                    sorted_item_data[j], sorted_item_data[j+1] = sorted_item_data[j+1], sorted_item_data[j]
        
        if len(sorted_item_data) == 0:
            print("Tidak ada produk")
        else:
            print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*self.header_data))
            for data in sorted_item_data:
                print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*data))
            print("")

    def fetch_add_next_transaction_info(self, method2 = 1):
        if method2 == 1:
            self.last_id = self.db_connect.get_last_id()
            self.last_id += 1
            self.date_now = datetime.datetime.now().strftime("%d/%m/%Y")
        
        elif method2 == 2:
            self.last_id = self.temp_storage[0][0]
            self.date_now = self.temp_storage[0][1].strftime("%d/%m/%Y")
            self.logged_username_temp = self.logged_username
            self.logged_username = self.temp_storage[0][2]
            self.payment = 0
            for data in self.temp_storage:
                self.payment += data[5]

        print("""ID Struk\t\t: {}
Tanggal Struk\t\t: {}
Nama Pegawai\t\t: {}
Total bayar\t\t: Rp {}""".format(self.last_id,self.date_now,self.logged_username, self.payment))
        self.logged_username = self.logged_username_temp

    def check_availability(self,item_id, stock_sold):
        found = 0

        for i in range (0,len(self.item_data)):
            if item_id == self.item_data[i][0]:
                item_stock = self.item_data[i][5]
                if item_stock >= stock_sold:
                    self.temp_storage.append([item_id, stock_sold, self.item_data[i][5]-stock_sold, self.item_data[i][1], self.item_data[i][3]])
                    print("Barang berhasil ditambahkan")
                    self.payment += stock_sold * self.item_data[i][3]
                else:
                    print("Stok tidak cukup. Tidak diperkenankan menambahkan transaksi")
                found += 1
                break

        if found == 0:
            print("Barang tidak ditemukan")
        
    def fetch_receipt_body(self, method2 = 1):
        if len(self.temp_storage) == 0:
            print("No data")
        else:
            print("{: <5} {: <30} {: <15} {: <15}".format(*self.receipt_header))
            if method2 == 1:
                for i in range(0,len(self.temp_storage)):
                    print("{: <5} {: <30} {: <15} {: <15}".format(i+1, self.temp_storage[i][3], self.temp_storage[i][1], self.temp_storage[i][1]*self.temp_storage[i][4]))
            elif method2 == 2:
                for i in range(0,len(self.temp_storage)):
                    print("{: <5} {: <30} {: <15} {: <15}".format(i+1, self.temp_storage[i][3], self.temp_storage[i][4], self.temp_storage[i][5]))

    def record_transaction(self):
        self.date_submit = datetime.datetime.now().strftime("%Y-%m-%d")
        self.db_connect.record_transaction(self.date_submit, self.logged_id)
        self.db_connect.record_transaction_details(self.temp_storage, self.last_id)
        print("Sukses")


    def fetch_transaction_ids(self):
        self.db_connect.get_transaction_ids()

    def fetch_transaction_history(self, id_fetch):
        self.temp_storage = self.db_connect.get_record_transaction(id_fetch)
        self.fetch_add_next_transaction_info(2)
        self.fetch_receipt_body(2)


        



    