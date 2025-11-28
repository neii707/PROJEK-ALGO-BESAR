import psycopg2
from psycopg2 import Error,  sql
import os

def connect_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="langgeng847",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="Project")
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        return None, None
def commit_db(connection, cursor):
    try:
        connection.commit()
        affected = cursor.rowcount  
        return affected > 0         
    except Exception as e:
        print("Error saat commit:", e)
        connection.rollback()
        return False
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass
def clear_terminal():
    os.system('cls')
# FITUR CUSTOMER
# def Katalog_Benih(id_user):
#     connection, cursor = connect_db()
#     clear_terminal()
#     print('1. Tampilkan semua Katalog Menu')
#     print()
#     print("  Filter Berdasarkan Kategori ")
#     print("2. Harga Terendah")
#     print("3. Harga Tertinggi")
#     print("4. Stok Tersedia")
#     print("5. Kembali ke Menu Customer")
#     print()
#     pilih = input('Pilih Menu anda 1/2/3/4/5: ')
    
#     QUERY_BASE = """
#         SELECT b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa, SUM(r.jumlah_produksi) as stok    
#         FROM benih b
#         JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
#         LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
#         GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa 
#         HAVING SUM(r.jumlah_produksi) > 0 
#     """
#     try: 
#         if pilih == '1':
#             query = QUERY_BASE + "ORDER BY k.nama_kategori ASC, b.nama_benih ASC"
#         elif pilih == "2":
#             query = QUERY_BASE + " ORDER BY b.harga ASC"    
#         elif pilih == "3":
#             query = QUERY_BASE + " ORDER BY b.harga DESC"
#         elif pilih == "4":
#             query =  """
#             SELECT b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa, SUM(r.jumlah_produksi) as stok    
#             FROM benih b
#             JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
#             LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
#             GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa 
#             HAVING SUM(r.jumlah_produksi) > 0 
#             ORDER BY k.nama_kategori ASC, b.nama_benih ASC
#         """
#         elif pilih == "5":
#             clear_terminal()
#             return menu_customer(id_user)
#         else:
#             print("Pilihan tidak valid.")
#             return Katalog_Benih(id_user)
#         cursor.execute(query)
#         data = cursor.fetchall()
        
#         clear_terminal()
#         print("\n" + "="*75)
#         print("                          🌱 KATALOG BENIH 🌱")
#         print("="*75)
#         print("="*75)
#         print("      Gunakan ID Benih untuk menambahkan ke keranjang belanja Anda.")
#         print("="*75)
#         if not data:
#             if pilih in ['1', '2', '3', '4']:
#                 print("Belum ada benih yang tersedia.")
            
#             print("="*75 + "\n")
#             return menu_customer(id_user)
        
#         kategori= {}
#         for row in data:
#             id_benih, nama_benih, nama_kategori, harga, kadaluarsa, stok = row
#             if nama_kategori not in kategori:
#                 kategori [nama_kategori] = []
#             kategori[nama_kategori].append(row)
#         for kategori, items in kategori.items():
#                 print(f"\n📂 Kategori: {kategori}")
#                 print("-"*75)
#                 print(f"{'ID Benih':^10} {'Nama Benih':^25} {'Harga':^10} {'Tanggal Kadaluarsa':^20} {'Stok':^7}")
#                 print("-"*75)
#                 for id_benih, nama_benih, kategori, harga, kadaluarsa, stok in items:
#                     tanggal_str = kadaluarsa.strftime("%Y-%m-%d") if kadaluarsa else "N/A"
#                     print(f"{id_benih:^10} {nama_benih:^25} {harga:^10} {tanggal_str:^20} {stok:^7}")

#         stok_display = stok if stok is not None else 0
#         id_benih_display = id_benih if id_benih is not None else ""
#         nama_benih_display = nama_benih if nama_benih is not None else ""
#         harga_display = harga if harga is not None else ""
#         print(f"{id_benih_display:^10} {nama_benih_display:^25} {harga_display:^10} {tanggal_str:^20} {stok_display:^7}")
#         stok = stok_display
            
#         print()
#         kelas = input('pilih 1 untuk kembali dan 2 untuk pilih benih: ')
#         if kelas == '1':
#           clear_terminal()
#           Katalog_Benih(id_user)
#         elif kelas == '2':
#           connection, cursor = connect_db()
#           aku = input('masukkan id benih yg mau dibeli: ')
#           kmu = input('masukkan jumlah benih yg dibeli: ')

#           sql_get_keranjang = "SELECT id_keranjang FROM users WHERE id_user = %s"
#           cursor.execute(sql_get_keranjang, (id_user,))
#           result = cursor.fetchone()

#           if result:
#             id_keranjang = result[0]

#           sql_detail = """
#                         INSERT INTO detail_keranjang (id_keranjang, id_benih, quantity)
#                         VALUES (%s, %s, %s)
#                         """
#           cursor.execute("SELECT id_keranjang FROM users WHERE id_user = %s", (id_user,))
#           keranjang = cursor.fetchone()                     
#           data_detail = (id_keranjang, aku, kmu) 
#           cursor.execute(sql_detail, data_detail)
#           connection.commit()  
#           print()
#           print()
#           print()
          
