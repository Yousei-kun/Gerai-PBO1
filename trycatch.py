class TryCatch():
    def __init__(self):
        self.menu_int = ['Masukkan Menu yang diinginkan : ']
        self.list_add_item_questions = ['Masukkan nama barang : ', 'Masukkan kategori barang : ', ' Masukkan harga beli barang : ',
                                        'Masukkan harga jual barang : ', "Masukkan Stok yang tersedia (dalam kg ATAU pcs) : ", "Masukkan ID gudang penyimpanan : "]
        self.menu_str = ['Masukkan nilai yang diinginkan : ']

    def input_int(self, low_limit = None, high_limit = None, menu = None):
        if menu == None:
            menu = self.menu_int[0]
        while True:
            try:
                input_num = int(input(menu))
                if input_num > low_limit or input_num < high_limit:
                    break
                else:
                    raise TypeError
            except ValueError:
                print("Masukan hanya dapat berupa angka. Masukkan lagi angka yang diinginkan")
            except TypeError:
                print("Angka yang anda masukkan diluar batas. Masukkan lagi angka yang diinginkan")
        return input_num

    def input_str(self, menu = None):
        if menu == None:
            menu = self.menu_str[0]
        while True:
            try:
                input_str = input(menu)
                float(input_str)/0
            except ValueError:
                break
            except ZeroDivisionError:
                print("Masukan hanya dapat berupa huruf/kombinasi angka dan huruf. Masukkan lagi angka yang diinginkan")
        return input_str


