# Write-Up Sleuthkit Apprentice PicoCTF

Okey teman-teman, kali ini saya akan menuliskan write up tentang Challenge `Forensic` di PicoCTF yang berjudul `Sleuthkit Apprentice` dan disini saya memakai Kali Linux.

Jadi pertama kita lihat dulu deskripsi dan juga file dari soalnya :

![alt text](<image/Screenshot 2026-08-29 at 10-34-28 CyLab Security Academy - Forensics in CTF's(1).png>)

Disini kita bisa lihat bahwa ada deskripsi untuk `Download Disk Image` dan `Find the flag`. Oke jadi karena disini awalnya saya bingung dan saya challenge untuk mengerjakan tanpa bantuan cara apapun, hanya mencari tools. Jadi saya sudah mencoba banyak cara.

Kita bisa melakukan wget dulu untuk save di webshell bawaan web atau kalau memakai kali linux juga bisa langsung wget/curl :
```bash
$wget [URL dari disk imagenya]
```
Setelah filenya di wget maka, kita akan mendapatkan file dengan format `disk.flag.img.gz`, nah disini filenya masih di kompresi sehingga kita harus melakukan gunzip dulu ya guys (kalau filenya zip, kalian bisa memakai unzip) :
```bash
$gunzip disk.flag.img.gz
```

Lalu setelah kalian melakukan gunzip terhadap filenya, kemudian kalian bisa melakukan command yaitu :
```bash
$mmls disk.flag.img
```

Setelah itu kalian bisa melihat Sector dan juga Descriptionnya, disini jangan terlalu diperhatikan untuk bagian Unallocated atau Swap ( karena kita tidak mencari sisa apapun di swap dan kita tidak mencari data yang dihapus atau disembunyikan di sini, kecuali ada clue). Cukup perhatikan bagian `Linux (0x83)`.

Nah karena sector 0000002048 itu sudah dilakukan di challenge sebelumnya jadi sepertinya anda sudah tau itu digunakan sebelumnya, dan ada satu sector yang belum diperiksa/digunakan yaitu 0000360448. Nah ini patut dicurigai karena kita sudah pernah menggunakan sektor 2048 sebelumnya ya.
Langsung aja kita cek :
```bash
$fls -o 0000360448 disk.flag.img
```
Nah, nanti akan muncul menu yang sama seperti di sektor 2048, tapi pasti isinya ada yang beda, kita bisa cek satu satu direktori yang menurut kali penting (karena saya melakukan itu). Kalian bisa mencari di direktori seperti `var, usr, tmp, home, root`, Hanya sekedar saran karena saya sendiri banyak melakukan cek direktorinya hampir semua.

Nah setelah kalian cari-cari filenya, dan kalian menyerah maka kalian bisa melihat kembali writeup ini. Jadi kita akan cek bagian direktori root karena di direktori penting lainnya sudah kita cek dan tidak ada apa apa gitu ya (biasanya tidak ada output yang artinya isinya kosong).

Cari kebagian root nya :

![alt text](image/Screenshot_2026-08-29_10_34_01(1)(1).png)

Cara mencarinya gimana? perhatikan inode (Seperti ID direktori/file) disamping tipenya yang d/d yaitu `1995`:

Formatnya :
fls -r -o [Nomor Sector] [Nama File] [Inode dari file/direktori]

```bash
$fls -r -o 0000360448 disk.flag.img 1995
```
Nah fungsi dari optionnya saya jelasin singkat aja :

-o = untuk mencari file image dari offset nya yaitu dari start sector

-r = untuk mencari isi dari file tersebut secara rekursif/berulang, jadi lebih mendalam gitu

Dan akan muncul output seperti ini :

![alt text](<image/root nya.png>)

Nah disitu ada hal yang mencurigakan, yaitu file dengan nama .ash_history dan mari kita coba lihat isinya, disini saya `icat` aja filenya karena belum terlalu sepuh untuk melihat dengan trik lain. Disini inode-nya kita ganti dengan inode dari ash_history tersebut.
```bash
$icat -o 0000360448 disk.flag.img 2363
```
![alt text](image/icat.png)

Nah, bisa kita perhatikan isi filenya itu historynya adalah add nano lalu ganti direktori ke my_folder, lalu melakukan command di nano setelah itu melakukan convert dan outputnya dimasukkan ke file `flag.uni.txt`.

Kemudian, disini kita bisa cek aja langsung file itu, dengan 
```bash
$fls -r -o 0000360448 disk.flag.img | grep "flag.uni.txt"
```
![alt text](image/flaguni.png)

Nah, bisa kita perhatikan disini kenapa saya grep? karena saya mau ambil nama file yang ada di partisi image ini yang memiliki nama tersebut, dan ternyata ada. Langsung aja kita `icat` dan masukin inode-nya dari `flag.uni.txt`.
```bash
$icat -o 0000360448 disk.flag.img 2371
```

Nah selesai deh, kalian bisa dapetin flagnya.


### Segitu aja guys untuk write-up nya, terimakasih dan mohon maaf apabila ada salah kata/tools/penamaan dari saya. Sekian...
Dan untuk bisa mengerjakan ini juga tidak tiba-tiba ya guyss, di challenge sebelumnya saya mencari bantuan dan disini karena saya sudah mulai paham makanya saya coba challenge sendiri. Maaf kalau bahasanya masih ada yang kurang.