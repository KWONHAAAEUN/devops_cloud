import os
import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox

win = Tk()
t_path = "c:\\py_haeun\\status.txt"
menu = []

win.geometry("1000x700")
win.title("햄버거 주문")

win.configure(background="red")
label123 = Label(win, text="햄버거 주문 사이트 입니다", font=("맑은 고딕", 18), bg="red", fg="white")
label123.pack()

photo1 = PhotoImage(file="C:\img\권하은.png")
pLabel = Label(win, image=photo1)
pLabel.pack(side=TOP, padx=10, pady=10)


label234 = Label(win, text="주문하시겠습니까?", font=("맑은 고딕", 16), bg="red", fg="white")
label234.pack()
btn = Button(win, text="주문자 정보 입력", bg="yellow", fg="black")
btn112 = Button(win, text="주문완료")

sql = ""
name = ""
mobile = ""
addr = ""


def clickButton():
    messagebox.showinfo("버튼 클릭", "메뉴가 저장되었습니다")


def alert():
    label234.config(text="")
    pLabel.pack_forget()
    btn.pack_forget()
    btn112.pack_forget()
    lab1 = Label(win)
    lab1.config(text="정보를 입력해주세요!", font=("맑은 고딕", 18), bg="red", fg="white")
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
        name, mobile, addr, menu = "", "", "", ""

        # GUI에서 입력한 데이터 담기
        name = edt1.get()
        mobile = edt2.get()
        addr = edt3.get()
        filePath = "C:\py_haeun\status.txt"
        f = open(filePath, "r")
        menu = f.read()

        # SQL 쿼리 만들기

        sql = (
            "INSERT INTO test1(name, mobile, addr, menu)VALUES "
            "('" + name + "','" + mobile + "','" + addr + "','" + menu + "')"
        )
        print(sql)
        try:
            cur.execute(sql)
        except:
            messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
        else:
            # 쿼리 실행이 완료(오류 없이)
            # 1) 메시지 박스로 성공 알림
            messagebox.showinfo("성공", "주문 정보가 등록 되었습니다.")
            # 2) 데이터 커밋 (진짜 저장)
            conn.commit()
            # 3) 테이블 조회(새로고침)
            selectData()

        # GUI에 입력한 데이터 삭제
        edt1.delete(0, "end")
        edt2.delete(0, "end")
        edt3.delete(0, "end")

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
        lname, lmobile, laddr, lmenu = [], [], [], []

        # 데이터 초기화
        lname.append("이름")
        lname.append("-------")

        lmobile.append("전화번호")
        lmobile.append("-------")

        laddr.append("주소")
        laddr.append("-------")

        lmenu.append("메뉴")
        lmenu.append("-------")

        # select 기능 구현
        sql = "SELECT name, mobile, addr, menu FROM test1"
        cur.execute(sql)

        while True:
            row = cur.fetchone()

            if row == None:
                break

            lname.append(row[0])
            lmobile.append(row[1])
            laddr.append(row[2])
            lmenu.append(row[3])

        # GUI ListBox에 insert
        # listUserID, listName, listBirthYear, listAddr
        # 1) 리스트 박스 초기화
        listname.delete(0, listname.size() - 1)  #
        listmobile.delete(0, listmobile.size() - 1)
        listaddr.delete(0, listaddr.size() - 1)
        listmenu.delete(0, listmenu.size() - 1)

        # 2) select 해온 데이터 insert
        for item1, item2, item3, item4 in zip(
            lname, lmobile, laddr, lmenu
        ):  # 직접 가져온 데이터
            listname.insert(END, item1)
            listmobile.insert(END, item2)
            listaddr.insert(END, item3)
            listmenu.insert(END, item4)

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

    def status1_print():
        print(lang_var1.get())

    def status2_print():
        print(lang_var2.get())

    def status3_print():
        print(lang_var3.get())

    def status4_print():
        print(lang_var4.get())

    def status5_print():
        print(lang_var5.get())

    def status6_print():
        print(lang_var6.get())

    def save_status(event):
        file = open(t_path, "w")
        file.write("%s\n" % lang_var1.get())
        file.write("%s\n" % lang_var2.get())
        file.write("%s\n" % lang_var3.get())
        file.write("%s\n" % lang_var4.get())
        file.write("%s\n" % lang_var5.get())
        file.write("%s\n" % lang_var6.get())
        file.close()

    def file_open(event):
        os.system("start %s" % t_path)

    lab2 = Label(win)
    lab2.config(text="메뉴를 선택해주세요", font=("맑은 고딕", 18), bg="red", fg="white")
    lab2.pack()
    lang_var1 = StringVar()
    lang_var2 = StringVar()
    lang_var3 = StringVar()
    lang_var4 = StringVar()
    lang_var5 = StringVar()
    lang_var6 = StringVar()  # str 형으로 변수 저장

    # photo2 = PhotoImage(file="C:\img\불고기.png")
    # pLabel1 = Label(win, image=photo2)
    # pLabel1.pack(side="left")

    btn_lang1 = Checkbutton(
        win,
        text="불고기버거",
        onvalue="불고기버거 ",
        offvalue="",
        variable=lang_var1,
        command=status1_print,
        font=("맑은 고딕", 15),
    )
    # photo3 = PhotoImage(file="C:\img\상하이.png")
    # pLabel = Label(win, image=photo3)
    # pLabel.pack(side="left")

    btn_lang2 = Checkbutton(
        win,
        text="치킨버거",
        onvalue="치킨버거 ",
        offvalue="",
        variable=lang_var2,
        command=status2_print,
        font=("맑은 고딕", 15),
    )
    btn_lang3 = Checkbutton(
        win,
        text="새우버거",
        onvalue="새우버거 ",
        offvalue="",
        variable=lang_var3,
        command=status3_print,
        font=("맑은 고딕", 15),
    )
    btn_lang4 = Checkbutton(
        win,
        text="감자튀김",
        onvalue="감자튀김 ",
        offvalue="",
        variable=lang_var4,
        command=status4_print,
        font=("맑은 고딕", 15),
    )
    btn_lang5 = Checkbutton(
        win,
        text="콜라",
        onvalue="콜라 ",
        offvalue="",
        variable=lang_var5,
        command=status5_print,
        font=("맑은 고딕", 15),
    )
    btn_lang6 = Checkbutton(
        win,
        text="사이다",
        onvalue="사이다 ",
        offvalue="",
        variable=lang_var6,
        command=status6_print,
        font=("맑은 고딕", 15),
    )
    btn_lang1.pack(side="left")
    btn_lang1.deselect()
    btn_lang2.pack(side="left")
    btn_lang2.deselect()
    btn_lang3.pack(side="left")
    btn_lang3.deselect()
    btn_lang4.pack(side="left")
    btn_lang4.deselect()
    btn_lang5.pack(side="left")
    btn_lang5.deselect()
    btn_lang6.pack(side="left")
    btn_lang6.deselect()

    btn.destroy()

    save_btn = Button(
        win,
        text="메뉴 저장",
        bg="yellow",
        fg="black",
        font=("맑은 고딕", 10),
        command=clickButton,
    )
    save_btn.bind("<Button-1>", save_status)
    save_btn.bind("<Button-3>", file_open)
    save_btn.place(x=700, y=191)

    btnInsert = Button(
        win,
        text="주문하기",
        command=insertData,
        bg="yellow",
        fg="black",
        font=("맑은 고딕", 10),
    )
    btnInsert.pack()

    listname = Listbox(listFrame)
    listname.pack(side=LEFT, fill=BOTH, expand=1)

    listmobile = Listbox(listFrame)
    listmobile.pack(side=LEFT, fill=BOTH, expand=1)

    listaddr = Listbox(listFrame)
    listaddr.pack(side=LEFT, fill=BOTH, expand=1)

    listmenu = Listbox(listFrame)
    listmenu.pack(side=LEFT, fill=BOTH, expand=1)


btn.config(command=alert)

btn.pack()
btn112.pack()
btn112.pack_forget()
win.mainloop()
