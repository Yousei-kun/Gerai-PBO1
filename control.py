from model_file import Model 

class Controller:
    def __init__(self):
        self.list_add_item_questions = ['Masukkan nama barang : ', 'Masukkan kategori barang : ', ' Masukkan harga beli barang : ',
                                  'Masukkan harga jual barang : ', "Masukkan Stok yang tersedia (dalam kg ATAU pcs) : ", "Masukkan ID gudang penyimpanan : "]

    def show_main_menu(self):
        choose_read_write = 0
        while (choose_read_write < 1 or choose_read_write > 3):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-3)
1. Tambah data (Hanya untuk Admin)
2. Lihat data
3. Tambah transaksi
3. Berhenti
4. Logout

Masukkan pilihan anda : """ ,end='')
            choose_read_write = int(input())
            if choose_read_write == 1:
                self.show_add_menu()
            elif choose_read_write == 2:
                self.show_get_menu()
            elif choose_read_write == 3:
                exit()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")
    
    def show_add_menu(self):
        choose_add = 0
        while (choose_add < 1 or choose_add > 3):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-2)
1. Tambah data barang
2. Tambah data gudang
3. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            choose_add = int(input())
            if choose_add == 1:
                self.item_input_process()
                main_model.add_item(self.list_add_item_answers)
            elif choose_add == 2:
                self.warehouse_input_process()
                main_model.add_warehouse(self.list_add_item_answers)
            elif choose_add == 3:
                self.show_main_menu()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")

    def item_input_process(self):
        self.list_add_item_answers = []
        for i in range(0, len(self.list_add_item_questions)):
            print(self.list_add_item_questions[i], end='')
            if i == 5:
                self.list_add_item_answers.append(0)
            if i in [0,1]:
                str(self.list_add_item_questions[i])
                self.try_str_input(i)
            else:
                str(self.list_add_item_questions[i])
                self.try_int_input(i)
        self.show_add_menu()
        

    def warehouse_input_process(self):
        self.list_add_item_answers = []
        print("Masukkan alamat gudang baru : ")
        self.try_str_input()
        
    def try_str_input(self, i = 0):
        try:
            val = str(input())
            float(val)/0
        except ZeroDivisionError:
            print("Barang tidak boleh berwujud angka saja. Masukkan lagi detail barang")
            self.try_str_input(i)
        except ValueError:
            self.list_add_item_answers.append(val)
    
    def try_int_input(self, i):
        try:
            val = float(input())
            self.list_add_item_answers.append(val)
        except ValueError:
            print("Kolom ini tidak boleh berisi huruf. Masukkan lagi detail barang")
            self.try_int_input(i)

    def show_get_menu(self):
        choose_get = 0
        while (choose_get < 1 or choose_get > 3):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-2)
1. Tampilkan data barang
2. Tampilkan data gudang
3. Cari data barang berdasarkan nama / kategori barang
4. Urutkan data barang berdasarkan harga
5. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            choose_get = int(input())
            if choose_get == 1:
                main_model.fetch_item()
                main_model.print_item_values()
                self.show_get_menu()
            elif choose_get == 2:
                main_model.fetch_warehouse()
                self.show_get_menu()
            elif choose_get == 3:
                main_model.fetch_item()
                self.search_data()
                self.show_get_menu()
            elif choose_get == 4:
                main_model.fetch_item()
                main_model.print_sorted_item()
            elif choose_get == 5:
                self.show_main_menu()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")
    
    def search_data(self):
        choose_get = 0
        while (choose_get < 1 or choose_get > 2):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-2)
1. Masukkan nama barang ATAU kategori barang
2. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            choose_get = int(input())
            if choose_get == 1:
                try:
                    val = str(input())
                    float(val)/0
                except ZeroDivisionError:
                    print("Barang tidak boleh berwujud angka saja. Masukkan lagi detail barang")
                    self.search_data()
                except ValueError:
                    main_model.print_search_item(val)
                self.search_data()
            elif choose_get == 2:
                self.show_get_menu()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")

    def show_login_menu(self):
        while True:
            print("""SELAMAT DATANG DI APLIKASI GERAI
            1. Login (Admin)
            2. Login (Pelanggan)""")
            choose_get = int(input("Masukkan pilihan anda: "))
            if choose_get == 1:
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                if main_model.login(username, password):
                    self.show_main_menu() # mengarahkan ke menu admin
                else:
                    print("Maaf, username / password tidak sesuai dengan data kami.")            
            elif choose_get == 2:
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                if main_model.login(username, password):
                    self.show_main_menu() # mengarahkan ke menu kasir
                else:
                    print("Maaf, username / password tidak sesuai dengan data kami.")   
            else:
                print("Pilihan tidak tersedia")


    def show_transaction_menu(self):
        pass
        

if __name__ == "__main__":
    main_model = Model()
    main_controller = Controller()
    main_controller.show_login_menu()