#           pergi = input('Benih sudah dimasukkan ke keranjang silahkan tekan enter untuk pergi ke menu keranjang')
#           if pergi == '':
#             clear_terminal()
#             Keranjang_Belanja(id_user)
#           else :
#             clear_terminal()
#             print('PILIHAN TIDAK VALID KEMBALI KE MENU CUSTOMER')
#             menu_customer(id_user)
          
#     except Exception as e :
#         print(f"Terjadi Error: {e}")
#         print()
#         print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
#         print()
#         menu_customer(id_user)
#         print()
#     finally:
#         commit_db(connection, cursor)
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
    pilih = input('Pilih Menu anda 1/2/3/4/5: ')
    
    QUERY_BASE = """
        SELECT
        b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa,
        SUM(r.jumlah_produksi) as stok    
        FROM benih b
        JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
        LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
        GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa 
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
            b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa,
            SUM(r.jumlah_produksi) as stok    
            FROM benih b
            JOIN kategori_benih k ON b.id_kategori_benih = k.id_kategori_benih
            LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
            GROUP BY b.id_benih, b.nama_benih, k.nama_kategori, b.harga, r.tanggal_kadaluarsa 
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
            
        print()
        kelas = input('pilih 1 untuk kembali dan 2 untuk pilih benih: ')
        if kelas == '1':
          clear_terminal()
          Katalog_Benih(id_user)
        elif kelas == '2':
          connection, cursor = connect_db()
          aku = input('masukkan id benih yg mau dibeli: ')
          kmu = input('masukkan jumlah benih yg dibeli: ')
          
          if not aku or not kmu:
              print(" ID Benih dan Jumlah tidak boleh kosong!")
              print()
              menu_customer(id_user)
              
            
          try:
              id_benih_beli = int(aku)
              qty_dibeli = int(kmu) # Konversi jumlah yang dibeli ke integer
          except ValueError:
              print(" Input ID Benih dan Jumlah harus berupa angka yang valid!")
              print()
              menu_customer(id_user)

          if qty_dibeli <= 0:
                print(" Jumlah benih harus lebih dari nol!")
                balik = input('tekan enter untuk kembali ke katalog: ')
                if balik == '':
                  clear_terminal()
                  Katalog_Benih(id_user)
              
          sql_get_stok = """
                SELECT COALESCE(SUM(jumlah_produksi), 0)
                FROM riwayat_produksi
                WHERE id_benih = %s;
            """
          cursor.execute(sql_get_stok, (id_benih_beli,))
          stok_saat_ini = cursor.fetchone()[0]
          
          if stok_saat_ini <= 0:
                print(f"❌ Benih dengan ID {id_benih_beli} saat ini KOSONG (Stok: 0). Tidak bisa dibeli.")
                balik = input('tekan enter untuk kembali kek katalog: ')
                if balik == '':
                  clear_terminal()
                  Katalog_Benih(id_user)
              

          if stok_saat_ini < qty_dibeli: 
                print(f" Stok tidak mencukupi!")
                print(f"   Stok tersedia: {stok_saat_ini}, Anda mencoba membeli: {qty_dibeli}")
                balik = input('tekan enter untuk kembali kek katalog: ')
                if balik == '':
                  clear_terminal()
                  Katalog_Benih(id_user)

          sql_get_keranjang = "SELECT id_keranjang FROM users WHERE id_user = %s"
          cursor.execute(sql_get_keranjang, (id_user,))
          result = cursor.fetchone()
            

          if result:
            id_keranjang = result[0]
        #   else:
        #     # keranjang baru 
        #     sql_create_keranjang = """
        #     INSERT INTO users (id_user, status, created_at) 
        #     VALUES (%s, 'active', NOW()) 
        #     RETURNING id_keranjang
        #     """
        #     cursor.execute(sql_create_keranjang, (id_user,))
        #     id_keranjang = cursor.fetchone()[0]
        #     print(f"Keranjang baru dibuat: {id_keranjang}")

          sql_detail = """
                        INSERT INTO detail_keranjang (id_keranjang, id_benih, quantity)
                        VALUES (%s, %s, %s)
                        """
                        
          cursor.execute("SELECT id_keranjang FROM users WHERE id_user = %s", (id_user,))
          keranjang = cursor.fetchone()                
                        
          data_detail = (id_keranjang, aku, kmu) 
          cursor.execute(sql_detail, data_detail)
          connection.commit()  
          print()
          print()
          print()
          
          pergi = input('Benih sudah dimasukkan ke keranjang silahkan tekan enter untuk pergi ke menu keranjang')
          if pergi == '':
            commit_db(connection, cursor)
            clear_terminal()
            Keranjang_Belanja(id_user)
          else :
            clear_terminal()
            print('PILIHAN TIDAK VALID KEMBALI KE MENU CUSTOMER')
            menu_customer(id_user)
        else:
            clear_terminal()
            print('PILIHAN TIDAK VALID KEMBALI KE MENU CUSTOMER')
            menu_customer(id_user)

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
    id_pesanan_baru = None
    connection, cursor = connect_db()
    
    print()
    print('1. Tampilkan Keranjang Belanja')
    print('2. Kembali Menu Customer')
    pilih = input('Pilih Menu anda 1/2: ')
    try:
      if pilih == '1':
            clear_terminal()
            print("===============================               WELCOME TO KERANJANG               ===============================")
            print()

            cursor.execute("SELECT id_keranjang FROM users WHERE id_user = %s", (id_user,))
            result = cursor.fetchone()
            if not result:
                print("Keranjang tidak ditemukan.")
                return menu_customer(id_user)

            id_keranjang = result[0]
            query = """
                SELECT d.id_detail_keranjang, b.nama_benih, b.harga, d.quantity, (b.harga * d.quantity) AS total_harga
                FROM detail_keranjang d
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE d.id_keranjang = %s
                ORDER BY d.id_detail_keranjang 
            """
            cursor.execute(query, (id_keranjang,))
            results = cursor.fetchall()

            if not results:
                print()
                print("Keranjang belanja Anda kosong.")
                return menu_customer(id_user)
    
            for row in results:
                print("===============================          Detail Keranjang Belanja Anda           ===============================")
                print()
                print(f"ID DETAIL   : {row[0]}       Nama Benih   : {row[1]}     harga: {row[2]}    Jumlah: {row[3]}     Total Harga: {row[4]}")
                print()
                print("================================================================================================================")  
            print()
            keranjang = []
            total_semua = 0
            keranjang.append({
            'id_detail': row[0],
            'nama_benih': row[1],
            'harga': row[2],
            'jumlah': row[3],
            'total_harga': row[4]
              })
            total_semua +=row[4]
            print(f"{'TOTAL KERANJANG':<100} Rp {total_semua:>}")
            print("="*112)
            
            print("\nMasukkan ID DETAIL yang ingin dibeli (pisahkan dengan spasi):")
            try:
                pilihan = input(">>:  ").strip()
                if not pilihan:
                  print("Tidak ada item yang dipilih!")
                  return pilihan
            
                id_detail = [int(x.strip()) for x in pilihan.split()]
                dipilih = [item for item in keranjang if int(str(item['id_detail']).strip()) in id_detail]
                
                if not dipilih:
                    print("Tidak ada item yang valid dipilih!")
                    clear_terminal()
                    menu_customer(id_user)
                
                print(f"\n✅ {len(dipilih)} item dipilih untuk checkout!")
                print("\n" + "="*100)
                print(" " * 40 + "🛒 CHECKOUT")
                print("="*100)
                print(f"{'ID':<8} {'NAMA BENIH':<25} {'HARGA':<12} {'QTY':>4} {'SUB TOTAL':>15}")
                print("-" * 100)
                    
                total_bayar = 0
                for item in dipilih:
                    print(f"{item['id_detail']:<8} {item['nama_benih']:<25} Rp {item['harga']:>3} {item['jumlah']:>7}        Rp {item['total_harga']:>7}")
                    total_bayar += item['total_harga']
                    print()
                    print("-" * 100)
                    print(f"{'TOTAL YANG HARUS DIBAYAR':<58} Rp {total_bayar:>3}")
                    print("="*100)
                    
                    cursor.execute("SELECT id_keranjang FROM users WHERE id_user = %s", (id_user,))
                    keranjang = cursor.fetchone()
                    if not keranjang:
                        print(" Keranjang tidak ditemukan!")
                    
                    print("\n" + "="*50)
                    print("INFORMASI PENGIRIMAN & PEMBAYARAN")
                    print("="*50)
                    
                    metode_pembayaran = input("Metode Pembayaran tunai/non tunai): ").strip().lower()
                    
                    if not metode_pembayaran :
                        print(" Metode pembayaran wajib diisi!")
                        metode_pembayaran
                    elif metode_pembayaran != 'tunai' or 'non tunai':
                        print('PILIHAN TIDAK VALID')
                        Keranjang_Belanja(id_user)
                    
                    status_transaksi = 'dikemas'

                    konfir = input('Anda yakin ingin untuk Membeli item ini ? ya/tidak: ').strip().lower()
                    if konfir == 'ya':
                      id_pesanan = """
                                  INSERT INTO pesanan (tanggal_pesanan, id_user)
                                  VALUES (NOW(), %s)
                                  RETURNING id_pesanan;
                                  """
                      data_pesan = (id_user,)
                      cursor.execute(id_pesanan, data_pesan)
                    
                      result = cursor.fetchone()
                      id_pesanan_baru = result[0]
                      id_transaksi_baru = result[0]

                      list = [item['id_detail'] for item in dipilih]
                      for id_detail_keranjang in list:
                        info = """
                                          SELECT id_benih, quantity
                                          FROM detail_keranjang
                                          WHERE id_detail_keranjang = %s
                                          """
                        cursor.execute(info, (id_detail_keranjang,))
                        item_data = cursor.fetchone()
                        
                        if item_data:
                            id_benih_beli = item_data[0]
                            qty_dibeli = item_data[1]

                            sql_insert_transaki = """
                                                    INSERT INTO transaksi (id_transaksi, tanggal_transaksi, metode_pembayaran, status_transaksi, id_pesanan)
                                                    VALUES (%s, NOW(), %s, %s, %s)
                            """
                            cursor.execute(sql_insert_transaki, (id_transaksi_baru, metode_pembayaran, status_transaksi, id_pesanan_baru))

                            sql_insert_detail_pesanan = """
                                INSERT INTO detail_pesanan (id_pesanan, id_benih, quantity)
                                VALUES (%s, %s, %s);
                            """
                            cursor.execute(sql_insert_detail_pesanan, 
                                          (id_pesanan_baru, id_benih_beli, qty_dibeli))
            
                            sql_update_stok = """
                                              UPDATE riwayat_produksi
                                              SET jumlah_produksi = jumlah_produksi - %s
                                              WHERE id_benih = %s;
                                  """
                            cursor.execute(sql_update_stok, (qty_dibeli, id_benih_beli))

                      hold = ', '.join(['%s'] * len(id_detail))
                      sql_delete = f"""
                      DELETE FROM detail_keranjang
                      WHERE id_detail_keranjang IN ({hold});
                                  """
                      cursor.execute(sql_delete, tuple(id_detail))
                      
                      print()
                      print("="*50)
                      print("PEMBELIAN BERHASIL!")
                      print(f" No. Pesanan: #{id_pesanan_baru}")
                      print(f" Total: Rp {total_bayar}")
                      print("🛒 Keranjang sekarang KOSONG") 
                      print()
                      pergi = input('Silahkan tekan enter untuk pergi kembali ke menu customer')
                      if pergi == '':
                        commit_db(connection, cursor)
                        clear_terminal()
                        menu_customer(id_user)
                      else :
                        clear_terminal()
                        print('PILIHAN TIDAK VALID KEMBALI KE MENU CUSTOMER')
                        menu_customer(id_user)
                    else:
                        clear_terminal()
                        print('PILIHAN TIDAK VALID KEMBALI KE KERANJANG')
                        print()
                        Keranjang_Belanja(id_user)
            except ValueError:
                  print(" Input tidak valid! Harus angka.")
                  clear_terminal()
                  pilihan
    except Exception as e :
        print(f"Terjadi Error: {e}")
        print('=== DATA TIDAK VALID KEMBALI KE MENU ===')
        print()
        menu_customer(id_user)
    finally:
        commit_db(connection, cursor)
        print() 
