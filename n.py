# import sqlite3

# connection = sqlite3.connect('student.db')
# cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS student (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     grade TEXT NOT NULL    
# )
# ''')

# def add_student(name,age,grade):
#     connection=sqlite3.connect('students.db')
#     cursor=connection.cursor

#     cursor.execute('''
#     INSERT INTO students (name,grade,grade)
#     VALEUS(?,?,?)
# ''',(name,age,grade))
    
#     connection.commit()
#     print(f"{name} ismli student qo'shildi!")
#     connection.close()

# def get_students():
#     connection=sqlite3.connect('students.db')
#     cursor=connection.cursor()

#     cursor.execute('SELECT*FROM students')
#     students=cursor.fetchall()
#     for student in students:
#         print(student)

#     connection.close()
# import sqlite3

# # SQLite bazasiga ulanish
# connection = sqlite3.connect('students.db')  # 'students.db' nomli baza faylini yaratadi
# cursor = connection.cursor()

# # Studentlar jadvalini yaratish
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     grade TEXT NOT NULL
# )
# ''')

# print("Jadval yaratildi yoki mavjud!")
# connection.commit()  # O'zgarishlarni saqlash
# connection.close()


# def add_student(name, age, grade):
#     connection = sqlite3.connect('students.db')
#     cursor = connection.cursor()

#     cursor.execute('''
#     INSERT INTO students (name, age, grade)
#     VALUES (?, ?, ?)
#     ''', (name, age, grade))

#     connection.commit()
#     print(f"{name} ismli student qo'shildi!")
#     connection.close()

# def get_students():
#     connection = sqlite3.connect('students.db')
#     cursor = connection.cursor()

#     cursor.execute('SELECT * FROM students')
#     students = cursor.fetchall() 
#     for student in students:
#         print(student)

#     connection.close()



# if __name__ == '__main__':
#     add_student('Ali', 20, 'A')
#     add_student('Madina', 19, 'B')
#     add_student('Bekzod', 22, 'A+')
#     print("Barcha talabalar muvaffaqiyatli qo'shildi!")
#     get_students()



# import psycopg2

# # PostgreSQLga ulanish uchun ma'lumotlar
# db_params = {
#     'dbname': 'postgres',  # O'zingizning baza nomingiz
#     'user': 'postgres',  # O'zingizning foydalanuvchi nomingiz
#     'password': '7414',  # Parolingiz
#     'host': 'localhost',  # Ma'lumotlar bazasining serveri (agar lokal bo'lsa, localhost)
#     'port': '5432'  # PostgreSQLning porti (default 5432)
# }

# # PostgreSQLga ulanish
# def create_connection():
#     return psycopg2.connect(**db_params)

# # Foydalanuvchi yaratish
# def create_user(username, balance):
#     conn = create_connection()
#     cur = conn.cursor()

#     # Foydalanuvchini bazaga qo'shish
#     cur.execute("INSERT INTO accounts (username, balance) VALUES (%s, %s)", (username, balance))

#     conn.commit()  # O'zgarishlarni saqlash
#     cur.close()
#     conn.close()
#     print(f"Foydalanuvchi {username} yaratildi!")

# # Foydalanuvchi balansini ko'rsatish
# def get_balance(username):
#     conn = create_connection()
#     cur = conn.cursor()

#     # Foydalanuvchining balansini olish
#     cur.execute("SELECT balance FROM accounts WHERE username = %s", (username,))
#     balance = cur.fetchone()  # 1ta natijani olish

#     cur.close()
#     conn.close()

#     if balance:
#         print(f"{username} balans: {balance[0]}")
#     else:
#         print(f"Foydalanuvchi {username} topilmadi.")

# # Pul o'tkazma operatsiyasi
# def transfer_money(from_username, to_username, amount):
#     conn = create_connection()
#     cur = conn.cursor()

#     # Tranzaksiyani boshlash
#     conn.autocommit = False
#     try:
#         # Sender balansini tekshirish
#         cur.execute("SELECT balance FROM accounts WHERE username = %s", (from_username,))
#         sender_balance = cur.fetchone()

#         if sender_balance and sender_balance[0] >= amount:
#             # Hisobdan pulni kamaytirish
#             cur.execute("UPDATE accounts SET balance = balance - %s WHERE username = %s", (amount, from_username))

#             # Hisobga pulni qo'shish
#             cur.execute("UPDATE accounts SET balance = balance + %s WHERE username = %s", (amount, to_username))

#             # Agar operatsiya muvaffaqiyatli bo'lsa, commit qilish
#             conn.commit()
#             print(f"{from_username} dan {to_username} ga {amount} miqdoridagi pul o'tkazildi.")
#         else:
#             print(f"{from_username} balansida yetarli mablag' yo'q!")
#             conn.rollback()  # Balans yetarli bo'lmasa, rollback

#     except Exception as e:
#         # Xato yuzaga kelsa, rollback qilish
#         conn.rollback()
#         print(f"Xato: {e}")

#     finally:
#         cur.close()
#         conn.close()

# # Main funktsiyasi (foydalanuvchidan kiritish)
# if __name__ == "__main__":
#     while True:
#         print("\nTanlovni kiriting:")
#         print("1. Foydalanuvchi yaratish")
#         print("2. Balansni ko'rish")
#         print("3. Pul o'tkazma qilish")
#         print("4. Dasturdan chiqish")

#         choice = input("Tanlovni kiriting (1/2/3/4): ")

#         if choice == '1':
#             username = input("Foydalanuvchi ismini kiriting: ")
#             balance = float(input(f"{username} uchun balansni kiriting: "))
#             create_user(username, balance)

#         elif choice == '2':
#             username = input("Balansini ko'rmoqchi bo'lgan foydalanuvchi ismini kiriting: ")
#             get_balance(username)

#         elif choice == '3':
#             from_username = input("Pul o'tkaziladigan foydalanuvchi ismini kiriting: ")
#             to_username = input("Pul o'tkazadigan foydalanuvchi ismini kiriting: ")
#             amount = float(input(f"{from_username} dan {to_username} ga o'tkaziladigan miqdorni kiriting: "))
#             transfer_money(from_username, to_username, amount)

#         elif choice == '4':
#             print("Dasturdan chiqilyapti...")
#             break

#         else:
#             print("Noto'g'ri tanlov! Iltimos, 1, 2, 3 yoki 4 ni kiriting.")

# def pul_yechish(balanc):
    
#     print("Pul yechish tizimiga xush kelibsiz!")
#     try:
#         sorov=float(input("Qancha pul yechmoqchisiz? "))
#         if sorov<=0:
#             raise ValueError("Pul manfiy yoki nol bo'lmasligi kerak.")
#         if sorov>balanc:
#             raise ValueError("Hisobda yetarli mablag' yo'q.")
#         balanc-=sorov
#         print(f"{sorov} so'm yechildi. Qolgan balans: {balanc} so'm.")
#     except ValueError as b:
#         print(f"Xatolik: {b}")
#     finally:
#         print(f"Jarayon tugatildi. Joriy balans: {balanc} so'm.")
# balanc=1000   

# pul_yechish(balanc)
