list=["Jake","Zac","Ian","Ron","Sam","Dave"]
search_name="Sam"
if search_name in list:
    print(f"{search_name} found in the list")
search_name1=input("Enter the name to be searched:")
for i in list:
    a=i.upper()
    b=search_name1.upper()
    if a==b:
        print("The name",search_name1,"has been found in the list")
        break
    else:
        print("No such name found in the list")
        break