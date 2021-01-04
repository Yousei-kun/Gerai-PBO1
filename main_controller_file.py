from abc import ABC, abstractmethod
import trycatch

class Controller:
    def __init__(self):
        self.trycatcher = trycatch.TryCatch()


    def show_add_menu(self):
        choose_add = 0
        while (choose_add < 1 or choose_add > 4):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-4)
1. Tambah data barang
2. Tambah data gudang
3. Tambah stok barang (Restock)
3. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            try:
                choose_add = int(input())
            except ValueError:
                choose_add = 0
            if choose_add == 1:
                self.item_input_process()
                main_model.add_item(self.list_add_item_answers)
                self.show_add_menu()
            elif choose_add == 2:
                self.warehouse_input_process()
                main_model.add_warehouse(self.list_add_item_answers)
                self.show_add_menu()
            elif choose_add == 3:
                self.show_restock_item()
                self.show_add_menu()
            elif choose_add == 4:
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

    def show_restock_item(self):
        main_model.fetch_item()
        main_model.print_item_values()
        id_stock = int(input("Masukkan ID item yang akan direstock : "))
        amount_stock = float(input("Masukkan jumlah item yang akan direstock : "))
        main_model.update_stock(id_stock, amount_stock)

    def show_get_menu(self):
        choose_get = 0
        while (choose_get < 1 or choose_get > 5):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-5)
1. Tampilkan data barang
2. Tampilkan data gudang
3. Cari data barang berdasarkan nama / kategori barang
4. Urutkan data barang berdasarkan harga
5. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            try:
                choose_get = int(input())
            except ValueError:
                choose_get = 0
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
            try:
                choose_get = int(input())
            except ValueError:
                choose_get = 0
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

    def show_transaction_menu(self):
        main_model.payment = 0
        main_model.temp_storage = []
        choose_transaction = 0
        while (choose_transaction < 1 or choose_transaction > 3):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-3)
1. Buat transaksi baru
2. Lihat riwayat transaksi
3. Kembali ke menu utama

Masukkan pilihan anda : """ ,end='')
            choose_transaction = int(input())
            if choose_transaction == 1:
                main_model.payment = 0
                self.add_transaction_item()
            elif choose_transaction == 2:
                self.show_transaction_history()
            elif choose_transaction == 3:
                self.show_main_menu()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")

    def add_transaction_item(self):
        self.show_current_receipt()
        main_model.fetch_receipt_body()
        item_id = int(input("Masukkan ID barang\t: "))
        stock_sold = float(input("Masukkan jumlah barang\t: "))
        main_model.check_availability(item_id, stock_sold)
        print("""Lanjutkan transaksi?
1. Ya
2. Tidak, print struk

Masukkan pilihan anda : """ ,end='')
        try:
            print_now = int(input())
        except ValueError:
            print_now = 0
        if print_now == 1:
            self.add_transaction_item()
        elif print_now == 2:
            main_model.fetch_add_next_transaction_info()
            self.show_receipt_body()
            main_model.record_transaction()
            print("Proses print struk...")
            print("Print sukses")
            main_model.payment = 0
            main_model.temp_storage = []
            self.show_transaction_menu()
        else:
            print("Pilihan tidak tersedia. Mohon input lagi")
            self.add_transaction_item()

    def show_current_receipt(self):
        main_model.fetch_item()
        main_model.print_item_values()
        main_model.fetch_add_next_transaction_info()
    
    def show_receipt_body(self):
        main_model.fetch_receipt_body()

    def show_transaction_history(self):
        main_model.fetch_transaction_ids()
        print()
        id_fetch = int(input("Masukkan ID yang akan dilihat : "))
        main_model.fetch_transaction_history(id_fetch)
        self.show_transaction_menu()
        
    @abstractmethod    
    def show_main_menu(self):
        pass