import psycopg2
from psycopg2 import Error, sql
import os

def connect_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="langgeng847",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="Seedbridge")
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Gagal terhubung ke database", error)
        return None, None

def clear_terminal():
    os.system('cls')

def kembali():
    inputan_kembali = input('Tekan enter untuk kembali...')
    if inputan_kembali == '':
        clear_terminal()
    else:
        kembali()

# FITUR CUSTOMER
def Katalog_Benih(id_user):
    connection, cursor = connect_db()
    clear_terminal()
    print()
    print('1. Tampilkan semua Katalog Menu')
    print()
    print("  Filter Berdasarkan Kategori ")
    print("2. Harga Terendah")
    print("3. Harga Tertinggi")
    print("4. Stok Tersedia")
    print("5. Kembali ke Menu Customer")
    print()
    pilih = input('Pilih Menu anda 1/2/3/4/5/6: ')
    
    QUERY_BASE = """
        SELECT
        b.id_benih, b.nama_benih, k.nama_kategori, b.harga, b.kadaluarsa,
        SUM(r.jumlah_produksi) as stok    
        FROM benih b
        JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
        LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
        GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, b.kadaluarsa 
    """
    
    try: 
        if pilih == '1':
            query = QUERY_BASE
        elif pilih == "2":
            query = QUERY_BASE + " ORDER BY b.harga ASC"    
        elif pilih == "3":
            query = QUERY_BASE + " ORDER BY b.harga DESC"
        elif pilih == "4":
            query =  """
            SELECT
            b.id_benih, b.nama_benih, k.nama_kategori, b.harga, b.kadaluarsa,
            SUM(r.jumlah_produksi) as stok    
            FROM benih b
            JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
            LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
            GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, b.kadaluarsa 
            HAVING SUM(r.jumlah_produksi) > 0 
            ORDER BY b.nama_benih ASC
        """
        elif pilih == "5":
            clear_terminal()
            return menu_customer(id_user)
        else:
            print("Pilihan tidak valid.")
            return Katalog_Benih(id_user)

        if pilih in ['1', '2', '3', '4']:
            cursor.execute(query)
            data = cursor.fetchall()
        else:
            data = []

        clear_terminal()
        print("\n" + "="*75)
        print("                   🌱 KATALOG BENIH 🌱")
        print("="*75)
        print("="*75)
        print("     Gunakan ID Benih untuk menambahkan ke keranjang belanja Anda.")
        print("="*75)

        if not data:
            if pilih in ['1', '2', '3', '4']:
                print("Belum ada benih yang tersedia.")
            
            print("="*75 + "\n")
            return menu_customer(id_user)
            
        kategori_sekarang = None

        for row in data:
            id_benih, nama_benih, nama_kategori, harga, kadaluarsa, stok = row

            if nama_kategori != kategori_sekarang:
                kategori_sekarang = nama_kategori
                print(f"\n📂 Kategori: {nama_kategori}")
                print("-"*75)
                print(f"{'ID Benih':^10} {'Nama Benih':^25} {'Harga':^10} {'Tanggal Kadaluarsa':^20} {'Stok':^7}")
                print("-"*75)
            
            if kadaluarsa is not None:
                tanggal_str = kadaluarsa.strftime("%Y-%m-%d")
            else:
                tanggal_str = "N/A"
                
            stok_display = stok if stok is not None else 0
            
            id_benih_display = id_benih if id_benih is not None else ""
            nama_benih_display = nama_benih if nama_benih is not None else ""
            harga_display = harga if harga is not None else ""

            print(f"{id_benih_display:^10} {nama_benih_display:^25} {harga_display:^10} {tanggal_str:^20} {stok_display:^7}")
            
            stok = stok_display
            
            # if stok > 15:
            #     status_stok = f"{stok} tersedia"
            # elif 1 <= stok <= 15:
            #     status_stok = f"{stok} hampir habis"
            # else:
            #     status_stok = "Habis"
            
            # print(f"   Status: {status_stok}")
        print()
        kelas = input('pilih 1 untuk kembali dan 2 unutk pilih benih: ')
        if kelas == '1':
          clear_terminal()
          Katalog_Benih(id_user)
        elif kelas == '2':
          connection, cursor = connect_db()
          aku = input('masukkan id benih yg mau dibeli: ')
          kmu = input('masukkan jumlah benih yg dibeli: ')

          sql_pesanan = """
                        INSERT INTO pesanan (tanggal_pesanan, id_user)
                        VALUES (NOW(), %s);
                        """
          data_pesan = (id_user,)
          cursor.execute(sql_pesanan, data_pesan)

          cursor.execute("SELECT LAST_INSERT_ID();")
          idbaru = cursor.fetchone()[0]

          sql_detail = """
                        INSERT INTO detail_pesanan (id_pesanan, id_benih, quantity)
                        VALUES (%s, %s, %s)
                        """
          data_detail = (idbaru, aku, kmu) 
          cursor.execute(sql_detail, data_detail)

          connection.commit()  

    except Exception as e :
        print(f"Terjadi Error: {e}")
        print()
        print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
        print()
        menu_customer(id_user)
        print()
    finally:
        commit_db(connection, cursor)

