from cake import Cake
from cakemgmt import Cakemgmt

def admin():
    choice = 0
    cakemgmt = Cakemgmt()
    while(choice != 6):
        print('''
        1. Add cake
        2. Search cake
        3. Edit cake
        4. Delete cake
        5. Show all cakes
        6. Exit
        ''')
        choice = int(input("Enter your choice:"))
        # shop owner will add cake in admin part
        if (choice == 1):
            id = int(input("Enter cake id:"))
            name = input("Enter cake name:")
            price = int(input("Enter cake price:"))
            quantity = int(input("Enter cake quantity:"))
            c1 = Cake(id,name,price,quantity)
            cakemgmt.addcake(c1)

        # admin will search cake by using id/name
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

        # admin will edit cake by using id
        elif (choice == 3):
            id = int(input("Enter cake id tobe edited: "))
            cakemgmt.edit_by_id(id)

        # admin will delete cake by using id
        elif (choice == 4):
            id = int(input("Enter cake id tobe deleted: "))
            cakemgmt.delete_by_id(id)

        # admin will show all cake 
        elif (choice == 5):
            cakemgmt.showallcake()

        elif (choice == 6):
            print("Log out")
