import os,sys
import time
from colorama import init,Fore,Style,Back
an = 0.0
ya = len(sys.argv)
try:
  def math(a,b):
    ez = a + b
    print(f"{Fore.WHITE}Program Ini Dibuat Dengan {Fore.BLUE}sys.call_tracing")
    time.sleep(.5)
    print(f"{Fore.WHITE}Hasil Dari %d + %d : {Fore.GREEN}{ez}{Fore.WHITE}" % (a,b))
  os.system('clear')
  print(Fore.BLUE,"Bermain Main Dengan Module sys",Fore.WHITE)
  print("Tunggu Sebentar ...")
  time.sleep(2)
  print(Fore.WHITE,"\bNama File          :",Fore.BLUE,sys.argv[0],Fore.WHITE)
  time.sleep(.5)
  print("Lokasi             :",Fore.BLUE,sys.base_exec_prefix,Fore.WHITE)
  time.sleep(.5)
  print("Panjang Huruf File :",Fore.BLUE,len(sys.argv[0]),Fore.WHITE)
  sys.call_tracing(math,(int(input(f"Masukan Angka ke 1 :  {Fore.GREEN}")),int(input(f"{Fore.WHITE}Masukan Angka ke 2 :  {Fore.GREEN}"))))
  for ngentot in range(1,ya):
    an += float(sys.argv[ngentot])
  print(ngentot)
  print("Hasil  : ",Fore.GREEN,an)
except ValueError:
  print("Masukkan Angka !")
try:
  angka = 5
  angka2 = 40
  user = input(f"{Fore.WHITE}Lanjut y/n ? ")
  if user == "y" or "Y":
     os.system('clear')
     iya = input("Masukkan Huruf min 5, max 40 : ")
     if len(iya) > angka2:
        print(Fore.RED,"Jangan Lebih Ngentot !")
     elif len(iya) < angka:
        print(Fore.RED,"Jangan Dikit Juga Dek !")
     elif len(iya) > angka and len(iya) < 40:
        inp = input(f"{Fore.WHITE}Sudah y/n ? ")
        print("Tunggu ...")
        time.sleep(1)
        if inp == "y" or "Y":
          print("\nTotal Huruf Yang Kamu Input : %s" % len(iya))
          time.sleep(.5)
          print("cv ke huruf kapital : %s" % iya.upper())
          print("cv ke huruf kecil : %s" % iya.lower())
          print("Total huruf (a) : %s " % iya.count('a'))
          time.sleep(.5)
          print("3 huruf depan : %s" % iya[:3])
          print("Sisa Huruf Setelah 3 : %s" % iya[3:])
          time.sleep(.5)
          print(f"{Fore.WHITE}Jalankan Ulang : {Fore.BLUE}python sys2.py {Fore.RED}[angka]{Fore.WHITE}")
     else:
        print("Oke !")
  else:
     print("Okey !")
except:
  print("Masukkan Huruf !")
