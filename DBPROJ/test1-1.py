import os
import tkinter

import pymysql
from tkinter import *
from tkinter import messagebox, ttk

win = Tk()
t_path = "c:\\py_haeun\\status.txt"

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


def clickButton1():
    messagebox.showinfo("버튼 클릭", "주문 정보가 저장되었습니다")


def alert(lang_var1=None, lang_var2=None, lang_var3=None):
    label234.config(text="")
    btn.pack_forget()
    btn112.pack_forget()
    lab1 = Label(win)
    lab1.config(text="정보를 입력해주세요!")
    lab1.pack()
    editFrame = Frame(win)
    editFrame.pack()

    def insertData1():
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
        name, mobile, addr = "", "", ""

        # GUI에서 입력한 데이터 담기
        name = edt1.get()
        mobile = edt2.get()
        addr = edt3.get()

        # SQL 쿼리 만들기

        sql = (
            "INSERT INTO test1(name, mobile, addr)VALUES "
            "('" + name + "','" + mobile + "','" + addr + "')"
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
            selectData1()

        # GUI에 입력한 데이터 삭제
        edt1.delete(0, "end")
        edt2.delete(0, "end")
        edt3.delete(0, "end")
        # DB접속 종료
        conn.close()

    def selectData1():
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
        lname, lmobile, laddr = [], [], []

        # 데이터 초기화
        lname.append("이름")
        lname.append("-------")

        lmobile.append("전화번호")
        lmobile.append("-------")

        laddr.append("주소")
        laddr.append("-------")

        # select 기능 구현
        sql = "SELECT name, mobile, addr FROM test1"
        cur.execute(sql)

        while True:
            row = cur.fetchone()

            if row == None:
                break

            lname.append(row[0])
            lmobile.append(row[1])
            laddr.append(row[2])

        # GUI ListBox에 insert
        # listUserID, listName, listBirthYear, listAddr
        # 1) 리스트 박스 초기화
        listname.delete(0, listname.size() - 1)  #
        listmobile.delete(0, listmobile.size() - 1)
        listaddr.delete(0, listaddr.size() - 1)
        listmenu1.delete(0, listmenu1.size() - 1)

        # 2) select 해온 데이터 insert
        for item1, item2, item3, item4 in zip(
            lname, lmobile, laddr
        ):  # 직접 가져온 데이터
            listname.insert(END, item1)
            listmobile.insert(END, item2)
            listaddr.insert(END, item3)

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

    def insertData2():
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
        menu1 = ""

        # GUI에서 입력한 데이터 담기

        # SQL 쿼리 만들기

        sql = "INSERT INTO test1(menu1)VALUES""('" + name + "','" + mobile + "','" + addr + "')"
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
            selectData2()

        # GUI에 입력한 데이터 삭제

        # DB접속 종료
        conn.close()

    def status1_print():
        print(lang_var1.get())

    def status2_print():
        print(lang_var2.get())

    def status3_print():
        print(lang_var3.get())

    def save_status(event):
        file = open(t_path, "w")
        file.write("%s\n" % lang_var1.get())
        file.write("%s\n" % lang_var2.get())
        file.write("%s\n" % lang_var3.get())
        file.close()
        print("save complete!")

    def file_open(event):
        os.system("start %s" % t_path)

    def btnpress():  # 함수 btnpress() 정의
        a = []

    lang_var1 = StringVar()
    lang_var2 = StringVar()
    lang_var3 = StringVar()  # str 형으로 변수 저장
    btn_lang1 = Checkbutton(
        win,
        text="햄버거",
        onvalue="햄버거",
        variable=lang_var1,
        command=status1_print,
    )
    # root라는 창에 "Python"이라는 내용을 가지고 "Python"이라는 value값을 가진 라디오 버튼 생성
    btn_lang1.select()  # 기본값 선택
    btn_lang2 = Checkbutton(
        win, text="커피", onvalue="커피", variable=lang_var2, command=status2_print
    )
    btn_lang3 = Checkbutton(
        win, text="사이다", onvalue="사이다", variable=lang_var3, command=status3_print
    )
    btn_lang1.pack()
    btn_lang1.deselect()
    btn_lang2.pack()
    btn_lang2.deselect()
    btn_lang3.pack()
    btn_lang3.deselect()

    save_btn = tkinter.Label(win, text="save", bg="grey19", fg="snow")
    save_btn.bind("<Button-1>", save_status)
    save_btn.bind("<Button-3>", file_open)
    save_btn.place(x=180, y=100)

    file_path = "C:\py_haeun\status.txt"

    with open(file_path) as f:
        lines = f.readlines()

    lines = [line.rstrip("\n") for line in lines]

    def selectData2():
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
        lmenu1 = []
        lmenu1 = lines
        lmenu1.append("메뉴")
        lmenu1.append("-------")

        # select 기능 구현
        sql = "SELECT menu1 FROM test1"
        cur.execute(sql)

        while True:
            row = cur.fetchone()

            if row == None:
                break

            lmenu1.append(row[3])

        listmenu1.delete(0, listmenu1.size() - 1)

        # 2) select 해온 데이터 insert
        for item4 in zip(lmenu1):  # 직접 가져온 데이터

            listmenu1.insert2(END, item4)

        conn.close()

    # btn100 = Button(win)  # root라는 창에 버튼 생성
    # btn100.config(text="선택")  # 버튼 내용
    # btn100.config(width=10)  # 버튼 크기
    # btn100.config(command=btnpress)  # 버튼 기능 (btnpree() 함수 호출)
    # btn100.pack()  # 버튼 배치

    lb = Label(win)  # root라는 창에 레이블 생성
    lb.pack()

    # label4 = Label(editFrame, text="메뉴1")
    # label4.pack(side=LEFT, padx=10, pady=10)
    #
    # edt4 = Entry(editFrame, width=10)
    # edt4.pack(side=LEFT, padx=10, pady=10)
    #
    # label5 = Label(editFrame, text="메뉴2")
    # label5.pack(side=LEFT, padx=10, pady=10)
    #
    # edt5 = Entry(editFrame, width=10)
    # edt5.pack(side=LEFT, padx=10, pady=10)
    #
    # label6 = Label(editFrame, text="메뉴3")
    # label6.pack(side=LEFT, padx=10, pady=10)
    #
    # edt6 = Entry(editFrame, width=10)
    # edt6.pack(side=LEFT, padx=10, pady=10)

    # 버튼
    btnInsert = Button(editFrame, text="주문 확인", command=insertData2)
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
