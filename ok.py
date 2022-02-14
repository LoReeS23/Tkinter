from tkinter import *
from db import Database

# db
my_db = Database('simple_db.db')

# app settings
app = Tk()
app.title('First tk App')
app.geometry('700x400')


# funcs

def show_everything_on_list():
    for row in my_db.fetch():
        lst.insert(END, row)


def clear_text():
    entry.delete(0, END)


def add_item():
    my_db.insert(text.get())
    lst.delete(0, END)
    clear_text()
    show_everything_on_list()


text = StringVar()
label1 = Label(app, text='Text field', font=('bold', 14))
label1.grid(row=0, column=0)
label2 = Label(app, text='List', font=('bold', 14))
label2.grid(row=1, column=2)
entry = Entry(app, textvariable=text)
entry.grid(row=0, column=1)
lst = Listbox(app, height=17, width=50, border=1)
lst.grid(row=4, column=2)
# creating and connecting scroll to list
scroll = Scrollbar(app)
scroll.grid(row=4, column=3)
lst.configure(yscrollcommand=scroll.set)
scroll.configure(command=lst.yview)

# buttons
add_value_btn = Button(app, text='Add', command=add_item)
add_value_btn.grid(row=5, column=2)

# app runner
show_everything_on_list()
app.mainloop()