def Keranjang_Belanja(id_user):
    connection, cursor = connect_db()
    print()
    print('1. Tampilkan Keranjang Belanja')
    print('2. Kembali Menu Customer')
    pilih = input('Pilih Menu anda 1/2: ')
    try:
      if pilih == '1':
            clear_terminal()
            print("=== WELCOME TO KERANJANG BELANJA ===")
            query = """
                SELECT b.nama_benih, b.harga, d.quantity, (b.harga * d.quantity) AS total_harga
                FROM detail_pesanan d
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE b.id_user = %s
            """
            cursor.execute(query, (id_user,))
            results = cursor.fetchall()

            if not results:
                print()
                print("Keranjang belanja Anda kosong.")
                return menu_customer(id_user)
    
            for row in results:
                print("================          Detail Keranjang Belanja Anda           ================")
                print(f"Nama Benih   : {row[0]}, harga: {row[1]}, Jumlah: {row[2]}, Total Harga: {row[3]}")
                print("==================================================================================")   
      elif pilih == '2':
        clear_terminal()
        menu_customer(id_user)
      else :
        clear_terminal()
        print('=== PILIHAN TIDAK VALID ===')
        print()
        menu_customer(id_user)
    except Exception as e :
      print(f"Terjadi Error: {e}")
    finally:
      commit_db(connection, cursor)
      print()
      print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
      print()
      menu_customer(id_user)
        
def Checkout_Belanja():
    try:
      print()
      print()
      print("=== WELCOME TO CHECKOUT BELANJA ===")
    except Exception as e :
      print(f"Terjadi Error: {e}")
    print()
    print()

def update_stok(id_pesanan):
    connection, cursor = connect_db()
    try:
        query_select = """
            SELECT id_benih, quantity
            FROM detail_pesanan
            WHERE id_pesanan = %s
        """
        cursor.execute(query_select, (id_pesanan,))
        pesanan = cursor.fetchall()

        for id_benih, qty in pesanan:
            update_stok = """
                UPDATE riwayat_produksi
                SET jumlah_produksi = jumlah_produksi - %s
                WHERE id_benih = %s
            """
            cursor.execute(update_stok, (qty, id_benih))

        commit_db(connection, cursor)
        print("Stok berhasil diperbarui!")

    except Exception as e:
        print(f"Gagal memperbarui stok: {e}")

    finally:
        connection.close()
 
