from tkinter import messagebox
import tkinter as tk
from numpy import place
import pbl_data1
import share_call
from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("600x600")
root.configure(bg="black")
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)
#
# label1 = Label(root,image=photo)
# label1.place(x=0,y=0)
def stag():
    messagebox.showinfo("STAGNANT", f"Stagnant amount: INR  {pbl_data1.stag}")
    return
def graph1():
    pbl_data1.graph()
    return
def expense():
    messagebox.showinfo("EXPENSE WINDOW", f'''
    Average expense: INR {int(pbl_data1.mean)}
    Suggested Potential Expenditure per day: INR {int(pbl_data1.expense/30)}/day"''')
    return
def suggest():
    global screen
    screen = Toplevel(root)
    string = share_call.response()
    screen.title("Login")
    screen.geometry("1300x300")
    Label(screen, text=f"{string}", font="time 15 ").pack()
    Label(screen, text="").pack()
    return
root.title("PROJECT ARTHA")
def runner(ch):
    if ch == 1:
        print("Stagnant data is:", pbl_data1.stag)
        messagebox.showinfo("STAGNANT", f"Stagnant amount: INR{pbl_data1.stag}")
        return
    if ch == 2:
        pbl_data1.graph()
        return
    if ch==3:
        messagebox.showinfo("EXPENSE WINDOW", f'''Average expense: INR {int(pbl_data1.mean)}
Suggested Potential Expenditure per day: INR {int(pbl_data1.expense/30)}/day"''')
        return
    if ch == 4:
        global screen
        screen=Toplevel(root)
        string=share_call.response()
        screen.title("Login")
        screen.geometry("1300x300")
        Label(screen, text=f"{string}",font="time 15 ").pack()
        Label(screen, text="").pack()
        return

    else:
        messagebox.showinfo("Exit", "Invalid option")
        return
def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    # Button(text="Generate", command=order).pack()


# def order():
#     # tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")
#     runner(int(var.get()))
#     print("ran")



def on_enter(e):
    e.widget['background'] = 'green'

def on_leave(e):
    e.widget['background'] = '#d7f542'





def run():
    import tkinter.messagebox as tmsg
    # var = IntVar()
    global var
    var=StringVar()
    var.set("Radio")
    # def on_enter(e):
    #     btn1['background']=bcolor
    # var.set(1)
    # Label(root, text="ARTHA", font="Helvetica 24 bold",fg="#FF0000",bg="black",
    # Label(root, text="ARTHA", font="Helvetica 24 bold",fg="#FF0000",bg="black",
    # Label(root, text="ARTHA", font="Helvetica 24 bold",fg="#FF0000",bg="black",
    # justify=LEFT, padx=14).pack()
    image = Image.open("artha.png")
    resized=image.resize((400,400))
    photo = ImageTk.PhotoImage(resized)
    label1 = Label(root, image=photo,border=0).pack()
    # radio = Radiobutton(root, text="Your stagnent data", padx=14, variable=var, value=1).pack(anchor="w")
    # radio = Radiobutton(root, text="Transaction analysis graph", padx=14, variable=var, value=2).pack(anchor="w")
    # radio = Radiobutton(root, text="Suggested Expense on daily basis", padx=14, variable=var, value=3).pack(anchor="w")
    # radio = Radiobutton(root, text="Share Recomendations", padx=14, variable=var, value=4).pack(anchor="w")
    # Button(text="Generate", command=order,fg="white",bg="blue",font="time 15 bold").pack()
    # btn1=Button(text="Stagnant", command=stag,fg="white",bg="blue",border=0,activeforeground="blue",activebackground="black",font="time 15 bold")
    # btn1.bind("<Enter>",on_enter)
    # Button(text="expense", command=expense,fg="white",bg="#d7f542",font="time 25").pack()
    # Button(text="Graph", command=graph1,fg="white",bg="#d7f542",font="time 15 bold").pack()
    # Button(text="suggest", command=suggest,fg="white",bg="#d7f542",font="time 15 bold").pack()
    # Button(text="QUIT", command=root.destroy, fg="white",bg="#d7f542").pack()
    myButton = tk.Button(root,text="Generate Stagnant Amount", command=stag,fg="black",bg="#d7f542",width=25,border=0,font="lucida 15 bold")
    myButton.pack(padx=30,pady=20)

    myButton.bind("<Enter>", on_enter)
    myButton.bind("<Leave>", on_leave)
    myButton2 = tk.Button(root,text="Expense per day", command=expense,fg="black",bg="#d7f542",width=25,font="lucida 15 bold")
    myButton2.pack(padx=30,pady=20)

    myButton2.bind("<Enter>", on_enter)
    myButton2.bind("<Leave>", on_leave)
    myButton3 = tk.Button(root, text="Transaction analysis Graph", command=graph1,fg="black",bg="#d7f542",width=25,font="lucida 15 bold")
    myButton3.pack(padx=30,pady=20)

    myButton3.bind("<Enter>", on_enter)
    myButton3.bind("<Leave>", on_leave)
    myButton4 = tk.Button(root, text="Stock Suggestions", command=suggest,fg="black",bg="#d7f542",width=25,font="lucida 15 bold")
    myButton4.pack(padx=30,pady=20)

    myButton4.bind("<Enter>", on_enter)
    myButton4.bind("<Leave>", on_leave)

    myButton5 = tk.Button(root,text ="QUIT", command=root.destroy, fg="black",bg="#d7f542",width=25,font="lucida 15 bold")
    myButton5.pack(padx=30,pady=20)

    myButton5.bind("<Enter>", on_enter)
    myButton5.bind("<Leave>", on_leave)

    # label_frame = LabelFrame(root, text='This is Label Frame',bg="#d7f542")
    # label_frame.pack(expand='yes', fill='both')
    label1 = Label(root, text='''Creator:  Abhinav | Aryan | Ayush | Himanshu |''', fg="red", bg="black", font="13")
    label1.place(x=5, y=711)
    label1 = Label(root, text='This project totally based on PBL and outer scope',fg="white",bg="black",font="13")
    label1.place(x=5, y=735)

    label1 = Label(root, text='@2022 PROJECT ARTHA, PBL.All rights reserved',fg="white",bg="black",font="13")
    label1.place(x=5, y=760)
    root.mainloop()
run()