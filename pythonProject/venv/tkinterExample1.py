from tkinter import *

# 문자를 표현할 수 있는 라벨 사용
window = Tk()
window.title("라벨 연습")
# window.geometry("400x100")  # 사이즈 넓이*높이
# window.resizable(width=TRUE, height=TRUE)  # 사이즈 고정

# 라벨 선언
label1 = Label(window, text="This is MariaDB를")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부중이다", bg="magenta", width=20, height=5, anchor=NW)
# 레이블이 올라갈 윈도우, 출력될 글, 설정: font=글씨체, fg=글씨색, bg=배경색, anchor=위치(SE,NW..기본은 center)

# 위젯 적용
label1.pack()
label2.pack()
label3.pack()


window.mainloop()
