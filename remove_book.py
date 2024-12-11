import json
import data_loader

def remove_book():
    all_books = data_loader.load_books()
    isbn = input("Enter ISBN of book to remove: ")
    
    for book in all_books:
        if book['isbn'] == isbn:
            all_books.remove(book)
            file = open("library.json",'w')
            json.dump(all_books, file, indent=4)
            print("\033[32mBook removed successfully!\033[0m")
            return
        
    print("\033[31mBook not found!\033[0m")


