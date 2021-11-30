from tkinter import *
import pymysql
from tkinter import messagebox

conn = None
cur = None

# 데이터베이스 접속
conn = pymysql.connect(
    host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
)

win = Tk()

win.geometry("1000x500")
win.title("햄버거 주문")

label1 = Label(win, text="햄버거 주문 사이트 입니다")
label1.pack()
label2 = Label(win, text="주문하시겠습니까?")
label2.pack()
btn = Button(win, text="주문자 정보 입력")
btn112 = Button(win, text="주문완료")

sql = ""
name = ""
mobile = ""
addr = ""


def clickButton():
    messagebox.showinfo("버튼 클릭", "주문 정보가 저장되었습니다")


def alert():
    label2.config(text="")
    btn.pack_forget()
    btn112.pack_forget()
    lab1 = Label(win)
    lab1.config(text="정보를 입력해주세요!")
    lab1.pack()
    # while True:
    #     name = input("이름 ==>")
    #     if name == "":
    #         break
    #     mobile = input("전화번호(-)제외 ==>")
    #     if mobile == "":
    #         break
    #     addr = input("주소 ==>")
    #     if addr == "":
    #         break
    #     sql = "INSERT INTO ordertest (name, mobile, addr) VALUES"
    btn.destroy()
    lab2 = Label(win)
    lab2.config(text="메뉴를 선택해주세요")
    lab2.pack()
    # 셀렉트 버튼 구현
    # 뒤로가기 버튼을 클릭시에 테이블에 저장
    btnok1 = Button(win, text="주문 저장", command=clickButton)
    btnok1.pack()

    btnok2 = Button(win, text="주문 완료", command=alert3)
    btnok2.pack()


def alert3():
    label2.config(text="")
    btn.pack_forget()
    btn112.pack_forget()
    lab3 = Label(win)
    lab3.config(text="주문이 완료되었습니다!")
    lab3.pack()
    btn112.destroy()


btn.config(command=alert)
btn112.config(command=alert3)

btn.pack()
btn112.pack()
btn112.pack_forget()
win.mainloop()
