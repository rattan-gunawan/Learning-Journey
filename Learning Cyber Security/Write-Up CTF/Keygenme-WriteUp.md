# Keygenme Pico CTF Write-Up

Untuk solving soal CTF Keygenme dari Pico CTF, pertama kita harus perhatikan file dari script Python yang diberikan 

Jadi download script Python tersebut dan lihat code di dalam script tersebut

Berikut merupakan bagian yang perlu diperhatikan :

```python
   def enter_license():
      user_key = input("\nEnter your license key: ")
      user_key = user_key.strip()

      global bUsername_trial
    
      if check_key(user_key, bUsername_trial):
         decrypt_full_version(user_key)
      else:
         print("\nKey is NOT VALID. Check your data entry.\n\n")
```

Jika kita perhatikan dibagian fungsi validasi check_key, itu menggunakan variabel dari bUsername_trial yang ada dibagian kode paling atas di script tersebut

```python
   username_trial = "BENNETT"
   bUsername_trial = b"BENNETT"
```

Dibagian awal juga tertera beberapa bagian dari flag yaitu `picoCTF{1n_7h3_kk3y_of_` dan `}` yang berarti bagian dari `key_part_dynamic1_trial` ini yang harus kita cari hasilnya yang kalau dilihat dari kodenya ini merupakan Hashing bertipe SHA-256

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True
```

Perhatikan pola dari index yang berada di validasi if untuk me-Hashing permasing-masing kata dari username_trial, tapi ingat kembali bahwa yang akan di check nanti adalah bUsername_trial, jadi username_trial disini hanyalah sebagai parameter.

Kita akan coba membuat kodenya dan menggunakan pola Index nya dari Script soal.

```python
import hashlib

bUsername_trial = b"BENNETT"
key_part_dynamic1_trial = ""

index = [4,5,3,6,2,7,1,8]

for i in index:
   key_part_dynamic1_trial += hashlib.sha256(bUsername_trial).hexdigest()[i]

key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

print(key_full_template_trial)
```

Nah, perhatikan dibagian `key_part_dynamic1_trial`, kenapa dia menjadi string kosong? karena dia sebelumnya berisi string x yang terdiri dari 8 digit, jadi kita akan mengosongkan stringnya dan kemudian kita akan gunakan stringnya untuk diisi hasil hashing dari `bUsername_trial`.

Index yang digunakan merupakan hasil dari index yang dipakai di script soal, jadi kita ubah menjadi satu list lalu kita looping per 1 index untuk mengambil satu kaarkter dari `bUsername_trial` sesuai indexnya.

Untuk bagian kode yang :
```python
key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

Dan untuk bagian dari hashingnya, kalian bisa perhatikan bagian IF difungsi `check_key` tadi :
```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]
```
Nah inilah yang digunakan untuk hashing teks dari `bUsername_trial` nya. Jangan lupa `Import Hashlib` dulu.

Kalian bisa mengambilnya dari script soal yang bagian awal, karena itu merupakan fungsi yang digunakan untuk menggabungkan 3 part key tersebut. Hanya kalau disitu `key_part_dynamic1_trial` ini kosong sehingga fungsinya tidak bisa mendeteksi bagian dari dynamic_trial1 ini

Dan ketika di Run, maka akan menghasilkan flag yang bisa kalian gunakan ( Soal ini berjenis Reverse Engineering )

Credit : Special thanks to [TeckNick80](https://gist.github.com/TeckNick80/a771963d196836bac94467c11b8668da) untuk konsep kode-nya.

Sekian Write-Up saya yang bisa saya jelaskan tentang Keygenme, bila ada yang kurang mohon maaf, dikarenakan saya masih pemula dalam CTF.