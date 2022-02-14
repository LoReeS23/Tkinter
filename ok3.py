from tkinter import *

# app settings
app = Tk()
app.title('First tk App About Bills')
app.geometry('700x400')

# texts
amount_bill = StringVar()
NIP_number = StringVar()
corporation_name_text = StringVar()


# funcs
def bill():
    chosen_type_of_bill.config(text='Paragon')
    NIP_label.config(state='disabled')
    corporation_name_label.config(state='disabled')


def invoice():
    NIP_label.config(state='normal')
    corporation_name_label.config(state='normal')
    chosen_type_of_bill.config(text='Faktura')


def clear_fields():
    bill_entry.delete(0, END)
    corporation_name.delete(0, END)
    NIP.delete(0, END)


def create_new_bill():
    if chosen_type_of_bill == "":
        pass
    pass


# buttons
button_frame = Frame(app)
button_frame.pack(side='top', fill='x')
button_bill = Button(button_frame, text='Paragon', command=bill)
button_invoice = Button(button_frame, text='Faktura', command=invoice)
button_other_bills = Button(button_frame, text='Rachunki')
bill_options_frame = Frame()
bill_options_frame.pack(side='bottom', fill='y')
button_create_bill = Button(bill_options_frame, text='Dodaj nowy rachunek', command=create_new_bill)
button_clear_all_fields = Button(bill_options_frame, text='Wyczysc wszystkie pola', command=clear_fields)

# labels
bill_labels_frame = Frame()
bill_labels_frame.pack(side='left', fill='x')

chosen_text = Label(button_frame, text='Wybrany typ rachunku: ')
chosen_type_of_bill = Label(button_frame, text="")
bill_value_label = Label(bill_labels_frame, text='Wartosc rachunku:')
corporation_name_label = Label(bill_labels_frame, text='Nazwa firmy:')
NIP_label = Label(bill_labels_frame, text="Numer NIP:")

# entries
bill_entry = Entry(bill_labels_frame, textvariable=amount_bill, selectforeground='red', width=10)
corporation_name = Entry(bill_labels_frame, textvariable=corporation_name_text, selectforeground='red')
NIP = Entry(bill_labels_frame, textvariable=NIP_number, width=10)

# grids
button_bill.grid(column=0, row=1)
button_invoice.grid(column=1, row=1)
button_other_bills.grid(column=2, row=1)
chosen_text.grid(column=3, row=1)
chosen_type_of_bill.grid(column=4, row=1)
bill_value_label.grid()
bill_entry.grid()
corporation_name_label.grid()
corporation_name.grid()
NIP_label.grid()
NIP.grid()
button_create_bill.grid()
button_clear_all_fields.grid()

# run
app.mainloop()
