y=0
contacts=[]
while(y==0):
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    contacts.append((name,email,mobile))
    #print(contacts)
    for item in contacts:
        print(item[0]+" "+item[1]+" "+item[2])
    
    y=int(input("Do you want to continue?press 0 for yes"))