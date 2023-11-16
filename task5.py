# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GANJIL

def point(x,y):
    return x,y

def line_equation_of(p1, p2):
    #TODO 1: gunakan inner function dan closure untuk menghitung nilai M
    def calculate_m():
        x_1, y_1 = p1
        x_2, y_2 = p2
        return (y_2 - y_1) / (x_2 - x_1)

    x, y = p1
    
    M = calculate_m() #TODO 2: panggil fungsi inner untuk mendapatkan nilai M
    C = y - (M * x)  #TODO 3: tulis rumus untuk mendapatkan nilai C disini
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 2), point(9, 3)))
#ubah nilai input dengan 4 digit nim akhir kalian
#dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
#untuk membuktikan bahwa output sudah benar