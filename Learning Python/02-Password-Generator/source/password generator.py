"""
Konsep Algoritma Password Generator:
1. import module random untuk bisa melakukan acak saat password digenerate
2. import module string untuk mendapatkan berbagai macam ascii letter, digit, punctuation (simbol)
3. membuat fungsi yang menampung jenis-jenis karakter dari module string tersebut yang dimana fungsi ini akan menjadi source utama dalam project ini
4. membuat fungsi untuk meminta input password dari user yang diinginkan seperti apa (apakah ada huruf, angka, simbol) lalu validasi apa yang diinput user sesuai kriteria minimum karakter password yang ditentukan (minimum password karakter), jika tidak memenuhi kriteria minimum panjang password yang kita tentukan maka generatenya akan false dan akan diberi peringatan kepada user untuk memasukkan jumlah password sesuai minimum karakter. lalu juga mungkin kita membuat if-else untuk mengecek jika user meminta angka maka nanti program bisa mengambil angka dari modul string tersebut dan sebagainya.
5. lalu membuat fungsi yang didalam parameternya mungkin bisa kita tambahkan nilai default agar ketika user tidak memilih kriteria karakter apapun, maka yang digenerate akan menyesuaikan default. nah didalam fungsi ini kita bisa membuat vairabel untuk menampung isi dari karakter yang ada di fungsi source tadi, kemudian variabel tersebut akan dijadikan parameter dalam random untuk dipilih secara acak yang mana saja yang akan dimunculkan dan hasilnya itu tampung dalam variabel baru.

"""

import random
import string

def get_source():
   source = {}
   source["upper"] = string.ascii_uppercase
   source["lower"] = string.ascii_lowercase
   source["number"] = string.digits
   source["symbol"] = string.punctuation

   return source

def get_user_input():
   source = get_source()
   while True :
      panjang = int(input("Berapa panjang password yang diinginkan? (min 8 karakter): "))
   
      if panjang < 8:
         print("Panjang password minimal 8 dek, pendek amat kek punya lu")
         continue

      input_kriteria = input("Pilih kriteria password yang mau digenerate (upper/lower/number/symbol): ")
      pilihan_kriteria = input_kriteria.split(",")
      true_kriteria = []
      typo_kriteria = False
      for elemen in pilihan_kriteria:
         clean = elemen.strip().lower()
         if clean == "":
            continue
         elif clean not in source:
            print("Kriteria yang kamu masukkan salah dan tidak dikenali")
            typo_kriteria = True
            break
         else:
            true_kriteria.append(clean)
      if typo_kriteria:
         continue
      if not true_kriteria:
         true_kriteria = ["upper", "lower", "number"]
      if panjang < len(true_kriteria):
         print("Panjang password yang dibuat tidak sesuai dengan kriteria")
         continue

      return panjang, true_kriteria

def generate_password(panjang_pw, jenis_kriteria):
   source = get_source()
   karakter_gabungan = "".join(source[key] for key in jenis_kriteria)

   karakter_wajib = []
   for key in jenis_kriteria:
      wajib = random.choice(source[key])
      karakter_wajib.append(wajib)

   jumlah_sisa = panjang_pw - len(karakter_wajib)
   sisa = []

   for i in range(jumlah_sisa):
      acak = random.choice(karakter_gabungan)
      sisa.append(acak)

   hasil_sementara = karakter_wajib + sisa
   random.shuffle(hasil_sementara)
   password_jadi = "".join(hasil_sementara)

   return password_jadi

def main():
   length, kriteria = get_user_input()
   password = generate_password(length, kriteria)

   print(password)

main()