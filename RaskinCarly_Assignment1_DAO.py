import mysql.connector


class HenryDAO():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='nopancakemix',
            database='comp3421',
            host='127.0.0.1'
        )
        self.mycur = self.mydb.cursor()

    def listAuthors(self):
        sql = 'SELECT * FROM HENRY_AUTHOR;'
        self.mycur.execute(sql)
        result = self.mycur.fetchall()

        authorList = []
        for row in result:
            author = Author(row[2], row[1], row[0])
            authorList.append(author)

        return authorList

    def byAuthor(self, authID):
        sql =  'SELECT title, book_code, price from henry_book WHERE book_code IN (SELECT book_code FROM henry_wrote WHERE author_num =' + str(authID) + ');'

        self.mycur.execute(sql)
        result = self.mycur.fetchall()

        bookList = []
        for row in result:
            book = Book(row[0], row[1], row[2])
            bookList.append(book)
        print(bookList)

        return bookList

    def authorBranch(self, bookID):
        sql = """SELECT branch_name, on_hand FROM henry_branch JOIN henry_inventory ON henry_branch.branch_num = henry_inventory.branch_num WHERE book_code ='""" + str(bookID) + "';"


        self.mycur.execute(sql)
        result = self.mycur.fetchall()
        branchList = []
        for row in result:
            branch = Branch(row[0], row[1])
            branchList.append(branch)

        return branchList

    def categoryList(self):
        sql = 'SELECT DISTINCT(type) FROM henry_book'
        self.mycur.execute(sql)
        result = self.mycur.fetchall()
        categories = []
        for row in result:
            category = Categories(row[0])
            categories.append(category)

        return categories

    def byCategory(self, catID):
        sql = """SELECT title, book_code, price from henry_book where book_code in (SELECT book_code from henry_book where type = '""" + str(catID) + "');"
        self.mycur.execute(sql)
        result = self.mycur.fetchall()
        bookList = []
        for row in result:
            book = Book(row[0], row[1], row[2])
            bookList.append(book)
        return bookList

    def pubList(self):
        """ I only want to get the publishers that have books available in Henry """
        sql = """SELECT publisher_code, publisher_name from henry_publisher where publisher_code IN (SELECT publisher_code from Henry_book);"""
        self.mycur.execute(sql)
        result = self.mycur.fetchall()
        publisherList = []
        for row in result:
            pub = Publisher(row[0],row[1])
            publisherList.append(pub)
        return publisherList

    def byPub(self, pub_id):
        sql = """SELECT title, book_code, price from henry_book where book_code in (Select book_code from henry_book where publisher_code = '""" + pub_id + "');"
        self.mycur.execute(sql)
        result = self.mycur.fetchall()
        bookList = []
        for row in result:
            book = Book(row[0],row[1],row[2])
            print(book)
            bookList.append(book)
        return bookList

    def close(self):
        self.mydb.commit()
        self.mydb.close()

class Author():
    def __init__(self, f, l, id):
        self.first = f
        self.last = l
        self.id = id

    def __str__(self):
        return self.first + " " + self.last


class Book():
    def __init__(self, t, i, p):
        self.title = t
        self.id = i
        self.price = p

    def __str__(self):
        return self.title

class Branch():
    def __init__(self, b, n):
        self.branch = b
        self.number = n

    def __str__(self):
        return str(self.branch) + " " + str(self.number)

class Categories():
    def __init__(self, c):
        """self.id = id
        self.title = t"""
        self.category = c

    def __str__(self):
        return self.category

class Publisher():
    def __init__(self, i, p):
        self.id = i
        self.publisher = p

    def __str__(self):
        return self.publisher

hi = HenryDAO()

hi.byAuthor(5)

hi.byPub('AH')