from tkinter import *
import backend

database = backend.Database("books.db")


class Executer:

    @staticmethod
    def get_selected_row(event):
        try:
            global selected_tuple
            index = list1.curselection()[0]
            selected_tuple = list1.get(index)
            e1.delete(0, END)
            e1.insert(END, selected_tuple[1])
            e2.delete(0, END)
            e2.insert(END, selected_tuple[2])
            e3.delete(0, END)
            e3.insert(END, selected_tuple[3])
            e4.delete(0, END)
            e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    @staticmethod
    def view_command():
        list1.delete(0, END)
        for row in database.view():
            list1.insert(END, row)

    @staticmethod
    def search_command():
        list1.delete(0, END)
        for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list1.insert(END, row)

    @staticmethod
    def add_command():
        list1.delete(0, END)
        database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

    @staticmethod
    def delete_command():
        database.delete(selected_tuple[0])

    @staticmethod
    def update_command():
        database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvar=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvar=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvar=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvar=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=32)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', Executer.get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, columnspan=1)

list1.config(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12, command=Executer.view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=Executer.search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=Executer.add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=Executer.update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=Executer.delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
