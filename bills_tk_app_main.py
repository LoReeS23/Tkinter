from tkinter import *
from tkinter import messagebox
from db import Database

# app settings
app = Tk()
app.title('First tk App About Bills')
app.geometry('700x400')
db = Database('bills.db')

# texts
item_text = StringVar()
amount_bill = StringVar()
NIP_number = StringVar()
corporation_name_text = StringVar()
corporation_address_text = StringVar()
vat_option_text = StringVar()


# funcs
def bill():
    bill_labels_frame.lift()
    bill_options_frame.lift()
    chosen_type_of_bill.config(text='Paragon')
    NIP_label.config(state='disabled')
    corporation_name_label.config(state='disabled')
    corporation_address_label.config(state='disabled')


def invoice():
    bill_labels_frame.lift()
    bill_options_frame.lift()
    NIP_label.config(state='normal')
    corporation_name_label.config(state='normal')
    corporation_address_label.config(state='normal')
    chosen_type_of_bill.config(text='Faktura')


def clear_fields():
    item.delete(0, END)
    bill_entry.delete(0, END)
    corporation_name.delete(0, END)
    corporation_address.delete(0, END)
    NIP.delete(0, END)


def create_new_bill():
    if chosen_type_of_bill == "Faktura":
        pass
    db.insert_bills(item_text.get(), amount_bill.get(), vat_option_text.get())
    clear_fields()
    messagebox.showinfo('Dodano!', 'Rachunek dodany do bazy danych')


# frames
button_frame = Frame()
button_frame.pack(side='top', fill='x', expand=False)

bill_labels_frame = Frame()
bill_labels_frame.pack(side='left', fill='both', expand=True)

bill_options_frame = Frame()
bill_options_frame.place(relx=0.5, rely=0.5)

# buttons
button_bill = Button(button_frame, text='Paragon', command=bill)
button_invoice = Button(button_frame, text='Faktura', command=invoice)
button_other_bills = Button(button_frame, text='Rachunki')
button_create_bill = Button(bill_options_frame, text='Dodaj nowy rachunek', command=create_new_bill)
button_clear_all_fields = Button(bill_options_frame, text='Wyczysc wszystkie pola', command=clear_fields)

# labels
chosen_text = Label(button_frame, text='Wybrany typ rachunku: ')
chosen_type_of_bill = Label(button_frame, text="")
item_label = Label(bill_labels_frame, text="Przedmiot:")
bill_value_label = Label(bill_labels_frame, text='Wartosc rachunku:')
corporation_name_label = Label(bill_labels_frame, text='Nazwa firmy:')
corporation_address_label = Label(bill_labels_frame, text="Adres firmy:")
NIP_label = Label(bill_labels_frame, text="Numer NIP firmy:")
VAT_label = Label(bill_labels_frame, text="% podatku VAT:")

# entries
item = Entry(bill_labels_frame, textvariable=item_text)
bill_entry = Entry(bill_labels_frame, textvariable=amount_bill, selectforeground='red', width=10)
corporation_name = Entry(bill_labels_frame, textvariable=corporation_name_text, selectforeground='red')
corporation_address = Entry(bill_labels_frame, textvariable=corporation_address_text)
NIP = Entry(bill_labels_frame, textvariable=NIP_number, width=10)

# option lists
vat_option = OptionMenu(bill_labels_frame, vat_option_text, '8', '23')
vat_option_text.set('23')

# grids
button_bill.grid(column=0, row=1)
button_invoice.grid(column=1, row=1)
button_other_bills.grid(column=2, row=1)
chosen_text.grid(column=3, row=1)
chosen_type_of_bill.grid(column=4, row=1)
item_label.grid()
item.grid()
bill_value_label.grid()
bill_entry.grid()
corporation_name_label.grid()
corporation_name.grid()
corporation_address_label.grid()
corporation_address.grid()
NIP_label.grid()
NIP.grid()
VAT_label.grid()
vat_option.grid()
button_create_bill.grid()
button_clear_all_fields.grid()

# run
app.mainloop()
