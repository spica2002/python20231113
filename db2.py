# db2.py
import sqlite3

# 메모리에서 작업
# 연결객체 리턴받기
#con = sqlite3.connect(":memory:")  # 메모리에 저장
con = sqlite3.connect("c:\\work\\test.db")

# 커서객체 리턴
cur = con.cursor()

# 테이블구조(자료구조생성)
cur.execute("create table PhoneBook (name text, phonenum text);")

# 1건 입력
cur.execute("insert into PhoneBook values ('홍길동', '010-222');")

# 입력 파라미터 처리
name = "전우치"
phonenumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phonenumber))

# N건을 입력
datalist = (("박문수","010-333"),("김기동","010-444"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

# 검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("===fetchone()---")  # 튜플 ()
print(cur.fetchone())
print("---fetchmany(2)---")   # 리스트   []
print(cur.fetchmany(2))
print("---fetchall()---")   # 리스트  []
print(cur.fetchall())
