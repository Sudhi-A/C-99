num =int(input("Enter the number of rows:"))
print(num)

for i in range(0, num):   
        for j in range(0, i + 1):              
            print("*", end=" ")
        print() 

for i in range(0, num):   
        for j in range(0, i + 1):              
            print(j, end=" ")
        print()  

for i in range(1,num):
    for j in range(1,i+1):
        print(j, end=" ")
    print()   

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()   

for i in range(0, num):   
        for j in range(num, i, -1):              
            print("*", end=" ")
        print()  

for i in range(num, 0, -1):   
        for j in range(1, i+1):              
            print(j, end=" ")
        print()   





 