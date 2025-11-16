import pandas as pd
import datetime as dt
import os

def connect_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="langgeng847",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="SEEDBRIDGE")
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Gagal terhubung ke database", error)
        return None, None
    finally:
        pass

def clear_terminal():
    os.system('cls')

def kembali():
    inputan_kembali = input('Tekan enter untuk kembali...')
    if inputan_kembali == '':
        clear_terminal()
    else:
        kembali()

# FITUR CUSTOMER
def Katalog_Benih():
    try:
      print()
      print()
      print("=== WELCOME TO KATALOG BENIH ===")
      print("1. Lihat Alur Pesanan")
      print("2. Generate Laporan")
      print("3. Update Status Pengiriman")
      print("4. Keluar")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def Filter_Benih():
    try:
      print()
      print()
      print("=== WELCOME TO FILTER BENIH ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def Keranjang_Belanja():
    try:
      print()
      print()
      print("=== WELCOME TO KERANJANG BELANJA ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def Checkout_Belanja():
    try:
      print()
      print()
      print("=== WELCOME TO CHECKOUT BELANJA ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def Status_Transaksi():
    try:
      print()
      print()
      print("=== WELCOME TO STATUS TRANSAKSI ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()
 
def Riwayat_Transaksi():
    try:
      print()
      print()
      print("=== WELCOME TO RIWAYAT TRANSAKSI ===")
    except Exception as e :
      print(f"Terjadi Error: {e}") 
    print()
    print()

def Ulasan():
    try:
      print()
      print()
      print("=== WELCOME TO ULASAN ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

# FITUR ADMIN
def lihat_alur_pesanan():
  try:
    print()
    print()
    print("=== LIHAT ALUR PESANAN ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()

def generate_laporan():
  try:
    print()
    print()
    print("=== TAMPILKAN LAPORAN ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()
  
def update_status_pengiriman():
  try:
    print()
    print()
    print("=== UPDATE STATUS PENGIRIMAN ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()
  
# FITUR PRODUSEN

def cek_stok():
  try:
    print()
    print()
    print("=== CEK STOK HABIS/KADALUARSA ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()

def update_benih():
  try:
    print()
    print()
    print("=== TAMPILKAN LAPORAN ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()
  
def lihat_daftar_order():
  try:
    print()
    print()
    print("=== UPDATE STATUS PENGIRIMAN ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()

# MENU TIAP ROLE
def menu_admin():
    print()
    print("=== WELCOMEE ADMINN ===")
    print()
    print("1. Lihat Alur Pesanan")
    print("2. Generate Laporan")
    print("3. Update Status Pengiriman")
    print("4. Keluar")
    try: 
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == '1':
            lihat_alur_pesanan()
        elif pilihan == '2':
            generate_laporan()
        elif pilihan == '3':
            update_status_pengiriman()
        elif pilihan == '4':
            clear_terminal()
            print("Keluar dari menu admin.")
            print()
            gambar()
            dashboard()
        else:
            print()
            clear_terminal()
            print("Pilihan tidak valid. Silakan coba lagi.")
            menu_admin()
    except Exception as e :
     print(f"Terjadi Error: {e}")
  
def menu_customer():
    print()
    print("=== WELCOMEE CUSTOMERR ===")
    print()
    try:
        print("1. Katalog Benih")
        print("2. Filter Benih")
        print("3. Keranjang Belanja")
        print("4. Checkout Belanja")
        print("5. Status Transaksi")
        print("6. Riwayat Transaksi")
        print("7. Ulasan")
        print("8. Keluar")
        pilih = input("Pilih Menu Customer: ")
        if pilih == "1":
            Katalog_Benih()
        elif pilih == "2":
            Filter_Benih()
        elif pilih == "3":
            Keranjang_Belanja()
        elif pilih == "4":
            Checkout_Belanja()
        elif pilih == "5":
            Status_Transaksi()
        elif pilih == "6":
            Riwayat_Transaksi()
        elif pilih == "7":
            Ulasan()
        elif pilih == "8":
            clear_terminal()
            print('Keluar dari menu Customer')
            print()
            gambar()
            dashboard()
        else :
            clear_terminal()
            print()
            print('=== PILIHAN TIDAK VALID ===')
            print()
            menu_customer()
    except Exception as e :
        print(f"Terjadi Error: {e}")
  

def menu_produsen():
    print()
    print("=== WELCOMEE PRODUSEN ===  ")
    print()
    print("1. Cek Stok Habis/Kadaluarsa")
    print("2. Update Stok Benih")
    print("3. Lihat Daftar Order")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    if pilihan == '1':
      cek_stok()
    elif pilihan == '2':
      update_benih()
    elif pilihan == '3':
      lihat_daftar_order()
    elif pilihan == '4':
      clear_terminal()
      print('Keluar dari Menu Produsen')
      print()
      gambar()
      dashboard()
    else:
      clear_terminal()
      print()
      print("Pilihan tidak valid. Silakan coba lagi.")
      print()
      menu_produsen()

def gambar():
  print(""" 
  █████████                        █████ ███████████             ███      █████                  
 ███░░░░░███                      ░░███ ░░███░░░░░███           ░░░      ░░███                   
░███    ░░░   ██████   ██████   ███████  ░███    ░███ ████████  ████   ███████   ███████  ██████ 
░░█████████  ███░░███ ███░░███ ███░░███  ░██████████ ░░███░░███░░███  ███░░███  ███░░███ ███░░███
 ░░░░░░░░███░███████ ░███████ ░███ ░███  ░███░░░░░███ ░███ ░░░  ░███ ░███ ░███ ░███ ░███░███████ 
 ███    ░███░███░░░  ░███░░░  ░███ ░███  ░███    ░███ ░███      ░███ ░███ ░███ ░███ ░███░███░░░  
░░█████████ ░░██████ ░░██████ ░░████████ ███████████  █████     █████░░████████░░███████░░██████ 
 ░░░░░░░░░   ░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░░░░░░░░  ░░░░░     ░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  
                                                                                ███ ░███         
                                                                               ░░██████          
                                                                                ░░░░░░                
      """)

def dashboard():
  while True :
    try:
      ds = input("Apakah sudah memiliki akun ? yes/no: ").lower()
      if ds == "yes":
        login()
      elif ds == "no":
        register()
        break
      else :
        clear_terminal()
        gambar()
        print()
        print()
        print("=== INPUTAN TIDAK VALID ===")
        print("=== COBA LAGI ===")
        print()
        dashboard()
    except Exception as e :
        print(f"Terjadi Error: {e}")
  
  
def login():
  usn = input("Username: ")
  pw = input("Password: ")
  if usn == "admin" and pw == "admin":
    menu_admin()
  elif usn == "customer" and pw == "customer":
    menu_customer()
  elif usn == "produsen" and pw == "produsen":
    menu_produsen()
  else:
    clear_terminal()
    gambar()
    print()
    print()  
    print("=== INPUTAN TIDAK VALID ===")
    print("=== COBA LAGI ===")
    print()
    login()

# BIKIN AKUN BARU
def register():
    try: 
      print("1. Admin")
      print("2. Customer")
      print("3. Produsen")
      pilih = input("Pilih Akun Role yang ingin anda buat 1/2/3: ")
      if pilih == "1":
        data_admin()
      elif pilih == "2": 
        data_customer()
      elif pilih == "3":
        data_produsen()
      else :
        clear_terminal()
        gambar()
        print()
        print()
        print("=== INPUT TIDAK VALID COBA LAGI ===")
        print()
        register()
      connect_db()
      insert_query = sql.SQL("INSERT INTO users (username, password) VALUES (%s, %s)")
      record_to_insert = (usn, pw)
      commit_db(insert_query, record_to_insert)
      close_db()
    except Exception as e :
      print(f"Terjadi Error: {e}")
        
def data_admin():
    try:
      print()
      nama = input("Masukkan Nama: ")
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        print('Username tersimpan')
        print()
      else :
        clear_terminal()
        print("username harus lebih dari 8")
        print()
        data_admin()

      pw = input("Masukkan Password:  ")
      if len(pw) > 8 :
        print('Password tersimpan')
        print()
      else :
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        print()
        data_admin()

      no_telp = input("Masukkan No. Telepon: ")
      if no_telp .isdigit() and len(no_telp) >= 10 :
        print('No. Telepon tersimpan')
        print()
      if no_telp in data_admin:
        clear_terminal()
        print("No. Telepon sudah terdaftar. Silahkan Mulai Kembali")
        print()
      else :
        clear_terminal()
        print("No. Telepon harus berupa angka dan minimal 10 digit. Silahkan Mulai Kembali")
        print()
    except Exception as e :
        print(f"Terjadi Error: {e}")

    connection, cursor = connect_db()

    query = """
        INSERT INTO users (nama, username, password, no_telp)
         VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (nama, usn, pw, no_telp))
    connection.commit()

    gambar()
    print()
    print()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    print()
    print()
    dashboard()

def data_customer():
    try:
      print()
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        print('Username tersimpan')
        print()
      else :
        clear_terminal()
        print("username harus lebih dari 8")
        print()
        data_customer()

      pw = input("Masukkan Password:  ")
      if len(pw) > 8 :
        print('Password tersimpan')
        print()
      else :
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        print()
        data_customer()
    except Exception as e :
      print(f"Terjadi Error: {e}")
    gambar()
    print()
    print()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    print()
    print()
    dashboard()
    dashboard()

def data_produsen():
    try:
      print()
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        print('Username tersimpan')
        print()
      else :
        clear_terminal()
        print("username harus lebih dari 8")
        print()
        data_produsen()

      pw = input("Masukkan Password:  ")
      if len(pw) > 8 :
        print('Password tersimpan')
        print()
      else :
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        print()
        data_produsen()
    except Exception as e :
      print(f"Terjadi Error: {e}")
    gambar()
    print()
    print()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    print()
    print()
    dashboard()


gambar()
print("=== WELCOME TO OUR PLATFROM ===")
print()
print()
dashboard()





