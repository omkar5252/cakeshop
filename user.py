from cakemgmt import Cakemgmt
from usermgmt import Usermgmt

def user():
    choice = 0
    cakemgmt = Cakemgmt()
    usermgmt = Usermgmt()
    print("NOTE : ONLY HALF KG CAKES ARE AVAILABLE")
    while(choice != 7):
        print('''
        1. Show all cakes
        2. Search cake
        3. Add to cart
        4. Remove from cart
        5. View cart
        6. Buy cake
        7. Exit
        ''')
        choice = int(input("Enter your choice: "))
        # show all cake in shop
        if (choice == 1):
            usermgmt.showallcake()

        # search cake in shop
        elif (choice == 2):
            print("Search cake based on id (1)")
            print("Search cake based on name (2)")
            choice = int(input("Enter your choice (1/2): "))
            if (choice == 1):
                id = int(input("Enter cake id tobe search: "))
                cakemgmt.search_by_id(id)
            elif(choice == 2):
                name = input("Enter cake name tobe search: ")
                cakemgmt.search_by_name(name)
            else:
                print("Invalid choice")

        # add cake to user cart
        elif (choice == 3):
            id = int(input("Enter cake id add to cart: "))
            usermgmt.addtocart_by_id(id)

        # remove cake from user cart
        elif (choice == 4):
            id = int(input("Enter cake id remove from cart: "))
            usermgmt.remove_by_id(id)

        # view cakes in user cart
        elif (choice == 5):
            usermgmt.viewcart()

        # buy cake
        elif (choice == 6):
            usermgmt.buycake()

        elif (choice == 7):
            print('''
            *************************************
            * Thank you so much for choosing us *
            *************************************
            ''')
            
        else:
            print("Please enter valid choice")


       