def Transaksi(id_user):
    connection, cursor = connect_db()
    print()
    clear_terminal()
    print('1. Tampilkan Fitur Transaksi')
    print('2. Kembali Menu Admin')
    pilih = input('Pilih Menu anda 1/2: ')
    try:
      if pilih == '1':
          query = """
          SELECT t.id_transaksi, t.metode_pembayaran, t.status_transaksi, d.quantity*b.harga as Total_bayar
          FROM transaksi t
		      JOIN detail_pesanan d on d.id_pesanan = t.id_pesanan
		      JOIN benih b on b.id_benih = b.id_benih
          WHERE id_user = %s
          """
          cursor.execute(query, (id_user,))
          result = cursor.fetchone()

          if not result:
            print()
            print("Tidak ada transaksi ditemukan.")
            return menu_customer(id_user)

          id_transaksi, total_bayar, metode_pembayaran, status_transaksi = result
          clear_terminal()

          print("\n" + "="*50)
          print("               💰 DETAIL TRANSAKSI 💰")
          print("="*50)
          print(f"ID Transaksi     :     {id_transaksi}")
          print(f"Total Bayar      :      {total_bayar}")
          print(f"Metode Pembayaran:{metode_pembayaran}")
          print(f"Status           : {status_transaksi}")
          print("="*50 + "\n")
          print("Terima kasih telah berbelanja di SeedBridge!")
          print("="*50 + "\n")
      elif pilih == '2':
        clear_terminal()
        menu_customer(id_user)
      else : 
        clear_terminal()
        print('=== PILIHAN TIDAK VALID ===')
        print()
        menu_admin(id_user)
    except Exception as e :
        print(f"Terjadi Error: {e}")
    finally:
          commit_db(connection, cursor)
    print()
    print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
    print()
    menu_admin(id_user)

# FITUR ADMIN
def generate_laporan(id_user):
    connect_db()
    connection, cursor = connect_db()
    clear_terminal()
    print("=== MENU LAPORAN ===")
    print('1. Tampilkan seluruh Laporan')
    print('2. Tampilkan laporan berdasarkan transaksi yang selesai')
    print('3. Tampilkan laporan berdasarkan 3 bulan terakhir')
    print('4. Kembali')
    print()
    pilih = input('Masukkan menu yang ingin ditampilkan (1/2/3/4): ')
    try:
      if pilih == '1':
          print("\n" + "="*70)
          query = '''
                SELECT t.tanggal_transaksi, t.status_transaksi, t.metode_pembayaran, b.nama_benih
                FROM transaksi t
                JOIN detail_pesanan d ON d.id_pesanan = t.id_pesanan
                JOIN benih b ON d.id_benih = b.id_benih
                ORDER BY t.tanggal_transaksi DESC
            '''
      elif pilih == '2':
            query = '''
                SELECT t.tanggal_transaksi, t.status_transaksi, t.metode_pembayaran, STRING_AGG(b.nama_benih, ', ')
                FROM transaksi t
                JOIN detail_pesanan d ON t.id_pesanan = d.id_pesanan
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE t.status_transaksi = 'selesai'
                GROUP BY t.id_transaksi
            '''
      elif pilih == '3':
            query = '''
                SELECT t.tanggal_transaksi, t.status_transaksi, t.metode_pembayaran, b.nama_benih
                FROM transaksi t
                JOIN detail_pesanan d ON d.id_pesanan = t.id_pesanan
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE t.tanggal_transaksi >= CURRENT_DATE - INTERVAL '3 months'
                ORDER BY t.tanggal_transaksi DESC
            '''
      elif pilih == '4' :
        clear_terminal()
        menu_admin(id_user)
      else :
        print('=== PILIHAN TIDAK VALID ===')
        generate_laporan(id_user)
      cursor.execute(query)
      hasil = cursor.fetchall()
      print("\n=== HASIL LAPORAN ===\n")
      if not hasil:
        print("Tidak ada data yang ditemukan.\n")
      else:
        for row in hasil:
           print(f"Tanggal      : {row[0]}")
           print(f"Status       : {row[1]}")
           print(f"Pembayaran   : {row[2]}")
           print(f"Benih        : {row[3]}")
           print("-" * 40)
      print()
      input("Tekan enter untuk kembali....")
      menu_admin(id_user)
    except Exception as e:
        print(f"Terjadi Error: {e}")
    print()
    print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
    print()
    menu_admin(id_user)

