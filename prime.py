l=int(input("enter a lower range num:"))
u=int(input("Enter a upper range"))
print("Prime numbers are between",l,"and",u,"are:")
for num in range(l,u+1):
    if num > 1:
        for i in range(2,num):
            if (num%1)==0:
                break
            else:
                print(num)