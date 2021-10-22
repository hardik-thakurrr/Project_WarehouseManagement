from tkinter import *
import mysql.connector as my
from tkinter import messagebox
from tkinter.ttk import Treeview


def return_id():
    mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
    cur = mysql.cursor()
    cur.execute("select inventory_id from inventory")
    id_list = cur.fetchall()
    return id_list


def inventory_reset():
    warehouse.txtproduct_id.delete(0, 'end')
    warehouse.txtproduct_name.delete(0, 'end')
    warehouse.txtproduct_price.delete(0, 'end')
    warehouse.txtproduct_quantity.delete(0, 'end')
    warehouse.txtproduct_company.delete(0, 'end')
    warehouse.txtproduct_contact.delete(0, 'end')


def inventory_insert():
    sql_id = warehouse.txtproduct_id.get()
    sql_name = warehouse.txtproduct_name.get()
    sql_price = warehouse.txtproduct_price.get()
    sql_quantity = warehouse.txtproduct_quantity.get()
    sql_company = warehouse.txtproduct_company.get()
    sql_contact = warehouse.txtproduct_contact.get()

    var = return_id()
    validation_list = []
    for i in var:
        validation_list.append(i[0])

    if (sql_id == "" or sql_name == "" or sql_price == "" or sql_quantity == "" or sql_company == ""
            or sql_contact == ""):
        messagebox.showinfo("Warning", "All Fields are Required !!")

    elif int(sql_id) in validation_list:
        messagebox.showerror("Warning", "Enter Different Product ID !!")

    else:
        mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
        cur = mysql.cursor()
        cur.execute("insert into inventory values('" + sql_id + "', '" + sql_name + "', '" + sql_price + "', "
                    "'" + sql_quantity + "' , '" + sql_company + "', '" + sql_contact + "')")
        cur.execute("commit")
        inventory_show()
        messagebox.showinfo("Success", "Product Details Inserted !!")
        inventory_reset()
        mysql.close()


def inventory_delete():
    sql_id = warehouse.txtproduct_id.get()
    var = return_id()
    validation_list = []
    for i in var:
        validation_list.append(i[0])

    if sql_id == "":
        messagebox.showerror("Warning", "Product ID is Required !!")

    elif int(sql_id) in validation_list:
        mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
        cur = mysql.cursor()
        cur.execute("delete from inventory where inventory_id ='" + sql_id + "'")
        cur.execute("commit")

        inventory_show()
        messagebox.showinfo("Success", "Product Details Deleted !!")
        inventory_reset()
        mysql.close()
    else:
        messagebox.showerror("Warning", "Incorrect Product ID !!")


def inventory_update():
    sql_id = warehouse.txtproduct_id.get()
    sql_name = warehouse.txtproduct_name.get()
    sql_price = warehouse.txtproduct_price.get()
    sql_quantity = warehouse.txtproduct_quantity.get()
    sql_company = warehouse.txtproduct_company.get()
    sql_contact = warehouse.txtproduct_contact.get()
    var = return_id()
    validation_list = []
    for i in var:
        validation_list.append(i[0])

    if (sql_id == "" or sql_name == "" or sql_price == "" or sql_quantity == "" or sql_company == ""
            or sql_contact == ""):
        messagebox.showinfo("Warning", "All Fields are Required !!")

    elif int(sql_id) in validation_list:
        mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
        cur = mysql.cursor()
        cur.execute("update inventory set inventory_name='" + sql_name + "',"
                    " inventory_price='" + sql_price + "', inventory_quantity='" + sql_quantity + "' , "
                    " inventory_company='" + sql_company + "', inventory_retailer= '" + sql_contact
                    + "' where inventory_id='" + sql_id + "'")

        cur.execute("commit")
        inventory_show()
        messagebox.showinfo("Success", "Product Details Updated !!")
        inventory_reset()
        mysql.close()
    else:
        messagebox.showerror("Warning", "Incorrect Product ID !!")