def Riwayat_Transaksi(id_user):
    connect_db()
    connection, cursor = connect_db()
    print()
    print('1. Tampilkan Fitur Transaksi')
    print('2. Kembali Menu Customer')
    pilih = input('Pilih Menu anda 1/2: ')
    try:
      clear_terminal()
      if pilih == '1':
          # checkout detail = join
          query = """
                  SELECT t.tanggal_transaksi, b.nama_benih, d.quantity, d.quantity*b.harga AS Total_bayar,
                        k.nama, c.nama, s.nama
                  FROM transaksi t
                  JOIN detail_pesanan d ON d.id_pesanan = t.id_pesanan
                  JOIN pesanan p ON p.id_pesanan = d.id_pesanan
                  JOIN benih b ON b.id_benih = d.id_benih 
                  JOIN users u ON p.id_user = u.id_user  
                  JOIN alamat a ON u.id_user = a.id_user
                  JOIN desa s ON a.id_desa = s.id_desa
                  JOIN kecamatan c ON s.id_kecamatan = c.id_kecamatan
                  JOIN kabupaten k ON c.id_kabupaten = k.id_kabupaten
                  WHERE p.id_user = %s
                  ORDER BY t.tanggal_transaksi DESC, t.id_transaksi;
          """
          cursor.execute(query, (id_user,))
          results = cursor.fetchall()
          print()
          print("=== WELCOME TO RIWAYAT TRANSAKSI ===")
          print()
          if not results:
              print()
              print("Tidak ada riwayat transaksi.")
              print()
              menu_customer(id_user)
          else:
              for row in results:
                tanggal = str(row[0]) 
                nama = row[1]
                qty = row[2]
                harga = row[3]
                kabupaten = row[4]
                kecamatan = row[5]
                desa = row [6]

                print(f"| {tanggal:<10} | {nama:<20} | {qty:<5} | {harga:<10} | {kabupaten:<15} | {kecamatan:<15} | {desa:<15} |")
                print("-" * 65)
      
          balik = input('Tekan enter untuk kembali ke menu customer')
          if balik == '':
            clear_terminal()
            menu_customer(id_user)
          else :
            menu_customer(id_user)
      
      elif pilih == '2':
        menu_customer(id_user)
      
      else:
        print('=== PILIHAN TIDAK VALID ===')
    except Exception as e :
        print(f"Terjadi Error: {e}")
    finally:
          commit_db(connection, cursor)
    print()
    print()
