dict={}
def add_expense():
    item = input("enter the item")
    price = int(input("enter the price"))
    dict[item] = price
    print("expenses add")
def view_expense():
    for price,item in dict.items():
        print(price,item)
def total_expense():
    sum = 0
    for price in dict.values():
        sum += price
    print("total expense", sum)
while True:
    print("1.add expense")
    print("2. view expense")
    print("3.total expense")
    print("4.exit")

    choice = input("enter the choice")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("exit")
        break
    else:
        print("invalid choice") 