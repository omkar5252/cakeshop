from cake import Cake
class Cakemgmt:
    def addcake(self,c):
        with(open("cake.txt","a")) as file:
            file.write(str(c)+"\n")

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

    def edit_by_id(self,id):
        allcake = []
        found = False
        try:
            with(open("cake.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(str(id),0,4)
                    except:
                        pass
                    else:
                        found = True
                        line = line.split(",")
                        print(line)
                        ans = input("Do you want to change cake name (y/n):")
                        if (ans.lower() == "y"):
                            line[1]= input("Enter new name of cake:")

                        ans = input("Do you want to change cake price (y/n):")
                        if (ans.lower() == "y"):
                            line[2] = input("Enter new cake price:")

                        ans = input("Do you want to change cake quantity (y/n):")
                        if (ans.lower() == "y"):
                            line[3] = input("Enter new cake Quantity:")
                            line[3] += "\n"
                        line = ",".join(line)
                    finally:
                        allcake.append(line)               
            if (found):
                with (open("cake.txt","w")) as file:
                    for s in allcake:
                        file.write(s)
                    print("Cake edit sucessfully")
            else:
                print("Record not found")
        except:
            print("File does not exist......")
            return

    def delete_by_id(self,id):
        allcake = []
        found = False
        try:
            with(open("cake.txt","r")) as file:
                for line in file:
                    try:
                        line.lower().index(str(id),0,4)
                    except:
                        allcake.append(line)
                    else:
                        found = True

                if (found):
                    with(open("cake.txt","w")) as file:
                        for cake in allcake:
                            file.write(cake)
                        print("Cake delete sucessfully.")
                else:
                    print("Record not found")
        except:
            print("File does not exist...")

    def showallcake(self):
        try:
            with(open("cake.txt","r")) as file:
                print(file.read())
        except:
            print("File does not exist...")
            return