# Build a shopping cart system where you can add, remove, and display items.

def shopping_cart():
    items = []

    while True:
        print("------ SHOPPING CART ------")
        print("1. Add Items\n2. Remove Item\n3. Display Item\n4. Exit")
        print("----<<<<<>>>>>----")
        try:
            user_choice_input = int(input("Enter your choice: "))
            if user_choice_input == 1:
                add_item = input("Enter an Item to Cart: ")
                items.append(add_item)
        except ValueError:
            print("Enter a valid choice (1, 2, 3, 4)")


        if user_choice_input == 2:
            try:
                remove_item = int(input("Enter index of the item you want to remove: "))
                print("----<<<<<>>>>>----")
                print("Succesfully Removed!")
                print("----<<<<<>>>>>----")
                items.pop(remove_item)
            except ValueError:
                print("----<<<<<>>>>>----")
                print("Please Enter a Valid Index")
                print("----<<<<<>>>>>----")

        if user_choice_input == 3:
            print("---- All Items----")
            if not items:
                print("----<<<<<>>>>>----")
                print("Currently You don't have any item add if you want")
                print("----<<<<<>>>>>----")
            else:
                print("----<<<<<>>>>>----")
                for i in range(len(items)):
                    print(f"{i}: {items[i]}")
                print("----<<<<<>>>>>----")
        if user_choice_input == 4:
            print("----<<<<<>>>>>----")
            print("Thank You! Have a Nice Day!")
            print("----<<<<<>>>>>----")
            break

        else:
            print("----<<<<<>>>>>----")
            print("Invalid Choce!")
            print("----<<<<<>>>>>----")

shopping_cart()



