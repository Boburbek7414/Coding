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














# def pul_yechish(balans):
#     print("pul yechish tizimiga hush kelibsiz")
#     try:
#         sorov=float(input("Qancha pul yechmoqchisiz: "))
#         if sorov<=0:
#             raise ValueError("Pul manfiy yoki '0' ga teng bo'lmasligi kerak")
#         if sorov>balans:
#             raise ValueError("Hisobda pul yetarli emas.")
#         balans-=sorov
#         print(f"{sorov} so'm hisobdan yechildi.")
#     except ValueError as b:
#         print(f"Xatolik: {b}")
#     finally:
#         print(f"Jarayon tugatildi. Joriy balans: {balans} so'm")
# balans=1000
# pul_yechish(balans)