# FITUR ADMIN
def generate_laporan(id_user):
    connect_db()
    connection, cursor = connect_db()
    clear_terminal()
    print("\n=== MENU LAPORAN ===")
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
          clear_terminal()
      elif pilih == '2':
            # STRING_AGG(b.nama_benih, ', '): menggabungkan nama benih menjadi satu string dalam satu transaksi.
            query = '''
                SELECT t.tanggal_transaksi, t.status_transaksi, t.metode_pembayaran, STRING_AGG(b.nama_benih, ', ')
                FROM transaksi t
                JOIN detail_pesanan d ON t.id_pesanan = d.id_pesanan
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE t.status_transaksi = 'selesai'
                GROUP BY t.id_transaksi
            '''
            clear_terminal()
      elif pilih == '3':
            query = '''
                SELECT t.tanggal_transaksi, t.status_transaksi, t.metode_pembayaran, b.nama_benih
                FROM transaksi t
                JOIN detail_pesanan d ON d.id_pesanan = t.id_pesanan
                JOIN benih b ON d.id_benih = b.id_benih
                WHERE t.tanggal_transaksi >= CURRENT_DATE - INTERVAL '3 months'
                ORDER BY t.tanggal_transaksi DESC
            '''
            clear_terminal()
      elif pilih == '4' :
        clear_terminal()
        menu_customer(id_user)
      else :
        print('=== PILIHAN TIDAK VALID ===')
        generate_laporan(id_user)
      cursor.execute(query)
      hasil = cursor.fetchall()
      # fetchall() mengambil semua hasil query dalam bentuk list.
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
        print("=== MONITORING & UPDATE STATUS PENGIRIMAN ===")
        print()
        print("Daftar Transaksi")
        query = """
            SELECT t.id_transaksi, t.tanggal_transaksi, STRING_AGG(b.nama_benih, ', '), SUM(d.quantity), t.status_transaksi
            FROM transaksi t
            JOIN detail_pesanan d ON t.id_pesanan = d.id_pesanan
            JOIN pesanan p ON t.id_pesanan = p.id_pesanan
            JOIN benih b ON d.id_benih = b.id_benih
            GROUP BY t.id_transaksi, t.tanggal_transaksi, b.nama_benih, d.quantity, t.status_transaksi
            ORDER BY t.id_transaksi
        """
        cursor.execute(query)
        results = cursor.fetchall()
        # fetchall() mengambil semua hasil query dalam bentuk list.
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
          clear_terminal()
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
          # commit() menyimpan perubahan.
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
            menu_admin(id_user)
