n = int(input("Enter number: "))

a = 0
while a < n:
        list1 = ([a*a])
        a += 1
        if a > n:
            break
        
        print(list1, end=',')