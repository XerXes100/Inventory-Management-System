from datetime import date
import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourMySQLPassword",
    database="dbms_project"
)

mycursor = mydb.cursor()


def login_user():
    employee_username = empid_entry.get()
    employee_password = password_entry.get()
    mycursor.execute('select * from employee where emp_id=%s and emp_pass=%s;', (employee_username, employee_password,))
    mycursor.fetchall()
    if mycursor.rowcount == 1:
        def inventory():
            inventory_window = Toplevel(newWindow)
            item_id = Label(inventory_window, text='ITEM ID')
            item_id.grid(row=0, column=0)

            iname = Label(inventory_window, text='ITEM NAME')
            iname.grid(row=0, column=1)

            idec = Label(inventory_window, text='ITEM DESCRIPTION')
            idec.grid(row=0, column=2)

            ip = Label(inventory_window, text='ITEM PRICE')
            ip.grid(row=0, column=3)

            qs = Label(inventory_window, text='QUANTITY IN STOCK')
            qs.grid(row=0, column=4)

            mycursor.execute("select * from product_inventory")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(inventory_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            btn = Button(inventory_window, text="Add product", command=lambda: add_product())
            btn.grid(row=i + 2, column=1)

            btn = Button(inventory_window, text="Delete product", command=lambda: remove_product())
            btn.grid(row=i + 2, column=2)

            btn = Button(inventory_window, text="Restock inventory", command=lambda: restock())
            btn.grid(row=i + 2, column=3)

        def add_product():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("500x300")
            l1 = Label(insertWindow, text="Enter Item Name")
            l1.place(x=20, y=20)

            l1 = Label(insertWindow, text="Enter Item Description")
            l1.place(x=20, y=80)

            l1 = Label(insertWindow, text="Enter Item Price")
            l1.place(x=20, y=140)

            l1 = Label(insertWindow, text="Enter Quantity")
            l1.place(x=20, y=200)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            e2 = Entry(insertWindow)
            e2.place(x=200, y=80)

            e3 = Entry(insertWindow)
            e3.place(x=200, y=140)

            e4 = Entry(insertWindow)
            e4.place(x=200, y=200)

            insert_into = Button(insertWindow, text='INSERT INTO INVENTORY',
                                 command=lambda: insert_values_inventory(e1.get(), e2.get(), e3.get(), e4.get()))
            insert_into.place(x=300, y=270)

        def insert_values_inventory(iname, idesc, iprice, iqu):
            mycursor.execute('insert into product_inventory(item_name, item_description, item_price, quantity_in_stock)'
                             ' values(%s, %s, %s, %s)', (iname, idesc, iprice, iqu))
            mydb.commit()

        def remove_product():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("300x300")
            l1 = Label(insertWindow, text="Enter Item ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            insert_into = Button(insertWindow, text='DELETE',
                                 command=lambda: delete_product(e1.get()))
            insert_into.place(x=60, y=80)

        def delete_product(item_id):
            mycursor.execute('delete from product_inventory where item_id=%s', (item_id,))
            mydb.commit()

        def restock():
            anotherWindow = Toplevel(newWindow)
            anotherWindow.geometry('500x200')
            lbl = Label(anotherWindow, text="Enter ITEM ID to be restocked")
            lbl.place(x=20, y=20)

            en = Entry(anotherWindow)
            en.place(x=250, y=20)

            bt = Button(anotherWindow, text="Restock", command=lambda: restock_query(en.get()))
            bt.place(x=150, y=75)

        def restock_query(item_id):
            mycursor.execute(
                'update product_inventory set quantity_in_stock = quantity_in_stock + 50 where item_id = %s',
                (item_id,))
            mydb.commit()

        def order_lists():
            order_window = Toplevel(newWindow)

            order_id = Label(order_window, text='ORDER ID')
            order_id.grid(row=0, column=0)

            od = Label(order_window, text='ORDER DATE')
            od.grid(row=0, column=1)

            tp = Label(order_window, text='TOTAL PRICE')
            tp.grid(row=0, column=2)

            ui = Label(order_window, text='USER ID')
            ui.grid(row=0, column=3)

            mycursor.execute("select * from orders")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(order_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            lbl = Label(order_window, text="Enter Order ID to view")
            lbl.grid(row=i + 3, column=1)
            order_entry = Entry(order_window, width=10)
            order_entry.grid(row=i + 3, column=2)
            btn = Button(order_window, text="OHKK", command=lambda: show_order(order_entry.get()))
            btn.grid(row=i + 3, column=3)

            create_user = Button(order_window, text='ADD ORDER', command=lambda: insert_order())
            create_user.grid(row=i + 3, column=0)

        def show_order(oid):
            so_window = Toplevel(newWindow)
            oii = Label(so_window, text='ORDER ITEM ID')
            oii.grid(row=0, column=0)

            ii = Label(so_window, text='ITEM ID')
            ii.grid(row=0, column=1)

            oi = Label(so_window, text='ORDER ID')
            oi.grid(row=0, column=2)

            qo = Label(so_window, text='QUANTITY ORDERED')
            qo.grid(row=0, column=3)

            it_nm = Label(so_window, text='ITEM NAME')
            it_nm.grid(row=0, column=4)

            it_ds = Label(so_window, text='ITEM DESCRIPTION')
            it_ds.grid(row=0, column=5)

            ip = Label(so_window, text='ITEM PRICE')
            ip.grid(row=0, column=6)

            mycursor.execute(
                "select contain.order_item_id, contain.item_id, contain.order_id, contain.quantity_ordered,"
                " product_inventory.item_name, product_inventory.item_description, product_inventory.item_price"
                " from contain inner join product_inventory on contain.item_id = product_inventory.item_id"
                " where order_id=%s", (oid,)
            )

            l = 1
            for x in mycursor.fetchall():
                for y in range(len(x)):
                    e = Entry(so_window, width=10, fg='blue')
                    e.grid(row=l, column=y)
                    e.insert(END, x[y])
                l = l + 1

            lbl = Label(so_window, text="Enter Order ITEM ID to be completed")
            lbl.grid(row=l + 1, column=3)
            order_update = Entry(so_window, width=10)
            order_update.grid(row=l + 2, column=3)
            btn = Button(so_window, text="OHKK", command=lambda: update_inventory(order_update.get()))
            btn.grid(row=l + 3, column=3)

        def insert_order():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("400x300")

            l1 = Button(insertWindow, text="Add items", command=lambda: items_insert())
            l1.place(x=20, y=20)

            l1 = Label(insertWindow, text="Enter Total Order Price")
            l1.place(x=20, y=80)

            l1 = Label(insertWindow, text="Enter User ID")
            l1.place(x=20, y=140)

            e4 = Entry(insertWindow)
            e4.place(x=200, y=80)

            e5 = Entry(insertWindow)
            e5.place(x=200, y=140)

            insert_into = Button(insertWindow, text='ADD',
                                 command=lambda: insert_values_orders(e4.get(), e5.get(), item_id_list,
                                                                      quantity_ordered_list))
            insert_into.place(x=200, y=200)

        def insert_values_orders(oprice, uid, item_list, quantity_list):
            odate = date.today()
            print(odate)
            mycursor.execute('INSERT INTO orders(order_date, total_price, user_id) VALUES(%s,%s,%s)',
                             (odate, oprice, uid,))
            mydb.commit()

            mycursor.execute('select order_id from orders order by order_id desc limit 1')
            oid = mycursor.fetchall()[0][0]

            for i in range(0, len(item_list)):
                mycursor.execute('insert into contain(order_id, item_id, quantity_ordered) values(%s, %s, %s)',
                                 (oid, item_list[i], quantity_list[i]))
            mydb.commit()
            item_id_list.clear()
            quantity_ordered_list.clear()

        item_id_list = []
        quantity_ordered_list = []

        def items_insert():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("600x300")
            l1 = Label(insertWindow, text="Enter ITEM ID")
            l1.place(x=20, y=20)

            a = Entry(insertWindow)
            a.place(x=150, y=20)

            l2 = Label(insertWindow, text="Enter QUANTITY ORDERED")
            l2.place(x=20, y=60)

            b = Entry(insertWindow)
            b.place(x=200, y=60)

            items = Button(insertWindow, text="OHKK", command=lambda: fetch_item_id(a.get(), b.get()))
            items.place(x=20, y=150)

        def fetch_item_id(item_id, quantity_ordered):
            item_id_list.append(item_id)
            quantity_ordered_list.append(quantity_ordered)

        def update_inventory(order_item_id):
            mycursor.execute('select item_id, order_id, quantity_ordered from contain where order_item_id=%s',
                             (order_item_id,))
            item_id, order_id, quantity_ordered = mycursor.fetchall()[0]

            mycursor.execute('select quantity_in_stock from product_inventory where item_id = %s', (item_id,))
            quantity_in_stock = mycursor.fetchall()[0][0]

            if quantity_in_stock >= quantity_ordered:
                mycursor.execute(
                    'update product_inventory set quantity_in_stock = quantity_in_stock - %s where item_id = %s',
                    (quantity_ordered, item_id,))
                mydb.commit()

                mycursor.execute('select count(*) from contain where order_id=%s', (str(order_id),))
                rows = mycursor.fetchall()[0][0]
                if rows == 1:
                    mycursor.execute('delete from orders where order_id=%s', (order_id,))
                    mydb.commit()
                mycursor.execute('delete from contain where order_item_id=%s', (order_item_id,))
                mydb.commit()

            else:
                MessageBox.showwarning('Error', 'Required quantity not available')

            # mycursor.execute('select * from product_inventory')
            # for x in mycursor.fetchall():
            #     print(x)

        def users():
            userWindow = Toplevel(newWindow)

            uid = Label(userWindow, text='USER ID')
            uid.grid(row=0, column=0)

            fname = Label(userWindow, text='FIRST NAME')
            fname.grid(row=0, column=1)

            lname = Label(userWindow, text='LAST NAME')
            lname.grid(row=0, column=2)

            uadd = Label(userWindow, text='USER ADDRESS')
            uadd.grid(row=0, column=3)

            mycursor.execute("select * from users")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(userWindow, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            create_user = Button(userWindow, text='ADD USER', command=lambda: insert_user())
            create_user.grid(row=1, column=6)

            del_user = Button(userWindow, text='DELETE USER', command=lambda: delete_user())
            del_user.grid(row=2, column=6)

        def insert_user():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("500x300")
            l1 = Label(insertWindow, text="Enter User's first name")
            l1.place(x=20, y=20)

            l1 = Label(insertWindow, text="Enter User's last name")
            l1.place(x=20, y=80)

            l1 = Label(insertWindow, text="Enter User's address")
            l1.place(x=20, y=140)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            e2 = Entry(insertWindow)
            e2.place(x=200, y=80)

            e3 = Entry(insertWindow)
            e3.place(x=200, y=140)

            insert_into = Button(insertWindow, text='INSERT',
                                 command=lambda: insert_values_users(e1.get(), e2.get(), e3.get()))
            insert_into.place(x=300, y=270)

        def insert_values_users(ufname, ulname, uadd):
            mycursor.execute('INSERT INTO users(user_fname, user_lname, user_address) VALUES(%s,%s,%s)',
                             (ufname, ulname, uadd,))
            mydb.commit()

        def delete_user():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("500x300")
            l1 = Label(insertWindow, text="Enter User ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            insert_into = Button(insertWindow, text='DELETE',
                                 command=lambda: remove_user(e1.get()))
            insert_into.place(x=60, y=80)

        def remove_user(user_id):
            mycursor.execute('delete from users where user_id=%s', (user_id,))
            mydb.commit()

        newWindow = Tk()
        newWindow.geometry("800x300")

        show_inventory = Button(newWindow, text="Show Inventory", command=inventory)
        show_inventory.place(x=20, y=20)

        show_order_lists = Button(newWindow, text='Show order lists', command=order_lists)
        show_order_lists.place(x=150, y=20)

        show_users = Button(newWindow, text='Show users', command=users)
        show_users.place(x=300, y=20)

    else:
        print(mycursor.rowcount)
        MessageBox.showwarning('Error', 'Invalid login credentials')


root = Tk()
root.geometry("600x300")
root.title('Inventory Management')

empid = Label(root, text="Enter Employee ID: ")
empid.place(x=20, y=20)

password = Label(root, text="Enter password: ")
password.place(x=20, y=50)

empid_entry = Entry(root)
empid_entry.place(x=150, y=20)

password_entry = Entry(root, show='*')
password_entry.place(x=150, y=50)

login_button = Button(root, text="Login", command=login_user, height=2, width=7)
login_button.place(x=170, y=130)

root.mainloop()