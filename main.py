from admin import admin
from user import user

if (__name__=="__main__"):
        print('''
        ************************************************************************
        *                        FIRSTBIT CAKE SHOP                            *
        ************************************************************************
        ''')
        print('''
        1. Admin part
        2. User part
        ''')
        choice = int(input("Enter your choice:"))
        pin = 1234
        if (choice == 1):
            try:
                pin = int(input("Enter admin pin:"))
                if (pin == 1234):
                    admin()
                else:
                    print("Invalid user name and password")
            except:
                pass

        elif(choice == 2):
            user()

        else:
            print("Inavlid choice")