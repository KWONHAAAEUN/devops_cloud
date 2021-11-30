import pymysql
from tkinter import *
from tkinter import messagebox

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

# 커서
cur = conn.cursor()

window = Tk()
window.title("심리테스트")

label1 = Label(window, text="심리테스트를 시작합니다")
label2 = Label(window, text="원하는 테스트의 버튼을 클릭해주세요")
button1 = Button(
    window,
    text="심테1",
    fg="yellow",
    bg="black",
    command=lambda: controller.show_frame("PageOne"),
)

label1.pack()
label2.pack()
button1.pack()

window.mainloop()
