import pandas as pd
import datetime as dt
import os
import prettytable

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
    connection, cursor = connect_db()

    query = """
        SELECT
            p.id_benih,
            p.nama_benih,   
            k.nama_kategori,
            p.harga,
            p.stok,
            p.tanggal_kadaluarsa    
        FROM benih p
        JOIN kategori_benih k ON p.id_kategori = k.id_kategori
        ORDER BY k.nama_kategori, p.nama_benih
    """
    cursor.execute(query)
    data = cursor.fetchall()

    try:
        print("\n" + "="*75)
        print("                    🌱 KATALOG BENIH 🌱")
        print("="*75)
    except Exception as e:
        print(f"Terjadi Error: {e}")
        return

    if not data:
        print("Belum ada benih yang tersedia.")
        print("="*75)
        return
    kategori_sekarang = None

    for row in data:
        id_benih, nama_benih, nama_kategori, harga, stok, tanggal_kadaluarsa = row

        if nama_kategori != kategori_sekarang:
            kategori_sekarang = nama_kategori
            print(f"\n📂 Kategori: {nama_kategori}")
            print("-"*75)
            print(f"{'ID Benih':<5} {'Nama Benih':<25} {'Harga':<10} {'Stok':<10} {'Tanggal Kadaluarsa':<10}")
            print("-"*75)

        if stok > 15:
            status_stok = f"{stok} tersedia"
        elif 1 <= stok <= 15:
            status_stok = f"{stok} hampir habis"
        else:
            status_stok = "Habis"

        print(f"{id_benih:<5} {nama_benih:<25} {harga:<10} {status_stok:<10} {tanggal_kadaluarsa:<10}")
        print("="*75)
        print("      Gunakan ID Benih untuk menambahkan ke keranjang belanja Anda.")
        print("="*75)

        print(f"ID Benih          :          {id_benih}")
        print(f"Nama Benih        :        {nama_benih}")
        print(f"Harga             :             {harga}")
        print(f"Stok              :              {stok}")
        print(f"Tanggal Kadaluarsa:{tanggal_kadaluarsa}")   
        print("----------------------------------------")

    print()
    print()

def Filter_Benih():
    connection, cursor = connect_db()
    try:
      print("=== WELCOME TO FILTER BENIH ===")
      
      print("Filter berdasarkan kategori:")
      print("1. Harga Terendah")
      print("2. Harga Tertinggi")
      print("3. Stok Tersedia")
      print("4. Semua")
      print("5. Kembali ke Menu Customer")
      pilih = input("Pilih kategori (1/2/3/4/5): ")

      if pilih == "1":
        query = "SELECT * FROM benih ORDER BY harga ASC"    
      elif pilih == "2":
        query = "SELECT * FROM benih ORDER BY harga DESC"
      elif pilih == "3":
        query = "SELECT * FROM benih WHERE stok > 0"
      elif pilih == "4":
        query = "SELECT * FROM benih"
      elif pilih == "5":
        clear_terminal()
        menu_customer()
        return
      else:
        clear_terminal()
        print("=== PILIHAN TIDAK VALID ===")
        print()
        Filter_Benih()
        return
      cursor.execute(query)
      data = cursor.fetchall()

      if not data:
        print("Tidak ada benih yang sesuai dengan filter.")
        return

      print("\n===== Hasil Filter Benih =====")
      for row in data:
          print(f"ID Benih:          {row[0]}")
          print(f"Nama Benih:        {row[1]}")
          print(f"Kategori:          {row[2]}")
          print(f"Harga:             {row[3]}")
          print(f"Stok:              {row[4]}")
          print(f"Tanggal Kadaluarsa:{row[5]}")   
          print("----------------------------")

    except Exception as e :
      print(f"Terjadi Error: {e}")
        
def Keranjang_Belanja():
    connection, cursor = connect_db()
    try:
      print("=== WELCOME TO KERANJANG BELANJA ===")

      query = """
          SELECT b.nama_benih, b.harga, kp.quantity, (b.harga * kp.quantity) AS total_harga
          FROM keranjang_pesanan kb     
          JOIN benih b ON kp.id_benih = b.id_benih
          WHERE kp.id_user = %s
      """
      cursor.execute(query, (id_user,))
      results = cursor.fetchall()

      if not results:
          print("Keranjang belanja Anda kosong.")
          return
      for row in results:
          print("================          Detail Keranjang Belanja Anda           ================")
          print(f"Nama Benih   : {row[0]}, harga: {row[1]}, Jumlah: {row[2]}, Total Harga: {row[3]}")
          print("==================================================================================")   
    except Exception as e :
      print(f"Terjadi Error: {e}")

