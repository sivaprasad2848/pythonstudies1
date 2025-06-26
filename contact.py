y=0
contacts=[]
while(y==0):
    print("Menu Program")
    print("1->For Create New Contact")
    print("2->For Display Contact")
    print("3->For Delete Contact")
    print("4->For Update Contact")
    opt=int(input("Enter an option"))
    if(opt==1):
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        contacts.append((name,email,mobile))
    if(opt==2):    
        for item in contacts:
            print(item[0]+" "+item[1]+" "+item[2])
        
    y=int(input("Do you want to continue?press 0 for yes"))