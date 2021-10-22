from Warehouse_Main import *

w = Tk()
w.geometry('450x600')
w.title(' L O G I N ')
w.resizable(0, 0)

# Making gradient frame
j = 0
r = 10
for i in range(100):
    c = str(222222 + r)
    Frame(w, width=10, height=600, bg="#" + c).place(x=j, y=0)
    j = j + 10
    r = r + 1

Frame(w, width=250, height=400, bg='white').place(x=100, y=90)

l1 = Label(w, text='Username', bg='white')
l = ('Consolas', 13)
l1.config(font=l)
l1.place(x=130, y=230)

# e1 entry for username entry
e1 = Entry(w, width=20, border=0)
l = ('Consolas', 13)
e1.config(font=l)
e1.place(x=130, y=260)

# e2 entry for password entry
e2 = Entry(w, width=20, border=0, show='*')
e2.config(font=l)
e2.place(x=130, y=360)

l2 = Label(w, text='Password', bg='white')
l = ('Consolas', 13)
l2.config(font=l)
l2.place(x=130, y=330)

# lineframe on entry

Frame(w, width=180, height=2, bg='#141414').place(x=130, y=382)
Frame(w, width=180, height=2, bg='#141414').place(x=130, y=282)

imageb = PhotoImage(file="log.PNG")

label1 = Label(image=imageb,
               border=0,

               justify=CENTER)

label1.place(x=165, y=90)


# Command
def cmd():
    if e1.get() == 'admin' and e2.get() == 'admin123':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
        w.destroy()
        warehouse()

    else:
        messagebox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")


# Button_with hover effect
def bttn(x, y, text, ecolor, lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor  # ffcc66
        myButton1['foreground'] = lcolor  # 000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground'] = ecolor

    myButton1 = Button(w, text=text,
                       width=20,
                       height=2,
                       fg=ecolor,
                       border=0,
                       bg=lcolor,
                       activeforeground=lcolor,
                       activebackground=ecolor,
                       command=cmd)

    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=150, y=425)


bttn(100, 375, 'L O G I N', 'white', '#994422')

w.mainloop()
