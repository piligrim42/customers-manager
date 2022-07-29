from sqlite3 import Row
from tkinter import *

from tkinter import messagebox

from db import Database

db = Database('customers.db')


def populate_list():
    customers_list.delete(0, END)
    for row in db.fetch():
        customers_list.insert(END, row)


def add_item():
    if CustomerN_text.get() =='' or CustomerL_text.get()=='' or Address_text.get()=='' or Telephone_text.get()=='':
        messagebox.showerror('Required Fields', 'Please fill all fields')
        return


    db.insert(CustomerN_text.get(), CustomerL_text.get(), 
                Address_text.get(), Telephone_text.get())
    customers_list.delete(0,END)
    customers_list.insert(END, (CustomerN_text.get(), CustomerL_text.get(), 
                Address_text.get(), Telephone_text.get()))
    populate_list()


def select_item(event):
    try: 
        global selected_item
        index = customers_list.curselection()[0]
        selected_item = customers_list.get(index)
        print(selected_item)

        CustomerN_entry.delete(0, END)
        CustomerN_entry.insert(END, selected_item[1])
        CustomerL_entry.delete(0, END)
        CustomerL_entry.insert(END, selected_item[2])
        Address_entry.delete(0, END)
        Address_entry.insert(END, selected_item[3])
        Telephone_entry.delete(0, END)
        Telephone_entry.insert(END, selected_item[4])
    except IndexError:
        pass

   

def remove_item():
    db.remove(selected_item[0])
    populate_list()


def update_item():
    db.update(selected_item[0], CustomerN_text.get(), CustomerL_text.get(), 
                Address_text.get(), Telephone_text.get())
    populate_list()


def clear_text():
    CustomerN_entry.delete(0, END)
    CustomerL_entry.delete(0, END)
    Address_entry.delete(0, END)
    Telephone_entry.delete(0, END)
    







#Create window object
app = Tk()
app.title('Менеджер клиентской базы')
app.geometry('700x350')



#Part First Name
CustomerN_text = StringVar()
CustomerN_label = Label(app, text='Имя', pady=20)
CustomerN_label.grid(row=0, column=0, sticky=W)
CustomerN_entry = Entry(app, textvariable=CustomerN_text)
CustomerN_entry.grid(row=0, column=1)

#Customer Last Name
CustomerL_text = StringVar()
CustomerL_label = Label(app, text='Фамилия')
CustomerL_label.grid(row=0, column=2, sticky=W)
CustomerL_entry = Entry(app, textvariable=CustomerL_text)
CustomerL_entry.grid(row=0, column=3)

#Address
Address_text = StringVar()
Address_label = Label(app, text='Адрес')
Address_label.grid(row=1, column=0, sticky=W)
Address_entry = Entry(app, textvariable=Address_text)
Address_entry.grid(row=1, column=1)

#Telephone
Telephone_text = StringVar()
Telephone_label = Label(app, text='Телефон')
Telephone_label.grid(row=1, column=2, sticky=W)
Telephone_entry = Entry(app, textvariable=Telephone_text)
Telephone_entry.grid(row=1, column=3)


#Customer list
customers_list = Listbox(app, height=30, width=70, border=0)
customers_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3, ipady=70)

#Set scrollbar
customers_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=customers_list.yview)

#Bind Select 
customers_list.bind('<<ListboxSelect>>', select_item)


#Buttons

add_btn = Button(app, text='Добавить', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Удалить', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Обновить', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Очистить поле', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)




#Populate data
populate_list()

#Start program
app.mainloop()