def Checkout_Belanja():
    try:
      print()
      print()
      print("=== WELCOME TO CHECKOUT BELANJA ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def Transaksi():
    connect_db()
    try:
      print("\n" + "="*50)
      print("                💰 DETAIL TRANSAKSI 💰")
      print("="*50)
      print(f"ID Transaksi     :      {id_transaksi}")
      print(f"Total Bayar      :       {total_bayar}")
      print(f"Metode Pembayaran: {metode_pembayaran}")
      print(f"Status           :            {status}")
      print("="*50 + "\n")
      print("Terima kasih telah berbelanja di SeedBridge!")
      print("="*50 + "\n")

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
    connect_db()
    try:
        print("\n" + "="*70)
        print("               📊 LAPORAN PENJUALAN SEEDBRIDGE 📊")
        print("="*70)
        print("")
    except Exception as e:
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

def data_customer(role):
    connection, cursor = connect_db()
    while True:
        try:
            print()
            nama = input("Masukkan Nama: ")
            usn = input("Masukkan Username: ")
            if len(usn) > 8:
                print('Username tersimpan')
                print()
            else:
                clear_terminal()
                print("username harus lebih dari 8")
                print()
                continue

            cursor.execute("SELECT username FROM users WHERE username = %s", (usn,))
            if cursor.fetchone():
                clear_terminal()
                print("Username sudah terdaftar, gunakan yang lain.")
                continue

            pw = input("Masukkan Password:  ")
            if len(pw) > 8:
                print('Password tersimpan')
                print()
            else:
                clear_terminal()
                print("Password harus lebih dari 8. Silahkan Mulai Kembali")
                print()
                continue

            no_telp = input("Masukkan No. Telepon: ")
            if no_telp.isdigit() and len(no_telp) >= 10:
                print('No. Telepon tersimpan')
                print()
            else:
                clear_terminal()
                print("No. Telepon harus berupa angka dan minimal 10 digit. Silahkan Mulai Kembali")
                continue

            cursor.execute("SELECT no_telp FROM users WHERE no_telp = %s", (no_telp,))
            if cursor.fetchone():
                clear_terminal()
                print("No. Telepon sudah terdaftar. Silahkan Mulai Kembali")
                continue

            break
        except Exception as e:
            print(f"Terjadi Error: {e}")

    query = """
        INSERT INTO users (nama, username, password, no_telp, id_role)
         VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nama, usn, pw, no_telp, role))
    connection.commit()

    cursor.execute("SELECT id_user FROM users WHERE username = %s", (usn,))
    id_user = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO keranjang_pesanan (id_user, quantity))
        VALUES (%s, 0)
    """, id_user)
    connnection.commit()
    gambar()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    dashboard()

def data_produsen(role):
    connection, cursor = connect_db()
    try:
      print()
      nama = input("Masukkan Nama: ")
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        print('Username tersimpan')
        print()
      elif usn in data_produsen:
        clear_terminal()
        print("Username sudah terdaftar. Silahkan Mulai Kembali")
        print()
      else :
        clear_terminal()
        print("username harus lebih dari 8")
        print()
        data_produsen(role)

      pw = input("Masukkan Password:  ")
      if len(pw) > 8 :
        print('Password tersimpan')
        print()
      else :
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        print()
        data_produsen(role)

      no_telp = input("Masukkan No. Telepon: ")
      if no_telp .isdigit() and len(no_telp) >= 10 :
        print('No. Telepon tersimpan')
        print()
      cursor.execute("SELECT no_telp FROM users WHERE no_telp = %s", (no_telp,))
      if cursor.fetchone():
        clear_terminal()
        print("No. Telepon sudah terdaftar. Silahkan Mulai Kembali")
      else :
        clear_terminal()
        print("No. Telepon harus berupa angka dan minimal 10 digit. Silahkan Mulai Kembali")
        data_produsen(role)
    except Exception as e :
      print(f"Terjadi Error: {e}")

    query = """
        INSERT INTO users (nama, username, password, no_telp, id_role)
         VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nama, usn, pw, no_telp, role))
    connection.commit()

    cursor.execute("SELECT id_user FROM users WHERE username = %s", (usn,))
    id_user = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO keranjang_pesanan (id_user, quantity))
        VALUES (%s, 0)
    """, id_user)
    connnection.commit()

    gambar()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    dashboard()

gambar()
print("=== WELCOME TO OUR PLATFROM ===")
print()
print()
dashboard()
