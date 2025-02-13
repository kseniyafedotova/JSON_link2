import sqlite3
 
# ������� ���������� � ����� ����� ������
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
 
# �������� ���������� ��� �������
cursor.execute("PRAGMA table_info(users)")
 
# ������� �������� ����� �������
fields = cursor.fetchall()
for field in fields:
	print(field[1])
 
# ��������� ���������� � ����� ������
conn.close()