# FITUR PRODUSEN
def cek_stok(id_user):
    connect_db()
    connection, cursor = connect_db()
    try:
        print()
        print("=== CEK STOK HABIS/KADALUARSA ===")
        print()
        print('1. Tampilkan Stok Benih')
        print('2. Kembali ke menu produsen')

        pilih = input('Pilih menu anda 1/2: ')

        if pilih == '1':
            query = """
                SELECT b.id_benih, b.nama_benih, b.harga,
                MIN(r.tanggal_kadaluarsa) AS kadaluarsa_terdekat,
                SUM(r.jumlah_produksi) AS stok
                FROM benih b
                LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
                GROUP BY b.id_benih, b.nama_benih, b.harga
                ORDER BY b.nama_benih ASC;
            """
            cursor.execute(query)
            data = cursor.fetchall()
            print("\nID | Nama Benih | Harga | Kadaluarsa | Total Stok")
            print("-" * 100)
            for row in data:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
            print("-" * 100)
        elif pilih == '2':
            clear_terminal()
            return menu_produsen(id_user)
        else:
            print('=== PILIHAN TIDAK VALID ===')
    except Exception as e:
        print(f"\nTerjadi Error: {e}")
    input("\nTekan ENTER untuk kembali ke menu...")
    clear_terminal()
    return menu_produsen(id_user)