def inventory_search():
    sql_id = warehouse.txtproduct_id.get()
    var = return_id()
    validation_list = []
    for i in var:
        validation_list.append(i[0])

    if sql_id == "":
        messagebox.showerror("Warning", "Product ID is Required !!")

    elif int(sql_id) in validation_list:
        mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
        cur = mysql.cursor()
        cur.execute("select * from inventory where inventory_id ='" + sql_id + "'")
        row_details = cur.fetchall()

        for row in row_details:
            warehouse.txtproduct_name.insert(0, row[1])
            warehouse.txtproduct_price.insert(0, row[2])
            warehouse.txtproduct_quantity.insert(0, row[3])
            warehouse.txtproduct_company.insert(0, row[4])
            warehouse.txtproduct_contact.insert(0, row[5])

        messagebox.showinfo("Success", "Product Details Found !!")
        mysql.close()
    else:
        messagebox.showerror("Warning", "Incorrect Product ID !!")


def inventory_show():
    mysql = my.connect(host='localhost', user='root', passwd='', database='warehouse_database')
    cur = mysql.cursor()
    cur.execute("select * from inventory")
    row_details = cur.fetchall()
    if len(row_details) != 0:
        warehouse.treev.delete(*warehouse.treev.get_children())
    for row in row_details:
        warehouse.treev.insert("", 'end', text="L1",
                               values=(row[0], row[1], row[2], row[3], row[4]))
    mysql.close()


