# ADA PGM1 For simple Linear Search

l1 = [25,42,15,54,2,75,85,15]
search = int(input("Enter No to search :- "))
j = 0
c = 0
for i in l1:
    j = j+1
    if i == search:
        c += 1
        print(i, " is located at position of ",j)
    
    if c==0:
        print("Sorry the no you entered is not exist!")