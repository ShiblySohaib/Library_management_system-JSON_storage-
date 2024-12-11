import json
import data_loader
from datetime import datetime

def return_book():
    all_books = data_loader.load_books()
    records = data_loader.load_records()
    isbn = input("Enter ISBN of book to return: ")
    phone = input("Enter borrowers phone number: ")

    for record in records:
        if record['borrowed_book_isbn'] == isbn and record['phone'] == phone:
            #adjust book quantity
            for book in all_books:
                if book['isbn'] == isbn:
                    book['quantity'] = str(int(book['quantity'])+1)
                    book_file = open('library.json','w')
                    json.dump(all_books, book_file, indent=4)

            #remove lend record
            records.remove(record)
            record_file = open('records.json','w')
            json.dump(records, record_file, indent=4)

            print("\033[32mBook returned successfully!\033[0m")
            dueTime = datetime.strptime(record['dueTime'], "%d-%m-%Y %H:%M:%S")

            #fined if not returned within a week
            if datetime.now()>dueTime:
                print("\033[31mBook returned late. Need to pay fine!\033[0m")
            return

    print("\033[31mNo such record found!\033[0m")