def warehouse():
    window = Tk()

    window.title("Warehouse Product Management System")
    window.geometry("1550x780+0+0")
    bg_colour = "#074463"

    Label(window, text="Warehouse Product Management System", bd=12, relief=GROOVE, bg=bg_colour, fg="white",
          font=("Times New Roman", 35, "bold"), pady=2).pack(fill=X)

    operation_frame = LabelFrame(window, text="Operations", fg="Gold", font=("Times New Roman", 23, "bold"),
                                 bd=3, bg=bg_colour, height=15)
    operation_frame.place(x=0, y=80, relwidth=1)

    button_show = Button(operation_frame, text="Show", font=("Times New Roman", 25, "bold"), height=1,
                         width=8, bd=4, padx=2, command=inventory_show)
    button_show.grid(row=0, column=5, padx=20, pady=5)

    button_save = Button(operation_frame, text="Save", font=("Times New Roman", 25, "bold"), height=1,
                         width=8, bd=4, padx=2, command=inventory_insert)
    button_save.grid(row=0, column=0, padx=20, pady=5)

    button_reset = Button(operation_frame, text="Reset", font=("Times New Roman", 25, "bold"), height=1,
                          width=8, bd=4, padx=2, command=inventory_reset)
    button_reset.grid(row=0, column=4, padx=20, pady=5)

    button_delete = Button(operation_frame, text="Delete", font=("Times New Roman", 25, "bold"), height=1,
                           width=8, bd=4, padx=2, command=inventory_delete)
    button_delete.grid(row=0, column=1, padx=20, pady=5)

    button_search = Button(operation_frame, text="Search", font=("Times New Roman", 25, "bold"), height=1,
                           width=8, bd=4, padx=2, command=inventory_search)
    button_search.grid(row=0, column=2, padx=20, pady=5)

    button_update = Button(operation_frame, text="Update", font=("Times New Roman", 25, "bold"), height=1,
                           width=8, bd=4, padx=2, command=inventory_update)
    button_update.grid(row=0, column=3, padx=20, pady=5)

    button_close = Button(operation_frame, text="Close", font=("Times New Roman", 25, "bold"), height=1,
                          width=8, bd=4, padx=2, command=window.destroy)
    button_close.grid(row=0, column=6, padx=20, pady=5)

    Label(operation_frame, bg=bg_colour).grid(row=1, column=1)
    # ********************************* body *********************************

    productEntry_frame = LabelFrame(window, text="Product Entries", fg="Gold", bd=3,
                                    font=("Times New Roman", 23, "bold"), bg=bg_colour, width=765, height=600)
    productEntry_frame.place(x=0, y=220)

    productDisplay_frame = LabelFrame(window, text="Product Details", fg="Gold", bd=3,
                                      font=("Times New Roman", 23, "bold"), bg=bg_colour, width=770, height=600)
    productDisplay_frame.place(x=765, y=220)

    left_border = Label(productEntry_frame, bd=12, padx=30, width=95, height=27,
                        pady=50, bg=bg_colour, relief=RIDGE)
    left_border.place(x=5, y=8)

    right_border = Label(productDisplay_frame, bd=12, padx=30, width=96, height=27,
                         pady=50, bg=bg_colour, relief=RIDGE)
    right_border.place(x=7, y=8)

    # ********************************** Left Body Frame **********************************
    left_body = Frame(window, width=722, height=503, padx=30, pady=50, bg=bg_colour, relief=RIDGE)
    left_body.place(x=20, y=278)
    # Product ID
    labelproduct_id = Label(left_body, font=("Times New Roman", 20, "bold"), bg=bg_colour,
                            text="Product ID:", fg="White")
    labelproduct_id.place(x=20, y=0)
    warehouse.txtproduct_id = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_id.place(x=250, y=5)
    # Product Name
    labelproduct_name = Label(left_body, font=("Times New Roman", 20, "bold"),
                              text="Product Name:", bg=bg_colour, fg="white")
    labelproduct_name.place(x=20, y=60)
    warehouse.txtproduct_name = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_name.place(x=250, y=65)
    # Product Price
    labelproduct_price = Label(left_body, font=("Times New Roman", 20, "bold"), text="Product Price:",
                               bg=bg_colour, fg="white")
    labelproduct_price.place(x=20, y=120)
    warehouse.txtproduct_price = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_price.place(x=250, y=125)
    # Product Quantity
    labelproduct_quantity = Label(left_body, font=("Times New Roman", 20, "bold"), text="Product Quantity:",
                                  bg=bg_colour, fg="white")
    labelproduct_quantity.place(x=20, y=180)
    warehouse.txtproduct_quantity = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_quantity.place(x=250, y=185)
    # Product Company
    labelproduct_company = Label(left_body, font=("Times New Roman", 20, "bold"), text="Product Company:",
                                 bg=bg_colour, fg="white")
    labelproduct_company.place(x=20, y=240)
    warehouse.txtproduct_company = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_company.place(x=250, y=246)
    # Product Contact
    labelproduct_contact = Label(left_body, font=("Times New Roman", 20, "bold"), text="Retailer Name:",
                                 bg=bg_colour, fg="white")
    labelproduct_contact.place(x=20, y=300)
    warehouse.txtproduct_contact = Entry(left_body, font=("Times New Roman", 15, "bold"), width=35)
    warehouse.txtproduct_contact.place(x=250, y=305)

    # ********************************** Right Body Frame **********************************
    right_body = Frame(window, width=730, height=503, padx=30, pady=50, bg=bg_colour, relief=RIDGE)
    right_body.place(x=787, y=278)

    warehouse.treev = Treeview(right_body, selectmode='extended', height=13)

    warehouse.treev.place(x=45, y=40)

    warehouse.treev["columns"] = ("1", "2", "3", "4", "5")

    warehouse.treev['show'] = 'headings'

    warehouse.treev.column("1", width=120, anchor='w')
    warehouse.treev.column("2", width=120, anchor='w')
    warehouse.treev.column("3", width=120, anchor='w')
    warehouse.treev.column("4", width=120, anchor='w')
    warehouse.treev.column("5", width=120, anchor='w')

    warehouse.treev.heading("1", text="Product ID")
    warehouse.treev.heading("2", text="Product Name")
    warehouse.treev.heading("3", text="Product Price")
    warehouse.treev.heading("4", text="Product Quantity")
    warehouse.treev.heading("5", text="Product Company")
    window.mainloop()
