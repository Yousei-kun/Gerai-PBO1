import main_controller_file
import admin_model_file
import login_controller_file

class Cashier(main_controller_file.Controller):
    def __init__(self):
        super().__init__()
        self.login_as = "cashier"

    def show_main_menu(self):
        choose_read_write = 0
        while (choose_read_write < 1 or choose_read_write > 4):
            print("""
Menu mana yang akan anda gunakan? (Pilih no 1-3)
1. Lihat data
2. Tambah / Lihat riwayat transaksi
3. Berhenti
4. Logout

Masukkan pilihan anda : """ ,end='')
            try:
                choose_read_write = int(input())
            except ValueError:
                choose_read_write = 0
            if choose_read_write == 1:
                self.show_get_menu()
            elif choose_read_write == 2:
                main_model.payment = 0
                main_model.temp_storage = []
                self.show_transaction_menu()
            elif choose_read_write == 3:
                exit()
            elif choose_read_write == 4:
                print("Anda telah sukses melakukan Logout.")
                print("\n"+"="*50+"\n")
                self.login_as = None
                login_controller.show_login_menu()
            else:
                print("Pilihan tidak tersedia. Mohon input lagi")