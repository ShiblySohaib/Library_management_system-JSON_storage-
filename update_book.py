import json
import data_loader
from datetime import datetime

def update_book():
    all_books = data_loader.load_books()
    isbn = input("Enter ISBN of the book to update: ")
    
    for book in all_books:
        if book['isbn'] == isbn:
            print("\n\nBook found!\n")
            print("[Note: Leave field blank if you don't want it to change]\n")
            print("Enter new data for the book:")
            print("----------------------------")
            try:
                title = input("Enter book title: ")
                if not title:
                    title = book['title']
                author = input("Enter author name: ")
                if not author:
                    author = book['author']
                isbn = input("Enter ISBN: ")
                if not isbn:
                    isbn = book['isbn']
                if int(isbn)<0:
                    print("\033[31mInvalid ISBN. Try again\033[0m")
                    return
                year = input("Enter publishing year: ")
                if not year:
                    year = book['year']
                if int(year)<0:
                    print("\033[31mInvalid year. Try again\033[0m")
                    return
                price = input("Enter price: ")
                if not price:
                    price = book['price']
                if float(price)<0:
                    print("\033[31mInvalid price. Try again\033[0m")
                    return
                quantity = input("Enter quantity: ")
                if not quantity:
                    quantity = book['quantity']
                if int(quantity)<0:
                    print("\033[31mInvalid quantity. Try again\033[0m")
                    return
                lastUpdateTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            except:
                print("\033[31mInvalid input. Try again\033[0m")
                return
            book['title'] = title
            book['author'] = author
            book['isbn'] = isbn
            book['year'] = year
            book['price'] = price
            book['quantity'] = quantity
            book['lastUpdateTime'] = lastUpdateTime

            file = open("library.json", 'w')
            json.dump(all_books, file, indent=4)
            
            print("\033[32mBook updated successfully!\033[0m")
            return
    
    print("\033[31mBook not found!\033[0m")



            


        