import pymysql

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 insert
sql = ""  # 실제 사용 쿼리
# userID, name, birthYear, addr은 넣어야한다 (NOT NULL)
userID = ""
name = ""
birthYear = ""
addr = ""
mokile1 = ""
mobile2 = ""
height = ""


# 과제 mobile1, mobile2 height까지 insert
while True:
    userID = input("사용자 ID ==>")
    if userID == "":
        break
    name = input("사용자 이름 ==>")
    birthYear = input("사용자 출생년도 ==>")
    addr = input("사용자 주소 ==>")
    mokile1 = input("사용자 전화번호 앞3자리 ==>")
    mobile2 = input("사용자 전화번호 뒤8자리 ==>")
    height = input("사용자 키 ==>")

    sql = (
        "INSERT INTO userTBL (userID, name, birthYear, addr, mokile1, mobile2, height, mDate) VALUES "
        "('"
        + userID
        + "','"
        + name
        + "',"
        + birthYear
        + ",'"
        + addr
        + "','"
        + mokile1
        + "','"
        + mobile2
        + "',"
        + height
        + ",CURDATE())"  # 작은 따옴표 넣는 기준은 테이블 데이터 넣은 것을 보고 결정
    )
    cur.execute(sql)

conn.commit()
conn.close()
