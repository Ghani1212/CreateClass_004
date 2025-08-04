class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self._panjang = panjang
        self._lebar = lebar

    def keliling(self):
        return 2 * (self._panjang + self._lebar)

    def luas(self):
        return self._panjang * self._lebar

    def __str__(self):
        return f"Persegi panjang, panjang {self._panjang} cm, dan lebar {self._lebar} cm"

try:
    panjang_input = int(input("Masukkan panjang (cm): "))
    lebar_input = int(input("Masukkan lebar (cm): "))

    pp = PersegiPanjang(panjang_input, lebar_input)
    print("Keliling:", pp.keliling(), "cm")
    print("Luas:", pp.luas(), "cm²")

except ValueError:
    print("Input harus berupa angka.")