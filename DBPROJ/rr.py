import tkinter

import pymysql
from tkinter import *
from tkinter import messagebox

win = Tk()

win.geometry("1000x500")
win.title("햄버거 주문")

label123 = Label(win, text="햄버거 주문 사이트 입니다")
label123.pack()
label234 = Label(win, text="주문하시겠습니까?")
label234.pack()
btn = Button(win, text="주문자 정보 입력")
btn112 = Button(win, text="주문완료")

sql = ""
name = ""
mobile = ""
addr = ""


def clickButton():
    messagebox.showinfo("버튼 클릭", "주문 정보가 저장되었습니다")


def alert():
    label234.config(text="")
    btn.pack_forget()
    btn112.pack_forget()
    lab1 = Label(win)
    lab1.config(text="정보를 입력해주세요!")
    lab1.pack()
    editFrame = Frame(win)
    editFrame.pack()

    def insertData():
        conn = None
        cur = None

        # 데이터베이스 접속
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            db="ordertest",
            charset="utf8",
        )

        # 커서
        cur = conn.cursor()

        # 회원 정보 insert 기능 구현
        # 사용자에게 입력받은 회원 정보 초기화
        name, mobile, addr, menu1, menu2, menu3 = "", "", "", "", "", ""

        # GUI에서 입력한 데이터 담기
        name = edt1.get()
        mobile = edt2.get()
        addr = edt3.get()
        menu1 = edt4.get()
        menu2 = edt5.get()
        menu3 = edt6.get()

        # SQL 쿼리 만들기

        sql = (
            "INSERT INTO test1(name, mobile, addr, menu1, menu2, menu3)VALUES "
            "('"
            + name
            + "','"
            + mobile
            + "','"
            + addr
            + "','"
            + menu1
            + "','"
            + menu2
            + "','"
            + menu3
            + "')"
        )
        print(sql)
        try:
            cur.execute(sql)
        except:
            messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
        else:
            # 쿼리 실행이 완료(오류 없이)
            # 1) 메시지 박스로 성공 알림
            messagebox.showinfo("성공", "회원 정보가 등록 되었습니다.")
            # 2) 데이터 커밋 (진짜 저장)
            conn.commit()
            # 3) 테이블 조회(새로고침)
            selectData()

        # GUI에 입력한 데이터 삭제
        edt1.delete(0, "end")
        edt2.delete(0, "end")
        edt3.delete(0, "end")
        edt4.delete(0, "end")
        edt5.delete(0, "end")
        edt6.delete(0, "end")
        # DB접속 종료
        conn.close()

    def selectData():
        conn = None
        cur = None
        # 데이버베이스 접속
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="1234",
            db="ordertest",
            charset="utf8",
        )
        # 커서
        cur = conn.cursor()
        conn.commit
        lname, lmobile, laddr, lmenu1, lmenu2, lmenu3 = [], [], [], [], [], []

        # 데이터 초기화
        lname.append("이름")
        lname.append("-------")

        lmobile.append("전화번호")
        lmobile.append("-------")

        laddr.append("주소")
        laddr.append("-------")

        lmenu1.append("메뉴")
        lmenu1.append("-------")

        # select 기능 구현
        sql = "SELECT name, mobile, addr, CONCAT(menu1,',',menu2,',',menu3) AS menu FROM test1"
        cur.execute(sql)

        while True:
            row = cur.fetchone()

            if row == None:
                break

            lname.append(row[0])
            lmobile.append(row[1])
            laddr.append(row[2])
            lmenu1.append(row[3])
            lmenu2.append(row[3])
            lmenu3.append(row[3])

        # GUI ListBox에 insert
        # listUserID, listName, listBirthYear, listAddr
        # 1) 리스트 박스 초기화
        listname.delete(0, listname.size() - 1)  #
        listmobile.delete(0, listmobile.size() - 1)
        listaddr.delete(0, listaddr.size() - 1)
        listmenu1.delete(0, listmenu1.size() - 1)

        # 2) select 해온 데이터 insert
        for item1, item2, item3, item4 in zip(
            lname, lmobile, laddr, lmenu1
        ):  # 직접 가져온 데이터
            listname.insert(END, item1)
            listmobile.insert(END, item2)
            listaddr.insert(END, item3)
            listmenu1.insert(END, item4)

        conn.close()

    listFrame = Frame(win)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    label1 = Label(editFrame, text="주문자 이름")
    label1.pack(side=LEFT, padx=10, pady=10)

    edt1 = Entry(editFrame, width=10)
    edt1.pack(side=LEFT, padx=10, pady=10)

    label2 = Label(editFrame, text="전화번호")
    label2.pack(side=LEFT, padx=10, pady=10)

    edt2 = Entry(editFrame, width=10)
    edt2.pack(side=LEFT, padx=10, pady=10)

    label3 = Label(editFrame, text="주소")
    label3.pack(side=LEFT, padx=10, pady=10)

    edt3 = Entry(editFrame, width=10)
    edt3.pack(side=LEFT, padx=10, pady=10)

    label4 = Label(editFrame, text="메뉴1")
    label4.pack(side=LEFT, padx=10, pady=10)

    edt4 = Entry(editFrame, width=10)
    edt4.pack(side=LEFT, padx=10, pady=10)

    label5 = Label(editFrame, text="메뉴2")
    label5.pack(side=LEFT, padx=10, pady=10)

    edt5 = Entry(editFrame, width=10)
    edt5.pack(side=LEFT, padx=10, pady=10)

    label6 = Label(editFrame, text="메뉴3")
    label6.pack(side=LEFT, padx=10, pady=10)

    edt6 = Entry(editFrame, width=10)
    edt6.pack(side=LEFT, padx=10, pady=10)

    # 버튼
    btnInsert = Button(editFrame, text="주문 확인", command=insertData)
    btnInsert.pack(side=LEFT, padx=20, pady=10)
    btn.destroy()
    lab2 = Label(win)
    lab2.config(text="메뉴를 선택해주세요")
    lab2.pack()
    # 셀렉트 버튼 구현
    # 뒤로가기 버튼을 클릭시에 테이블에 저장

    btnok2 = Button(win, text="주문 완료", command=alert3)
    btnok2.pack()

    listname = Listbox(listFrame)
    listname.pack(side=LEFT, fill=BOTH, expand=1)

    listmobile = Listbox(listFrame)
    listmobile.pack(side=LEFT, fill=BOTH, expand=1)

    listaddr = Listbox(listFrame)
    listaddr.pack(side=LEFT, fill=BOTH, expand=1)

    listmenu1 = Listbox(listFrame)
    listmenu1.pack(side=LEFT, fill=BOTH, expand=1)


def alert3():
    label234.config(text="")
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
