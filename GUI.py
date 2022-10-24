"""
Carly Raskin
COMP 3421
Assignment 1

"""

import mysql.connector
import tkinter as tk
from tkinter import ttk
import RaskinCarly_Assignment1_DAO as dao

""" Class Henry Search By Author """
class HenrySBA:

    def comCallback(self, event):
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))
        authorIndex = self.authorList[selIndex]
        self.bookList = self.data.byAuthor(authorIndex.id)
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2.grid(column=2, row=6)
        com2['values'] = self.bookList
        com2.current(0)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = self.bookList[0].price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride()

    def callBackAgain(self, event):
        selIndex = event.widget.current()
        titleIndex = self.bookList[selIndex]
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = titleIndex.price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride(selIndex)


    def treeOverride(self, i = 0):
        currBook = self.bookList[i]
        book = self.data.authorBranch(currBook.id)
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in book:
            tree1.insert("", "end", values=[row.branch, row.number])


    def __init__(self, frame):
        self.frame = frame
        self.data = dao.HenryDAO()

        self.authorList = self.data.listAuthors()
        self.bookList = self.data.byAuthor(self.authorList[0].id)
        self.branchList = self.data.authorBranch(self.bookList[0].id)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Search by Author')

        # Combobox
        com1 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com1.grid(column=1, row=6)
        com2.grid(column=2, row=6)
        com1['values'] = self.authorList
        hi = self.data.byAuthor(self.authorList[0].id)
        com2['values'] = hi
        com1.current(0)
        com2.current(0)
        com1.bind("<<ComboboxSelected>>", self.comCallback)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)

        # Labels
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = hi[0].price
        lab1['text'] = "Price: $" + str(self.price)
        lab2 = ttk.Label(self.tab1)
        lab2.grid(column = 1, row = 5)
        lab2['text'] = 'Author Selection'
        lab3 = ttk.Label(self.tab1)
        lab3.grid(column=2, row=5)
        lab3['text'] = 'Book Selection'

        # Tree
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in self.branchList:
            print(row.__class__)
            print(row)
            tree1.insert("", "end", values=[row.branch,row.number])





""" Class Henry Search By Category """

class HenrySBC:

    def comCallback(self, event):
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))
        catIndex = self.catList[selIndex]
        self.bookList = self.data.byCategory(catIndex.category)
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2.grid(column=2, row=6)
        com2['values'] = self.bookList
        com2.current(0)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = self.bookList[0].price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride()

    def callBackAgain(self, event):
        selIndex = event.widget.current()
        titleIndex = self.bookList[selIndex]
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = titleIndex.price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride(selIndex)


    def treeOverride(self, i = 0):
        currBook = self.bookList[i]
        book = self.data.authorBranch(currBook.id)
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in book:
            tree1.insert("", "end", values=[row.branch, row.number])


    def __init__(self, frame):
        self.frame = frame
        self.data = dao.HenryDAO()

        self.catList = self.data.categoryList()
        self.bookList = self.data.byCategory(self.catList[0].category)
        self.branchList = self.data.authorBranch(self.bookList[0].id)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Search by Category')

        # Combobox
        com1 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com1.grid(column=1, row=6)
        com2.grid(column=2, row=6)
        com1['values'] = self.catList
        hi = self.data.byCategory(self.catList[0].category)
        com2['values'] = hi
        com1.current(0)
        com2.current(0)
        com1.bind("<<ComboboxSelected>>", self.comCallback)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)

        # Labels
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = hi[0].price
        lab1['text'] = "Price: $" + str(self.price)
        lab2 = ttk.Label(self.tab1)
        lab2.grid(column = 1, row = 5)
        lab2['text'] = 'Category Selection'
        lab3 = ttk.Label(self.tab1)
        lab3.grid(column=2, row=5)
        lab3['text'] = 'Book Selection'

        # Tree
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in self.branchList:
            print(row.__class__)
            print(row)
            tree1.insert("", "end", values=[row.branch,row.number])

"""Class Henry Search by Publisher """

class HenrySBP:

    def comCallback(self, event):
        selIndex = event.widget.current()
        print("Index selected is: " + str(selIndex))
        pubIndex = self.publisherList[selIndex]
        self.bookList = self.data.byPub(pubIndex.id)
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2.grid(column=2, row=6)
        com2['values'] = self.bookList
        com2.current(0)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = self.bookList[0].price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride()

    def callBackAgain(self, event):
        selIndex = event.widget.current()
        titleIndex = self.bookList[selIndex]
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = titleIndex.price
        lab1['text'] = "Price: $" + str(self.price)
        self.treeOverride(selIndex)


    def treeOverride(self, i = 0):
        currBook = self.bookList[i]
        book = self.data.authorBranch(currBook.id)
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in book:
            tree1.insert("", "end", values=[row.branch, row.number])


    def __init__(self, frame):
        self.frame = frame
        self.data = dao.HenryDAO()

        self.publisherList = self.data.pubList()
        self.bookList = self.data.byPub(self.publisherList[0].id)
        self.branchList = self.data.authorBranch(self.bookList[0].id)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Search by Publisher')

        # Combobox
        com1 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com2 = ttk.Combobox(self.tab1, width=20, state="readonly")
        com1.grid(column=1, row=6)
        com2.grid(column=2, row=6)
        com1['values'] = self.publisherList
        hi = self.data.byPub(self.publisherList[0].id)
        com2['values'] = hi
        com1.current(0)
        com2.current(0)
        com1.bind("<<ComboboxSelected>>", self.comCallback)
        com2.bind("<<ComboboxSelected>>", self.callBackAgain)

        # Labels
        lab1 = ttk.Label(self.tab1)
        lab1.grid(column=2, row=1)
        self.price = hi[0].price
        lab1['text'] = "Price: $" + str(self.price)
        lab2 = ttk.Label(self.tab1)
        lab2.grid(column = 1, row = 5)
        lab2['text'] = 'Publisher Selection'
        lab3 = ttk.Label(self.tab1)
        lab3.grid(column=2, row=5)
        lab3['text'] = 'Book Selection'

        # Tree
        tree1 = ttk.Treeview(self.tab1, columns=('Branch Name', 'Copies Available'), show='headings')
        tree1.heading('Branch Name', text='Branch Name')
        tree1.heading('Copies Available', text='Copies Available')
        tree1.grid(column=1, row=1)
        for i in tree1.get_children():  # Remove any old values in tree list
            tree1.delete(i)
        for row in self.branchList:
            print(row.__class__)
            print(row)
            tree1.insert("", "end", values=[row.branch,row.number])


""" constructing the GUI """


# Main window
root = tk.Tk()
root.title("Book Finder")
root.geometry('800x400')

# Tab control
tabControl = ttk.Notebook(root)
HenrySBA(tabControl)
HenrySBC(tabControl)
HenrySBP(tabControl)
tabControl.pack(expand = 1, fill ="both")


root.mainloop()