def update_benih(id_user):
    connection, cursor = connect_db()
    try:
        print()
        print("=== UPDATE STOK BENIH ===")
        print()
        print("Daftar Stok")
        query = """
            SELECT b.id_benih, b.nama_benih,
            STRING_AGG(CAST(r.jumlah_produksi AS TEXT), ', ') AS daftar_produksi,
            SUM(r.jumlah_produksi) AS total_stok
            FROM benih b
            LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
            GROUP BY b.id_benih, b.nama_benih
            ORDER BY b.id_benih;
        """
        cursor.execute(query)
        data = cursor.fetchall()

        print("ID | Nama Benih | Daftar Produksi | Total Stok | Status Stok")
        print("-" * 120)

        for row in data:
            id_benih = row[0]
            nama = row[1]
            daftar_produksi = row[2] if row[2] else "-"
            total = row[3]
            if total is None:
                total = 0

            if total == 0:
             status_stok = "Habis"
            elif total < 50:
             status_stok = "Menipis"
            else:
             status_stok = "Aman" 

            print(f"{id_benih} | {nama} | {daftar_produksi} | {total} | {status_stok}")
            
        print("-" * 120)
        print()
        id_benih = input("Masukkan ID Benih: ")
        if not id_benih.isdigit():
            print("\n=== DATA TIDAK VALID ===\n")
            input("Tekan ENTER untuk kembali ke menu...")
            clear_terminal()
            return menu_produsen(id_user)
        cursor.execute("SELECT id_benih FROM benih WHERE id_benih = %s",(id_benih,))
        data = cursor.fetchone()

        if not data:
            print("\n=== ERROR: ID BENIH TIDAK DITEMUKAN ===")
            input("Tekan ENTER untuk kembali...")
            clear_terminal()
            return menu_produsen(id_user)

        
        stok_baru = input("Masukkan Stok Baru: ")
        if not stok_baru.isdigit():
            print("\n=== DATA TIDAK VALID ===\n")
            input("Tekan ENTER untuk kembali ke menu...")
            clear_terminal()
            return menu_produsen(id_user)
        
        id_benih = int(id_benih)
        stok_baru = int(stok_baru)

        if id_benih <= 0:
           print("\n=== DATA TIDAK VALID (stok harus > 0) ===")
           input("Tekan ENTER untuk kembali ke menu...")
           clear_terminal()
           return menu_produsen(id_user)

        tanggal_kadaluarsa = input("Masukkan Tanggal Kadaluarsa YYYY-MM-DD: ")
        from datetime import datetime
        try:
            tanggal_kadaluarsa = datetime.strptime(tanggal_kadaluarsa, "%Y-%m-%d").date()
        except ValueError:
            print("\n=== FORMAT TANGGAL TIDAK VALID (gunakan YYYY-MM-DD) ===")
            input("Tekan ENTER untuk kembali ke menu...")
            clear_terminal()
            return menu_produsen(id_user)

        query = query = """
            INSERT INTO riwayat_produksi (id_benih, jumlah_produksi, tanggal_produksi,tanggal_kadaluarsa)
            VALUES (%s, %s, CURRENT_DATE, %s)
        """
        cursor.execute(query, (id_benih, stok_baru, tanggal_kadaluarsa))
        connection.commit()


        query_total = """
            SELECT b.id_benih, b.nama_benih,
            SUM(r.jumlah_produksi) AS total_stok,
            MIN(r.tanggal_kadaluarsa) AS kadaluarsa_terdekat
            FROM benih b
            LEFT JOIN riwayat_produksi r ON b.id_benih = r.id_benih
            WHERE b.id_benih = %s
            GROUP BY b.id_benih, b.nama_benih
        """
        cursor.execute(query_total, (id_benih,))
        laporan = cursor.fetchone()
        print("\n=== LAPORAN STOK TERBARU ===")
        print(f"ID Benih           : {laporan[0]}")
        print(f"Nama Benih         : {laporan[1]}")
        print(f"Stok Ditambah      : {stok_baru}")
        print(f"Total Stok         : {laporan[2]}")
        print(f"Kadaluarsa Terdekat: {laporan[3]}")
        print("=============================")

        print("\nStok berhasil diperbarui!")

    except Exception as e:
        print(f"Terjadi Error: {e}")

    print()
    input("Tekan ENTER untuk kembali ke menu...")
    clear_terminal()
    menu_produsen(id_user)
