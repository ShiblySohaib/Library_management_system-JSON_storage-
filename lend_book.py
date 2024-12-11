import json
import data_loader
from datetime import datetime,timedelta


def lend_book():
    all_books = data_loader.load_books()
    records = data_loader.load_records()
    isbn = input("Enter ISBN of book to lend: ")
    for book in all_books:
        if book['isbn'] == isbn:
            if int(book['quantity'])<1:
                print("\n\n\033[31mNot enough copies!\033[0m")
                return
            
            print("\n\nBook found!\n")

            #get borrower data
            print("Enter borrower details: ")
            print("-----------------------")
            try:
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                if not phone.isnumeric():
                    print("\033[31mInvalid phone number. Try again\033[0m")
                    return
                lendTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                #lend for 7 days
                dueTime = (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y %H:%M:%S")
            except:
                print("\033[31mInvalid input. Try again\033[0m")
                return

            #get record data
            new_record = {
                "name": name,
                "phone": phone,
                "borrowed_book_isbn" : book['isbn'],
                "lendTime": str(lendTime),
                "dueTime": str(dueTime),
            }

            #adjust data
            book['quantity'] = str(int(book['quantity'])-1)
            book_file = open('library.json','w')
            json.dump(all_books, book_file, indent=4)

            records.append(new_record)
            record_file = open('records.json','w')
            json.dump(records, record_file, indent=4)

            print("\033[32mBook lent successfully!\033[0m")
            return
        
    print("\033[31mBook not found!\033[0m")
        