def update_status_pengiriman(id_user):
    connection, cursor = connect_db()
    try:
        print()
        print("=== MONITORING & UPDATE STATUS PENGIRIMAN ===")
        print()
        print("Daftar Transaksi")
        query = """
            SELECT t.id_transaksi, t.tanggal_transaksi, STRING_AGG(b.nama_benih, ', '), SUM(d.quantity), t.status_transaksi
            FROM transaksi t
            JOIN detail_pesanan d ON t.id_pesanan = d.id_pesanan
            JOIN benih b ON d.id_benih = b.id_benih
            GROUP BY t.id_transaksi, t.tanggal_transaksi, b.nama_benih, d.quantity, t.status_transaksi
            ORDER BY t.id_transaksi
        """
        cursor.execute(query)
        results = cursor.fetchall()
        print()
        if not results:
          print("Belum ada transaksi")
        else:
          print("="*70)
          for r in results:
            print(f"ID Transaksi : {r[0]}")
            print(f"Tanggal      : {r[1]}")
            print(f"Nama Benih   : {r[2]}")
            print(f"Quantity     : {r[3]}")
            print(f"Status       : {r[4]}")
            print("-"*70)
        print("="*70)
        print()
        print('1. Update Status Pesanan')
        print('2. Kembali')
        pilih = input('Pilih Menu: ')
        if pilih == '1':
          id_transaksi = input('Masukkan ID transaksi yang akan di update: ').strip()
          if not id_transaksi:
            print("\n=== ID Tidak Boleh Kosong! ===")
            input("Tekan enter untuk kembali...")
            return update_status_pengiriman(id_user)
          if not id_transaksi.isdigit():
            print("\n=== ID Transaksi Harus Berupa Angka! ===")
            input("Enter untuk kembali...")
            return update_status_pengiriman(id_user)
          # MENGECEK ID TRANSAKSI APAKAH ADA DI DATABASE
          cursor.execute("SELECT status_transaksi FROM transaksi WHERE id_transaksi = %s", (id_transaksi, ))
          data = cursor.fetchone()
          if not data:
            print("\n=== ERROR: ID TRANSAKSI TIDAK DITEMUKAN ===")
            input("Tekan enter untuk kembali...")
            return update_status_pengiriman(id_user)
          # TIDAK BOLEH UPDATE JIKA STATUS SUDAH SELESAI
          status_sekarang = data[0]
          if status_sekarang == 'selesai':
            print("\n=== TRANSAKSI SUDAH SELESAI & TIDAK DAPAT DIUBAH ===")
            input("Tekan enter untuk kembali...")
            return update_status_pengiriman(id_user)

          print(f"status saat ini: {status_sekarang}")
          status_baru = input('Pilih status (dikemas/dikirim/diterima/selesai): ').lower().strip()
          status_valid = ['dikemas', 'dikirim', 'diterima', 'selesai']

          # VALIDASI STATUS INPUT
          if status_baru not in status_valid:
            print("\n=== STATUS TIDAK VALID! ===")
            input("Tekan enter untuk kembali...")
            return update_status_pengiriman(id_user)
          # TIDAK BOLEH UPDATE STATUS YANG SAMA
          if status_baru == status_sekarang:
            print("\n=== STATUS SUDAH DALAM KONDISI TERSEBUT ===")
            input("Enter untuk kembali...")
            return update_status_pengiriman(id_user)

          # URUTAN STATUS HARUS MAJU
          tahap = {
            'dikemas': 1,
            'dikirim': 2,
            'diterima': 3,
            'selesai': 4
          }

          if tahap[status_baru] < tahap[status_sekarang]:
            print("\n=== STATUS TIDAK BOLEH MUNDUR ===")
            input("Enter untuk kembali...")
            return update_status_pengiriman(id_user)
          # UPDATE STATUS  
          cursor.execute("""
              UPDATE transaksi
              SET status_transaksi = %s:: enum_transaksi
              WHERE id_transaksi = %s
          """, (status_baru, id_transaksi))
          connection.commit()

          print()
          print("=== STATUS BERHASIL DIUPDATE ===")
          print("Tekan enter untuk kembali...")
          return update_status_pengiriman(id_user)
          
        elif pilih == '2':
            clear_terminal()
            menu_admin(id_user)
        else :
          print('=== PILIHAN TIDAK VALID ===')
          return
    except Exception as e:
        print(f"Terjadi Error: {e}")
    finally:
      if connection:
        cursor.close()
        connection.close()
    print()
    print()
    clear_terminal()
    menu_admin(id_user)
  
