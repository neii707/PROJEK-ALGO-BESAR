
def menu_admin():
  print()
  print("=== WELCOMEE ADMINN ===")
  
def menu_customer():
  print()
  print("=== WELCOMEE CUSTOMERR ===")

def menu_produsen():
  print()
  print("=== WELCOMEE PRODUSEN ===  ")

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
  try:
    ds = input("Apakah sudah memiliki akun ? yes/no: ")
    if ds == "yes":
      login()
    elif ds == "no":
      register()
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
    print("PILIHAN TIDAK VALID")
  print()

def register():
  while True:
    try: 
      print("1. Admin")
      print("2. Customer")
      print("3. Produsen")
      pilih = input("Pilih Akun Role yang ingin anda buat: ")
      if pilih == "1":
        data_admin()
      elif pilih == "2": 
        data_customer()
      elif pilih == "3":
        data_produsen() 
      break
    except Exception as e :
      print(f"Terjadi Error: {e}")

def data_admin():
  while True:
    try:
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        break
      else :
        raise ValueError("Username harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  
  while True:
    try:
      pw = input("Masukkan Password:  ")
      if len(pw) > 8 :
        break
      else :
        raise ValueError("Password harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  print()
  print()
  print("Selamat Akun Anda Telah Dibuat")
  print()
  print()
  gambar()
  dashboard()

def data_customer():
  while True:
    try:
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        break
      else :
        raise ValueError("Username harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  
  while True:
    try:
      pw = input("Masukkan Password: ")
      if len(pw) > 8 :
        break
      else :
        raise ValueError("Password harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  print()
  print()
  print("Selamat Akun Anda Telah Dibuat")
  print()
  print()
  gambar()
  dashboard()

def data_produsen():
  while True:
    try:
      usn = input("Masukkan Username: ")
      if len(usn) > 8 :
        break
      else :
        raise ValueError("Username harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  
  while True:
    try:
      pw = input("Masukkan Password: ")
      if len(pw) > 8 :
        break
      else :
        raise ValueError("Password harus lebih dari 8")
    except Exception as e :
      print(f"Terjadi Error: {e}")
  print()
  print()
  print("Selamat Akun Anda Telah Dibuat")
  print()
  print()
  gambar()
  dashboard()

print("=== WELCOME TO OUR PLATFROM ===")
gambar()
dashboard()
