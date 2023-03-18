from tkinter import*
from PIL import Image , ImageTk
from tkinter import ttk,messagebox
import sqlite3
class reportClass :
    def __init__(self,root):
        self.root = root
        self.root.title("Student DBMS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="pink")
        self.root.focus_force()

        title=Label(self.root,text="RGIT : View Student Result Details",font=("goudy old style",20,"bold"),bg="yellow",fg="black").place(x=10,y=15,width=1180,height=35)
#======Search=======
        self.var_search=StringVar()
        lbl_search = Label(self.root,text="Search by Roll no.:",font=("times new roman",20,"bold"),bg="white").place(x=150,y=100,height=40)
        txt_search = Entry(self.root,text="Select Student",font=("times new roman",20,"bold"),bg="white").place(x=400,y=100,height=40)
        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2").place(x=620,y=100,width=100,height=40)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="grey",fg="white",cursor="hand2").place(x=740,y=100,width=100,height=40)


if __name__ ==  "__main__":
    root=Tk()
    obj = reportClass(root)
    root.mainloop()
