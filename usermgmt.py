import os
import datetime
import random
class Usermgmt:
    def showallcake(self):
        try:
            with(open("cake.txt","r")) as file:
                print(file.read())
        except:
            print("File does not exist...")
            return

    def search_by_id(self,id):
        try:
            with(open("cake.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(str(id),0,4)
                        print("Found:",line)
                        break
                    except:
                        pass
                else:
                    print("Record not found")
        except:
            print("File does not exist....")

    def search_by_name(self,name):
        try:
            with(open("cake.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(name.lower())
                        print("Found:",line)
                        break
                    except:
                        pass
                else:
                    print("Record not found")
        except:
            print("File does not exist....")
   
    def addtocart_by_id(self,id):
        allcake = []
        found = False
        try:
            with(open("cake.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(str(id),0,4)
                        print("Found : ",line)
                        with(open("cart.txt","a")) as file:
                            pass
                    except:
                        pass
                    else:
                        found = True
                        line = line.split(",")
                        line[3] = input("Enter new cake quantity:")
                        line[3] +="\n"
                        line = ",".join(line)
                        allcake.append(line)    
            if (found):
                with (open("cart.txt","a")) as file:
                    for x in allcake:
                        file.write(x)
                    print("Cake added to the cart successfully")
            else:
                print("Record not found")      
        except:
            print("File does not exist......")
    
    def remove_by_id(self,id):
        allcake = []
        found = False
        try:
            with(open("cart.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(str(id),0,4)
                    except:
                        allcake.append(line)
                    else:
                        found = True
                if (found):
                    with(open("cart.txt","w")) as file:
                        for x in allcake:
                            file.write(x)
                        print("Cake remove from cart successfully")
                else:
                    print("Cake is not available in cart")
        except:
            print("File does not exist...")           
   
    def viewcart(self):
        try:
            with(open("cart.txt","r")) as file:
                print(file.read())
        except:
            print("There is nothing in your cart")
            return

    def buycake(self):
        allcake=[]
        cakes = []
        sum = 0
        try:
            with(open("cart.txt","r")) as file:
                for line in file:
                    line = line.strip()
                    line = line.split(",") 
                    cakes.append(line)
                    bill = float(line[2]) * int(line[3])
                    allcake.append(bill) 
                for x in allcake:
                    sum = sum + x
            # after enter buy button cart.txt file got deleted and bill is generated
            try:
                os.remove("cart.txt")
            except:
                print("File not found")
            else:
                print("Bill generate sucessfully")
                print("\n************** INVOICE **************")
                print("Bill No:",random.randint(11111,99999))
                current_time = datetime.datetime.now()
                print("Date:",current_time)
                print("-------------------------------------")
                print("Description of Cakes")
                for c in cakes:
                    print("Cakes:",c[1],end=" ")
                    print("- Rs.",c[2],end=" ")
                    print("- Q",c[3])
                print("-------------------------------------")
                print("Bill of cakes")
                print("Cakes Ammount      :Rs.",sum)
                gst = sum * (18/100)
                print("GST 18% of total   :Rs.",gst)
                sgst = sum *(9/100)
                print("9% SGST on GST 18% :Rs.",sgst)
                cgst = sum *(9/100)
                print("9% CGST on GST 18% :Rs.",cgst)
                total = sum + gst
                print("Total Bill Ammount :Rs.",total)
                print("*************************************")
                
                finalCakes = []
                with open("cake.txt","r") as file:
                    for line in file:
                        line = line.split(",")
                        for cake in cakes:
                            if(cake[0] == line[0]):
                                line[3] = str(int(line[3])-int(cake[3]))
                                line[3] += "\n"
                        line = ",".join(line)
                        finalCakes.append(line)
                   
                    with open("cake.txt","w") as file:
                        for j in finalCakes:
                            file.write(j)
        except:
            print("Bill does not generate first add something to cart")  