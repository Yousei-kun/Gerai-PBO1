import main_controller_file
import transaction_model_file
import login_controller_file

class Admin(main_controller_file.Controller):
    def __init__(self):
        # super().__init__()
        self.admin_model = transaction_model_file.Transaction_Model()
        self.login_as = "admin"

    def show_main_menu(self):
        choose_read_write = 0
        print("""
Menu mana yang akan anda gunakan? (Pilih no 1-5)
1. Tambah data 
2. Lihat data
3. Tambah / Lihat riwayat transaksi
4. Berhenti
5. Logout

Masukkan pilihan anda : """ ,end='')
        
        choose_read_write = self.

        if choose_read_write == 1:
            self.show_add_menu()
        elif choose_read_write == 2:
            self.show_get_menu()
        elif choose_read_write == 3:
            self.show_transaction_menu()
        elif choose_read_write == 4:
            exit()
        elif choose_read_write == 5:
            print("Anda telah sukses melakukan Logout.")
            print("\n"+"="*30+"\n")
            self.login_as = None
            login_controller = login_controller_file.Login_Controller()
            login_controller.show_login_menu()
        else:
            print("Pilihan tidak tersedia. Mohon input lagi")


