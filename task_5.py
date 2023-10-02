#contact_book = l
def AddContact():
    d = {}
    name = input("Enter name of the person :")
    d['name'] = name
    phno = input("Enter phone number :")
    d['phno'] = phno
    email = input("Enter email id :")
    d['email'] = email
    add = input("Enter address :")
    d['address'] = add
    contact_book.append(d)
    print("\nContact is added\n")
def ViewContacts():
    if len(contact_book) == 0:
        print("\nContact book is empty!!!\n")
    for i in contact_book:
        #print("contact No :",i+1)
        for k,v in i.items():
            print(k,':',v)
        print()
def searchContact(name):
    for i in contact_book:
       # for k in i.keys():
        if i['name'] == name:
            Flag = 1
            print("\nContact found\n")
            for k,v in i.items():
                print(k,':',v)
            return i
    print("\nContact not found !!\n")
def update_contact():
    person = input("Enter the name of the person for updating :")
   # p = searchContact(person)
    for i in contact_book:
        if i['name'] == person:
            p = i
            flag = 1
            break
    if flag != 1:
        print("Contact not found !!")
    print(f"Select options for updating the contact of {p['name']}:")
    n = int(input("1.Name\n2.Phone no\n3.Email id\n4.Address  : "))
    if n == 1:
        name = input(f"Enter the new name of {p['name']} : ")
        p['name'] = name
    elif n == 2:
        phno = input(f"Enter the new phone number of {p['name']} : ")
        p['phno'] = phno
    elif n == 3:
        email = input(f"Enter the new email id of {P['name']} : ")
        p['email'] = email
    elif n == 4:
        add = input(f"Enter the new address of {p['name']} : ")
        p['address'] = add
    else:
        print("Choose correct option\n")
def deleteContact(name):
    d = searchContact(name)
   
    print(f"Contact of {d['name']} is deleted\n")
    contact_book.remove(d)
contact_book = []
while True:
    op = int(input("1.Add contact\n2.View contact list\n3.Search contact\n4.Update contact\n5.Delete contact\n6.exit from contact book  : "))
    if op == 1:
        AddContact()
    elif op == 2:
        ViewContacts()
    elif op == 3:
        n = input("Enter the name of the person you want to search : ")
        searchContact(n)
    elif op == 4:
        update_contact()
    elif op == 5:
        n = input("Enter the  name of the person you want to delete : ")
        deleteContact(n)
    elif op == 6:
        exit()
    else:
        print("Choose correct option")

    



    
