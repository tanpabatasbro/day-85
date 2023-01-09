#MENGHITUNG GAJI BERSIH
nama = input("Masukkan Nama : ")
pekerjaan = input("Masukkan Pekerjaan : ")
gaji= int(input("Masukkan Gaji/Bulan : "))

if gaji >= 5_000_000:
    pajak = 10/100
    potongPajak = gaji * pajak
    gajiBersih = gaji - potongPajak
    print(f"\nNama : {nama}")
    print(f"pekerjaan : {pekerjaan}")
    print(f"Gaji Sebelum Dikenakan Pajak : {gaji}")
    print(f"Pajak 10% sebesar : {potongPajak}")
    print(f"Gaji Bersih : {gajiBersih}")
    
    if pekerjaan == "pns":
        pajakPns = 5/100
        potongPajakPns = gajiBersih * pajakPns
        gajiBersihPns = gajiBersih - potongPajakPns
        print(f"Pajak PNS 5% sebesar : {potongPajakPns}")
        print(f"Gaji Bersih PNS : {gajiBersihPns}")
        
elif gaji >= 3_000_000:
    pajak = 5/100
    potongPajak = gaji * pajak
    gajiBersih = gaji - potongPajak
    print(f"\nNama : {nama}")
    print(f"pekerjaan : {pekerjaan}")
    print(f"Gaji Sebelum Dikenakan Pajak : {gaji}")
    print(f"Pajak 5% sebesar : {potongPajak}")
    print(f"Gaji Bersih : {gajiBersih}")
    if pekerjaan == "pns" and "PNS":
        pajakPns = 5/100
        potongPajakPns = gajiBersih * pajakPns
        gajiBersihPns = gajiBersih - potongPajakPns
        print(f"Pajak PNS 5% sebesar : {potongPajakPns}")
        print(f"Gaji Bersih PNS : {gajiBersihPns}")

else:
    print(f"Nama : {nama}")
    print(f"pekerjaan : {pekerjaan}")
    print(f"Gaji (BebasPajak) : {gaji}")    
    
    