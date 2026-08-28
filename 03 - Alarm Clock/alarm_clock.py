from playsound import playsound
from datetime import datetime, timedelta
import time
import os

folder_script = os.path.dirname(__file__)
path_mp3 = os.path.join(folder_script, "alarm.mp3")


def alarm(seconds):
   waktu_sekarang = datetime.now()
   print(waktu_sekarang)

   waktu_berlalu = 0
   while waktu_berlalu < seconds:
      time.sleep(1)
      waktu_berlalu += 1
      print(f"Waktu mulai berjalan : {waktu_berlalu}")
   playsound(path_mp3)
   print("Waktunya bangunn!!!")

def minta_input_alarm():
   while True:
      alarm_input = input("Setel alarmnya cuy (Jam:Menit) : ")
      parts = alarm_input.split(":")

      if len(parts) != 2:
         print("Format jam dan menit tidak sesuai")
         continue

      try:
         jam = int(parts[0])
         menit = int(parts[1])
      except ValueError:
         print("Jam dan Menit harus berupa angka!")
         continue

      if 0 <= jam <= 23 and 0 <= menit <= 59:
         break
      else:
         print("Rentang waktu tidak sesuai")
         continue

   waktu_saat_ini = datetime.now()
   waktu_target = waktu_saat_ini.replace(hour=jam, minute=menit, second=0, microsecond=0)

   selisih_waktu = waktu_target - waktu_saat_ini

   if selisih_waktu < timedelta(0):
      waktu_target += timedelta(days=1)
      selisih_waktu = waktu_target - waktu_saat_ini

   total_second = int(selisih_waktu.total_seconds())
   return total_second

def main():
   total_detik = minta_input_alarm()
   alarm(total_detik)

main()