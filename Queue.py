# ADA PGM For Queue - FIFO

arr = []


try:
    while True:
        a = {1:"Insert",2:"Delete",3:"Display",4:"Exit"}
        for i in a:
            print(i," : ", a[i])
        
        choice = int(input("Please Enter your Choice  :- "))
        if choice == 1:
            ichoice = int(input("Enter Number to add :- "))
            arr.append(ichoice)

        if choice == 2:
            print(arr[0]," is poped")
            arr.pop(0)
        
        if choice == 3:
            print("\n-----",arr,"----- \n")
        
        if choice == 4:
            break
    
        if choice not in a.keys():
            print("\n Please enter correct Choice!")
        
        
    
except:
    print("Something Wrong!")