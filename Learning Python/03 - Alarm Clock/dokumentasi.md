# Dokumentasi dari Project Alarm Clock Python.

Pada dokumentasi kali ini, saya akan menulis tentang penjelasan dari code yang ada di `alarm_clock.py`

Jadi pertama kita bahas mulai dari bagian setup library-nya :
```python
from playsound import playsound
from datetime import datetime, timedelta
import time
import os
```
Di bagian setup library ini saya menggunakan :
- playsound = untuk memutar musik yang saya impor dari file .mp3, kalian bisa mengimpornya juga lalu diletakkan di folder tempat script pythonnya diletakkan
- datetime = untuk mengatur waktu karena disini juga tema kita alarm
- time = khusus saya gunakan untuk menggunakan sleep() guna menjeda waktu perhitungan
- os = untuk saya menambahkan jalur foldernya dengan file .mp3 saya dan bisa terkoneksi

Sebelum lanjut, saya ingin menjelaskan bahwa yang saya akan terangkan disini ada versi `Pseudocode` yang saya rancang dengan lengkap, yang merupakan kunci utama sebelum saya bisa mengimplementasikannya menjadi code di source code saya.

### Lanjut ke bagian fungsi alarm-nya :
```
fungsi alarm(seconds):
	waktu_sekarang = datetime.now()
	cetak(waktu_sekarang)
	
	waktu_berlalu = 0 
	selagi waktu_berlalu < seconds:
		time.sleep(1)
		waktu_berlalu += 1
		cetak(f"Waktu mulai berjalan : {waktu_berlalu}")

	playsound("alarm.mp3")
	cetak("Waktunya bangunn!!!")

```

Jadi, disini konsepnya adalah :
- Membuat parameter seconds yang menandakan perhitungan yang akan dilakukan adalah berbasis detik
- Lalu tampilkan waktu sekarang sebagai tampilan verifikasi awal aja untuk memastikan kapan user menyalakan alarmnya
- Buat looping untuk waktu alarmnya (time elapse) yang akan bertambah seiring waktu sampai mencapai detik yang diinput, nah untuk input akan kita bahas di pembahasan code selanjutnya
- Setelah buat looping untuk menghitung elapse timenya, sekarang kita buat agar waktu perhitungannya terjeda 1 detik agar tidak bertabrakan/beruntun menghitungnya seperti kecepatan komputer. Dan kemudian, sesuai yang tadi saya katakan, bahwa kita akan menambahkan waktu yang berlalu (time elapse) dengan 1, untuk menghitung berapa banyak detik yang kita hitung untuk mencapai target yang di-input
- Nyalakan musiknya ketika looping telah sampai ke waktu yang sudah ditargetin

### Lanjut ke inputnya :
```
fungsi minta_input_alarm():
	selagi True:
		alarm_input = input("Setel alarmnya cuy (Jam:Menit) : ")
		parts = alarm_input.split(":")      # Jadikan inputnya ke list dengan split agar bisa dipecah dengan IF, dan dicek formatnya.

		jika panjang_dari_parts(parts) != 2:
			cetak("Format jam dan menit tidak sesuai!")
			ulang inputnya ke user (continue)
		
		coba:
			jam = integer(parts[index pertama dari parts])
			menit = integer(parts[index kedua dari parts])
		kecuali ValueError:       # Mengecualikan error ValueError jika misal inputnya bukan integer, jadi diganti dengan pesan yang dicetak.
			cetak("Jam dan Menit harus berupa angka!")
			ulangi inputnya
		
		jika 0 <= jam <= 23 and 0 <= menit <= 59:    # Validasi rentang waktu agar sesuai dengan yang normal dan tidak melenceng dari penulisan waktu normal.
			hentikan loop
		selain itu:
			cetak("Rentang Waktu tidak sesuai untuk alarm!")
			ulangi inputnya

```

Jadi, kita bahas apa konsep dari input ini :
- Pertama kita looping dulu untuk input sampai validasinya, agar ketika ada input yang tidak sesuai maka fungsi akan meminta input ulang
- Lalu kita meminta input ke user, untuk dia mau setel target alarmnya seberapa, dan hasil inputnya kita pecah dengan split agar bisa menjadi list dan bisa kita validasi berdasarkan index. Kenapa begitu? agar kita bisa ambil hasilnya juga setelah validasi IF, untuk digunakan ke variabel jam dan menit yang dimana itu ada setting waktu yang kita ambil dari input user
- Validasi variabel yang menampung value splitnya itu untuk cek apakah total panjang value di dalam list nya itu 2 atau lebih? kalau lebih itu salah, kenapa? karena kita hanya mengambil jam dan menit (HH:MM) kalau lebih dari itu berarti yang diinput bisa sampe detik bahkan milidetik. HH:MM ketika displit berdasarkan ":" maka akan terpisah yaitu [HH, MM]
- Lalu menggunakan fungsi try/except untuk saya agar memverifikasi juga bagian jam dan menit apakah benar atau tidak,jika tidak langsung beralih ke except gitu. Nah, kita ambil value index pertama yang tadi kita tentukan HH:MM yaitu kita ambil HH nya untuk divariabel jam. Kemudian kita ambil MM untuk variabel menitnya, dan jika ada yang bukan anka maka prosessnya akan error
- Kemudian kebagian validasi rentang waktu, Banyak ya validasinya? HAUS VALIDASI WKWKWK, pusing juga. Oke lanjut jadi rentang waktu harus divalidasi agar kalau user tau-tau masukin 25:61 itukan tidak ada ya di pengaturan waktu manapun gitu. Jadi ini memvalidasinya, kalau rentangnya jam ini dari 0 -23 dan menit dari 0 - 59 itu keluar dari loop untuk nanti dihitung selisih waktu ini (target) ke waktu yang pas user nyalain alarmnya. Kalau rentangnya ngaco, kita minta user input ulang format alarm-nya.

