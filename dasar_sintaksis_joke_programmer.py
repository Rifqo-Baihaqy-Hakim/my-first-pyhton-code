"""
Semua Sintaksis bahasa pemograman terdiri dari :
1. Sekuensial: langkah berurutan
2. Percabangan: akah melompat jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu berkata, "Pergi ke toko" ')
print('Budi menjawab, "Apa yang harus saya lakukan di toko?"')
print('Ibu menjawab "Beli satu botol susu, dan jika ada telor beli 6"')
print("Maka Budi berangkat ke toko ")
print("Dan mulai belanja")

# Percabangan
jumlah_botol_susu = 179
jumlah_telur = 1587
print(f"Jumlah botol susu {jumlah_botol_susu} botol ")
print(f"Jumalah telur {jumlah_telur} butir")


if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli satu botol susu")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli satu botol susu ")

print("Budi Pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")
print("Kemudian Ibu berkata")
print("")
