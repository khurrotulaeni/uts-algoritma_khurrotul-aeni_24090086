jumlah = int(input("Masukan Jumlah yang di beli : "))
harga =int(input("Masukan harga barang 1:"))
harga =int(input("masukan harga barang 2:"))

jumlah_bayar = harga  * harga 

if jumlah >= 5 :
  harga = 1000

else :
    jumlah < 5 
    harga = 2000

total_bayar = jumlah_bayar + harga

print(f"jumlah harga :" , harga)
print(f"total bayar :" , total_bayar)