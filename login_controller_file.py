import person_model_file
import admin_controller_file
# import cashier_controller_file
import trycatch

class Login_Controller:
    def __init__(self):
        self.trycatcher = trycatch.TryCatch()
        self.person_model = person_model_file.Person_Model()

    def show_login_menu(self):
        x = True
        while x == True:
            print("""SELAMAT DATANG DI APLIKASI GERAI
            1. Login (Admin)
            2. Login (Cashier)
            3. Keluar""")
            choose_get = self.trycatcher.input_int(1,3)
            
            if choose_get == 1:
                self.username = self.trycatcher.input_str("Masukkan username: ")
                self.__password = self.trycatcher.input_str("Masukkan password: ")
                if self.person_model.login_verification(self.username, self.__password, '1'):
                    admin_controller = admin_controller_file.Admin()
                    admin_controller.username = self.username
                    admin_controller.show_main_menu() # mengarahkan ke menu admin
                    print("k")
                    x = False
                else:
                    print("Maaf, username / password tidak sesuai dengan data kami.")            
            elif choose_get == 2:
                self.username = self.trycatcher.input_str("Masukkan username: ")
                self.__password = self.trycatcher.input_str("Masukkan password: ")
                if self.person_model.login_verification(self.username, self.__password, '2'):
                    # cashier_controller = cashier_controller_file.Cashier()
                    # cashier_controller.username = self.username
                    # cashier_controller.show_main_menu() # mengarahkan ke menu admin
                    print("y")
                    x = False
                else:
                    print("Maaf, username / password tidak sesuai dengan data kami.")
            elif choose_get == 3:
                exit()  
            else:
                print("Pilihan tidak tersedia")

if __name__ == "__main__":
    login_controller = Login_Controller()
    login_controller.show_login_menu()


