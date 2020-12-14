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


    def login(self, username, password):
        login_credentioal = self.db_connect.login(username)
        if login_credentioal == password:
            return True
        else:
            return False
    