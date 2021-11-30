import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter import ttk
from tkinter import *

# tkinter 객체 생성
import controller as controller

window = Tk()

# 사용자 id와 password를 저장하는 변수 생성
user_id, password = StringVar(), StringVar()

# 사용자 id와 password를 비교하는 함수
def check_data():
    if user_id.get() == "Passing" and password.get() == "Story":
        print("Logged IN Successfully")
    else:
        print("Check your Usernam/Password")


# 회원가입하는 함수
def new_join_data():
    if user_id.get() == "Passing" and password.get() == "Story":
        print("Logged IN Successfully")
    else:
        print("Check your Usernam/Password")


# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
ttk.Label(window, text="ID : ").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
ttk.Entry(window, textvariable=user_id).grid(row=0, column=1, padx=10, pady=10)
ttk.Entry(window, textvariable=password).grid(row=1, column=1, padx=10, pady=10)
ttk.Button(window, text="로그인", command=check_data).grid(
    row=2, column=1, padx=10, pady=10
)
ttk.Button(window, text="회원가입", command=lambda: controller.show_frame("PageOne")).grid(
    row=2, column=1, padx=10, pady=10
)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family="Helvetica", size=18, weight="bold", slant="italic"
        )

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in PageOne:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


def show_frame(self, page_name):
    """Show a frame for the given page name"""
    frame = self.frames[page_name]
    frame.tkraise()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack()


window.mainloop()