def daftar_pesanan(id_user):
    connection, cursor = connect_db()
    print("╔════════════════════════════════════════════════════════╗")
    print("║                    DAFTAR PESANAN                      ║")
    print("╚════════════════════════════════════════════════════════╝")
    print()
    try:
        print(f"{'ID Pesanan':<12} {'ID User':<10} {'Benih':<20} {'Jumlah Pesanan':<10} {'Tanggal Pesan':<15}")
        print("-"*80)
    
        query =  """
            SELECT p.id_pesanan, p.id_user, b.nama_benih, dp.quantity, p.tanggal_pesanan
            FROM detail_pesanan dp
            JOIN pesanan p ON dp.id_pesanan = p.id_pesanan
            JOIN benih b ON dp.id_benih = b.id_benih
            ORDER BY p.id_pesanan ASC;
        """
        cursor.execute(query)   
        results = cursor.fetchall()
        for row in results:
            id_pesanan = row[0]
            user_id = row[1]
            nama_benih = row[2]
            jumlah = row[3]
            tanggal = str(row[4]) if row[4] else "-" 

            print(f"{id_pesanan:<12} {user_id:<10} {nama_benih:<20} {jumlah:<10} {tanggal:<15}")
        print("-"*80)
    except Exception as e:
        print(f"Terjadi Error: {e}")

    print()
    input("\nTekan ENTER untuk kembali ke menu...")
    clear_terminal()
    menu_produsen(id_user)

    print()
    print("=== WELCOME CUSTOMERR ===")
    print()
    try:
        print("1. Katalog Benih")
        print("2. Keranjang Belanja")
        print("3. Status Transaksi")
        print("4. Riwayat Transaksi")
        print("5. Keluar")
        print()
        pilih = input("Pilih Menu Customer: ")

        if pilih == "1":
            Katalog_Benih(id_user)
        elif pilih == "2":
            Keranjang_Belanja(id_user) 
        elif pilih == "3":
            Transaksi(id_user)
        elif pilih == "4":
            Riwayat_Transaksi(id_user)
        elif pilih == "5":
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
            clear_terminal()
            generate_laporan(id_user)
        elif pilihan == '2':
            clear_terminal()
            update_status_pengiriman(id_user)
        elif pilihan == '3':
            clear_terminal()
            print("Berhasil keluar dari menu admin.")
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
    print("=== WELCOME CUSTOMERR ===")
    print()
    try:
        print("1. Katalog Benih")
        print("2. Keranjang Belanja")
        print("3. Riwayat Transaksi")
        print("4. Keluar")
        print()
        pilih = input("Pilih Menu Customer: ")

        if pilih == "1":
            clear_terminal()
            Katalog_Benih(id_user)
        elif pilih == "2":
            clear_terminal()
            Keranjang_Belanja(id_user) 
        elif pilih == "3":
            clear_terminal()
            Riwayat_Transaksi(id_user)
        elif pilih == "4":
            clear_terminal()
            print('Berhasil keluar dari menu Customer')
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
def menu_produsen(id_user):
    print()
    print("\n=== WELCOMEE PRODUSEN === ")
    print()
    print("1. Cek Stok Habis/Kadaluarsa")
    print("2. Update Stok Benih")
    print("3. Lihat Daftar Pesanan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    if pilihan == '1':
      clear_terminal()
      cek_stok(id_user)
    elif pilihan == '2':
      clear_terminal()
      update_benih(id_user)
    elif pilihan == '3':
      clear_terminal()
      daftar_pesanan(id_user)
    elif pilihan == '4':
      clear_terminal()
      print('Berhasil keluar dari Menu Produsen')
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
  print('''
        SeedBridge adalah sebuah platform digital yang dirancang untuk menghubungkan PT. Benih Citra Asia, 
        para produsen benih, dan petani dalam satu ekosistem terpadu. Melalui aplikasi ini, seluruh proses 
        mulai dari penyediaan stok benih, pemesanan, distribusi, hingga pelacakan transaksi dapat dilakukan 
        secara real-time, lebih praktis, dan jauh lebih efisien dibanding cara manual.
        ''')
def dashboard():
    try:
      ds = input("Apakah sudah memiliki akun ? yes/no: ").lower()
      if ds == "yes":
        login()
      elif ds == "no":
        register()
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
        dashboard()
def login():
    connection, cursor = connect_db()

    print("=== LOGIN AKUN ANDA ===")
    usn = input("Username: ")
    pw = input("Password: ")

    query = """
        SELECT id_user, id_role FROM users
        WHERE username = %s AND password = %s
    """
    cursor.execute(query, (usn, pw))
    result = cursor.fetchone()
    
    if not result:
        clear_terminal()
        gambar()
        print()
        print()
        print("=== USERNAME ATAU PASSWORD SALAH, COBA LAGI ===")
        login()
    
    id_user, id_role = result
    clear_terminal()
    gambar()    

    if id_role == 1:
        print("=== LOGIN BERHASIL SEBAGAI CUSTOMER ===")
        menu_customer(id_user) 
    elif id_role == 2:
        print("=== LOGIN BERHASIL SEBAGAI PRODUSEN ===")
        menu_produsen(id_user)
    elif id_role == 3:
        print("=== LOGIN BERHASIL SEBAGAI ADMIN ===")
        menu_admin(id_user)
    else:
        print("Role tidak dikenali.")
        print()
        dashboard()
# BIKIN AKUN BARU
def register():
    try: 
      print("1. Customer")
      print("2. Produsen")
      pilih = input("Pilih Akun Role yang ingin anda buat 1/2: ")
      if pilih == "1": 
        data_customer(1)
        role = 1
      elif pilih == "2":
        data_produsen(2)
        role = 2
      else :
        clear_terminal()
        gambar()
        print()
        print()
        print("=== INPUT TIDAK VALID COBA LAGI ===")
        print()
        register()
      close_db()
    except Exception as e :
      print(f"Terjadi Error: {e}")
      register()
def data_customer(role):
    # ====== AMBIL DATA USER ======
    connection, cursor = connect_db()
    try:
        print()
        # NAMA
        nama = input("Masukkan Nama: ").strip()
        if not nama:
            print("Nama tidak boleh kosong!")
            clear_terminal()
            return data_customer(role)

        # USERNAME
        usn = input("Masukkan Username: ").strip()
        if len(usn) < 8:
            clear_terminal()
            print("Username minimal 8 karakter!")
            print()
            register()
        cursor.execute("SELECT 1 FROM users WHERE username = %s", (usn,))
        if cursor.fetchone():
            clear_terminal()
            print("Username sudah digunakan!")
            print()
            register()

        # PASSWORD
        pw = input("Masukkan Password: ").strip()
        if len(pw) < 8:
            clear_terminal()
            print("Password minimal 8 karakter!")
            print()
            register()

        # NO TELP
        no_telp = input("Masukkan No. Telepon: ").strip()
        if not (no_telp.isdigit() and len(no_telp) >= 10):
            clear_terminal()
            print("No. Telepon harus angka dan minimal 10 digit!")
            print()
            register()
        cursor.execute("SELECT 1 FROM users WHERE no_telp = %s", (no_telp,))
        if cursor.fetchone():
            clear_terminal()
            print("No. Telepon sudah digunakan!")
            print()
            register()

        # WILAYAH
        cursor.execute("SELECT id_kabupaten, nama FROM kabupaten")
        print("\nPilih Kabupaten:")
        for i, n in cursor.fetchall():
            print(f"{i}. {n}")
        id_kab = int(input("ID Kabupaten: "))

        cursor.execute("SELECT id_kecamatan, nama FROM kecamatan WHERE id_kabupaten = %s", (id_kab,))
        print("\nPilih Kecamatan:")
        for i, n in cursor.fetchall():
            print(f"{i}. {n}")
        id_kec = int(input("ID Kecamatan: "))

        cursor.execute("SELECT id_desa, nama FROM desa WHERE id_kecamatan = %s", (id_kec,))
        print("\nPilih Desa:")
        for i, n in cursor.fetchall():
            print(f"{i}. {n}")
        id_desa = int(input("ID Desa: "))

        print("\nAlamat tersimpan.\n")
         # BUAT KERANJANG BARU
        sql_create_keranjang = """
            INSERT INTO keranjang_pesanan 
            DEFAULT VALUES
            RETURNING id_keranjang
            """
        cursor.execute(sql_create_keranjang)
        id_keranjang = cursor.fetchone()[0] # ID Keranjang baru sudah didapatkan

        cursor.execute("""
            INSERT INTO users (nama, username, password, no_telp, id_role)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_user;
        """, (nama, usn, pw, no_telp, role))

        id_user = cursor.fetchone()[0]

        sql_update_user = """
            UPDATE users
            SET id_keranjang = %s
            WHERE id_user = %s;
            """
        cursor.execute(sql_update_user, (id_keranjang, id_user))

        # INSERT ALAMAT
        cursor.execute("""
            INSERT INTO alamat (id_user, id_desa)
            VALUES (%s, %s)
        """, (id_user, id_desa))

        connection.commit()

        gambar()
        print("=== Selamat Akun Anda Telah Dibuat ===")
        dashboard()
    except Exception as e:
        print("Terjadi error:", e)
        connection.rollback()
        register()

def data_produsen(role):
    connection, cursor = connect_db() 
    try:
      print()
      nama = input("Masukkan Nama: ").strip()
      if not nama:
        print("Nama tidak boleh kosong!")
        input("Tekan enter untuk kembali...")
        return
      usn = input("Masukkan Username: ").strip()
      if not usn:
        print("Username tidak boleh kosong!")
        input("Tekan enter untuk kembali...")
        return
      if len(usn) > 8:
        print('Username tersimpan')
      else:
        print("username harus lebih dari 8")
        return
      cursor.execute("SELECT username FROM users WHERE username = %s", (usn,))
      if cursor.fetchone():
         clear_terminal()
         print("Username sudah terdaftar, gunakan yang lain.")
         return
      pw = input("Masukkan Password:  ").strip()
      if not pw:
        print("Password tidak boleh kosong!")
        input("Tekan enter untuk kembali...")
        return
      if len(pw) > 8:
        print('Password tersimpan')
      else:
        clear_terminal()
        print("Password harus lebih dari 8. Silahkan Mulai Kembali")
        return
      no_telp = input("Masukkan No. Telepon: ").strip()
      if not no_telp:
        print("Nomer telepon tidak boleh kosong")
        input("Tekan enter untuk kembali...")
        return
      if no_telp.isdigit() and len(no_telp) >= 10:
        print('No. Telepon tersimpan')
      else:
        clear_terminal()
        print("No. Telepon harus berupa angka dan minimal 10 digit. Silahkan Mulai Kembali")
        input("Tekan enter untuk kembali....")
        register()
      cursor.execute("SELECT no_telp FROM users WHERE no_telp = %s", (no_telp,))
      if cursor.fetchone():
        clear_terminal()
        print("No. Telepon sudah terdaftar. Silahkan Mulai Kembali")
        return
    except Exception as e:
        print(f"Terjadi Error: {e}")
        return register()

    query = """
        INSERT INTO users (nama, username, password, no_telp, id_role)
         VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nama, usn, pw, no_telp, role))
    connection.commit()

    cursor.execute("SELECT id_user FROM users WHERE username = %s", (usn,))
    id_user = cursor.fetchone()[0]
    gambar()
    print("=== Selamat Akun Anda Telah Dibuat ===")
    dashboard()
gambar()
print("=== WELCOME TO OUR PLATFORM ===")
print()
print()
dashboard()