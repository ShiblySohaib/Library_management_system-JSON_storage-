import data_loader

def view_books():
    all_books = data_loader.load_books()
    if not all_books:
        print("\033[31mNo books found!\033[0m")
        return
    for book in all_books:
        print(
            f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Publishing year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}  | Added on: {book['addTime']} |", 
            end=''
        )
        if 'lastUpdateTime' in book:
            print(f" Last updated on: {book['lastUpdateTime']}|")
        else:
            print()