### Lanjut ke bagian Perhitungan selisih waktu target di alarm dan waktu saat user setel nya

```
waktu_saat_ini = datetime.now()
	waktu_target = waktu_saat_ini.replace(hour=jam, minute=menit, second=0, microsecond=0)

	selisih_waktu = waktu_target - waktu_saat_ini


	jika selisih_waktu < timedelta(0):
		waktu_target += timedelta(days=1)
		selisih_waktu = waktu_target - waktu_saat_ini


	total_second = int(selisih_waktu.total_seconds())
	return total_second
```

Jadi, kita bahas untuk konsep perhitungan waktu target alarm dengan waktu saat si user setel alarm :
- Kita definisiin dulu variabel waktu saat ini untuk nunjukkin waktu ketika user nyetel alarmnya
- Lalu kita atur waktu targetnya sesuai dengan yang diinput dari user, jadinya kita pake replace yang dimana fungsi replace dari datetime ini berguna untuk mengganti tahun,bulan,hari,jam,menit,detik,milidetik. Karena disini kita mau mengubah jam dan menit saja sesuai input user maka kita replace jam dan menitnya, nah tapi kenapa detik dan milidetiknya ngikut? karena kita disini mau reset detik dan milidetiknya ke semula, jadi hanya jam dan menit yang berubah, gitu.
- Kemudian kita hitung selisih waktu target alarm dengan waktu saat user setel alarm, dan jika hasilnya minus atau lebih kecil dari waktu saat ini artinya jam yang diseeting user itu sudah lewat dari waktu sekarangnya saat dia setel alarm, ibaratnya gini... Kamu input alarmnya 07:30, tapi waktu dikamu itu udah nunjukkin 09:15. Nah itu jelask waktunya udah lewat dan gabisa mundur kan? solusi nya adalah menambah 1 hari ke alarmnya secara otomatis ketika user setel waktunya kurang dari waktu saat dia setel, jadi dimajuin 1 hari gitu, maka selisihnya jadi 24 jam gitu kan. Nah nambahin satu harinya itu di fungsi timedelta itu (fungsinya sama dengan replace tapi dia langsung memakai + bukan . gitu), jadi langsung gitu, misal : waktu + timedelta(.....), kalau replace dia waktu.replace(....) dan kalau di timedelta itu saat mengubah itu harus ditambahkan 's jadi misal days, hours. Nah kalau replace itu seperti biasanya aja yaitu hour, minute.
- Nah kalau selisih waktunya gak kurang dari timedelta(0) yang dimana ini mengartikan bahwa perhitungan minus (dibawah 0), Maka hasil dari selisihnya akan dipecah dengan fungsi total_seconds() yang berguna untuk memecah perhitungan waktu menjadi detik, jadi hari, jam, menit itu diubah ke detik semua gitu. Dan disitu ada int, kenapa? karena hasil dari total_seconds() adalah float, jadi saya ubah ke integer agar tidak salah ke sistem perhitungannya yang sudah saya atur

- Yang terakhir ada return value dari total_second yang berisi total detik yang sudah dihitung tadi.

### Ke bagian terakhir untuk eksekusinya
```
fungsi main():
	total_detik = minta_input_alarm()
	alarm(total_detik)

main()
```

Disini kalian udah tau lah ya, bahwa kita membuat fungsi main() untuk menjalankan fungsi input dulu, setelah user memasukkan input dan dihitung total detiknya maka ditampung sebagai value di variabel total_detik. Nah abistuh fungsi alarm bisa kalian jalankan dengan variabel total_detik yang berisi total detiknya sehingga fungsi alarm tinggal menghitung detiknya sampai tercapai baru akan bunyi alarm nya.



## Sekian Dokumentasi Alarm Clock Python 
Project ini saya lakukan selama 4 jam terdiri dari : 3 Jam 40 Menit untuk membentuk konsep lengkap dan pseudocode lengkap, tentunya saya mencari referensi dari AI juga (Tidak perlu dipungkiri), dan 20 menit menulis code secara mandiri dari pseudocode saya. Saya akui menuliskode itu mudah kalau konsep nya sudah terbentuk semua, SERIUSS...

Mohon maaf apabila ada salah kata, kurang lengkap, dan juga jika menyinggung pihak lain (Saya disclaimer bahwa tidak ada unsur menyinggung). Sekian, Salam Neroko.