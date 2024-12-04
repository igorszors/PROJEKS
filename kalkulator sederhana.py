print ("kalkulator sederhana")
print ('')
angka_pertama =int( input ("Masukkan angka pertama: "))

opsi =input ("pilih opsi  (+,-,*,/ ): ")
angka_kedua= int ( input("masukkan angka kedua: "))

opsi_plus= angka_pertama + angka_kedua 
opsi_kurang= angka_pertama - angka_kedua 
opsi_kali= angka_pertama * angka_kedua 
opsi_bagi= angka_pertama / angka_kedua

if opsi == '+' :
    print ("hasil dari penjumlahan adalah: "+ str (opsi_plus))
elif opsi == '-' :
    print ("hasil dari penjumlahan adalah: "+ str (opsi_kurang))
elif opsi == '*' :
    print ("hasil dari penjumlahan adalah: "+ str (opsi_kali))
elif opsi == '/' :
    print ("hasil dari penjumlahan adalah: "+ str (opsi_bagi))





