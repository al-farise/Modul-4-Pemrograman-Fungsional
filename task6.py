# lengkapi kode berikut untuk mendapatkan persamaan garis lurus bagi NIM GANJIL

def point(x,y):
    return x,y

def line_equation_of(p1, M):
    x, y = p1

    C = y - (M * x) #TODO 1: tulis rumus untuk mendapatkan nilai C disini
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (2, 9) dan bergradien 3:")
print(line_equation_of(point(2, 9), 3))
#ubah nilai input dengan 3 digit nim akhir kalian
#dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
#untuk membuktikan bahwa output sudah benar