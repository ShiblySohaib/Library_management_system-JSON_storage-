import json
import data_loader
from datetime import datetime


def add_book():
    all_books = data_loader.load_books()
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        if int(isbn)<0:
            print("\033[31mInvalid ISBN. Try again\033[0m")
            return
        year = input("Enter publishing year: ")
        if int(year)<0:
            print("\033[31mInvalid year. Try again\033[0m")
            return
        price = input("Enter price: ")
        if float(price)<0:
            print("\033[31mInvalid price. Try again\033[0m")
            return
        quantity = input("Enter quantity: ")
        if int(quantity)<0:
            print("\033[31mInvalid quantity. Try again\033[0m")
            return
        addTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    except:
        print("\033[31mInvalid input. Try again\033[0m")
        return
    new_book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "price" : price,
        "quantity" : quantity,
        "addTime": addTime
    }

    for book in all_books:
        if book['isbn'] == new_book["isbn"]:
            print("\033[96mBook already exists\033[0m")
            return
    
    all_books.append(new_book)
    file = open("library.json",'w')
    json.dump(all_books, file, indent=4)
    print("\033[32mBook added successfully!\033[0m")