# FITUR PRODUSEN
def cek_stok():
  try:
    print()
    print()
    print("=== CEK STOK HABIS/KADALUARSA ===")
    print()
    print("1. Tampilkan Stok")
    print("2. Kembali")
    pilih = input('Pilih Menu 1/2 : ')
    if pilih == '1':
      print()
    elif pilih == '2':
      clear_terminal()
      menu_admin()
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()

def update_benih():
  try:
    print()
    print()
    print("=== WELCOME TO MENU UPDATE BENIH ===")
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()
  
def lihat_daftar_order():
  try:
    print()
    print()
    print("=== DAFTAR ORDER ===")
    print()
    print("1. Tampilkan Daftar Order")
    print("2. Kembali")
    pilih = input('Pilih Menu 1/2 : ')
    if pilih == '1':
      print()
    elif pilih == '2':
      clear_terminal()
      menu_admin()
  except Exception as e :
    print(f"Terjadi Error: {e}")
  print()
  print()

# MENU TIAP ROLE
def menu_admin(id_user):
    print()
    print("=== WELCOME ADMIN ===")
    print()
    print("1. Tampilkan Laporan")
    print("2. Monitoring & Update Status Pengiriman")
    print("3. Keluar")
    try: 
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == '1':
            generate_laporan(id_user)
        elif pilihan == '2':
            update_status_pengiriman(id_user)
        elif pilihan == '3':
            clear_terminal()
            print("Keluar dari menu admin.")
            print()
            gambar()
            dashboard()
        else:
            print()
            clear_terminal()
            print("Pilihan tidak valid. Silakan coba lagi.")
            menu_admin(id_user)
    except Exception as e :
     print(f"Terjadi Error: {e}")
     clear_terminal()
     menu_admin(id_user)
  
def menu_customer(id_user):
    print()
    print("=== WELCOME CUSTOMER ===")
    print()
    try:
        print("1. Katalog Benih")
        print("2. Keranjang Belanja")
        print("3. Checkout Belanja")
        print("4. Status Transaksi")
        print("5. Riwayat Transaksi")
        print("6. Keluar")
        print()
        pilih = input("Pilih Menu Customer: ")

        if pilih == "1":
            Katalog_Benih()
        elif pilih == "2":
            Keranjang_Belanja(id_user)
        elif pilih == "3":
            Checkout_Belanja(id_user)
        elif pilih == "4":
            Transaksi(id_user)
        elif pilih == "5":
            Riwayat_Transaksi(id_user)
        elif pilih == "6":
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
            menu_customer(id_user)
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
      print("1. Customer")
      print("2. Produsen")
      pilih = input("Pilih Akun Role yang ingin anda buat 1/2: ")
      if pilih == "1": 
        data_customer()
      elif pilih == "2":
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
        
def data_admin(role):
    try:
      print()
      nama = input("Masukkan Nama: ")
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        print('Username tersimpan')
      cursor.execute("SELECT username FROM users WHERE username = %s", (usn,))
      if cursor.fetchone():
        clear_terminal()
        print("Username sudah terdaftar. Silahkan Mulai Kembali")
        print()
      else :
        clear_terminal()
        print("username harus lebih dari 8")
        print()
        data_admin(role)

      pw = input("Masukkan Password: ")
      if len(pw) > 8 :
        print('Password tersimpan')
        print()
      else :
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        print()
        data_admin(role)
      no_telp = input("Masukkan No. Telepon: ")
      if no_telp .isdigit() and len(no_telp) >= 10 :
        print('No. Telepon tersimpan')
        data_admin(role)
      cursor.execute("SELECT no_telp FROM users WHERE no_telp = %s", (no_telp,))
      if ncursor.fetchone(): 
        clear_terminal()
        print("No. Telepon sudah terdaftar. Silahkan Mulai Kembali")
      else :
        clear_terminal()
        print("No. Telepon harus berupa angka dan minimal 10 digit. Silahkan Mulai Kembali")
    except Exception as e :
        print(f"Terjadi Error: {e}")

    connection, cursor = connect_db()

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

def data_customer(role):
    connection, cursor = connect_db()
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
print("=== WELCOME TO OUR PLATFORM ===")
print()
print()
dashboard()

