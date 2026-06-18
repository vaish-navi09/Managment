books =[]
def add_books():
    book = input("enter the name of book")
    books.append(book)
    print("book added")

def issue_book():
    name = input("enter the issue book")
    if name in books:
        books.remove(name)
        print("book issue")
    else:
        print("book not found")

def return_book()  :
    rbook = input("enter the book to return")
    books.append(rbook)   
    print("book back")

def view_book():
    for book in books:
        print(book)

while True:
    print("1. add book")
    print("2. issue_book")
    print("3. return_book")
    print("4.view book")
    print("5.exit")

    choice= input("enter the choice")
    if choice == "1":
        add_books()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        view_book()
    elif choice == "5":
        print("exit")
        break
    else:
        print("invalid choice")
     