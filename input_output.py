def is_leap_year(year):
    tahun = int("masukan tahun")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
         True
    else:
         False

year = int(input("Masukkan tahun: "))

if is_leaf_year(year):
    print(f"{year} adalah tahun kabisat.")
else:
    print(f"{year} bukan tahun kabisat.")