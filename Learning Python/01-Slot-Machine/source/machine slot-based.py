# Project 1 (Machine Slot-Based)
import random

MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3
symbol_count = {
   "A": 1,
   "B": 3,
   "C": 5,
   "D": 7
}

value_simbol = {
   "A": 1,
   "B": 3,
   "C": 5,
   "D": 7
}

def deposit():
   while True:
      angka = input("Masukkan nominal yang mau di deposit: $")
      if angka.isdigit():
         angka = int(angka)
         if angka > 0:
            break
         else: 
            print("Angka harus lebih dari 0")
      else:
         print("Tolong input angka yang valid")
   return angka

def get_number_line():
   while True:
      line = input("Masukkan baris yang mau dipertaruhkan (1-" + str(MAX_LINE) + "): ")
      if line.isdigit():
         line = int(line)
         if 1 <= line <= MAX_LINE:
            break
         else:
            print("Masukkan baris yang sesuai")
      else:
         print("Baris yang dimasukkan harus berupa angka")
   return line

def get_bet():
   while True:
      bet = input("Masukkan bet: $")
      if bet.isdigit():
         bet = int(bet)
         if MIN_BET <= bet <= MAX_BET:
            break
         else:
            print("Masukkan bet yang sesuai")
      else:
         print("Bet harus berupa angka")
   return bet

def slot_machine_spin(rows, cols, symbol_count):
   semua_simbol = []
   for symbol, count in symbol_count.items():
      for i in range(count):
         semua_simbol.append(symbol)

   columns = []
   for i in range(cols):
      salinan_simbol = semua_simbol.copy()
      column = []
      for j in range(rows):
         value = random.choice(salinan_simbol)
         column.append(value)
         salinan_simbol.remove(value)
      columns.append(column)
   return columns

def print_slot_machine(columns):
   for row in range(len(columns[0])):
      for i, col in enumerate(columns):
         if i != len(columns) - 1:
            print(col[row], end=" | ")
         else:
            print(col[row], end="")
            print()

def check_winnings(columns, lines, bet, value_simbol):
   total_menang = 0
   baris_menang = []

   for row in range(lines):
      simbol_acuan = columns[0][row]
      menang = True
      for col in columns:
         new_simbol = col[row]
         if new_simbol != simbol_acuan:
            menang = False
            break
      if menang:
         hasil = value_simbol[simbol_acuan] * bet
         total_menang = total_menang + hasil
         baris_menang.append(row + 1)
   return total_menang, baris_menang

def spin(balance):
   lines = get_number_line()
   while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
         print(f"Saldomu tidak mencukupi, saldo yang dimiliki: {balance}")
      else:
         break
   print(f"Kamu bertaruh sebanyak {bet}, dan total taruhanmu {total_bet}")
   slots = slot_machine_spin(ROWS, COLS, symbol_count)
   print_slot_machine(slots)

   total_menang, baris_menang = check_winnings(slots, lines, bet, value_simbol)
   print(f"Kamu menang sebanyak ${total_menang}")
   print(f"Kamu menang dibaris ke: {baris_menang}")

   return total_menang - total_bet

def main():
   balance = deposit()
   while True:
      print(f"Saldo saat ini: {balance}")
      jawaban = input("Tekan enter untuk mulai (atau q jika ingin keluar)")
      if jawaban == "q":
         break
      balance = balance + spin(balance)

main()