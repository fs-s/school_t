a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a > b and a > c:  
    print("a on suurem, kui b ja c")
if b > a and b > c:
    print("b on suurem, kui a ja c ")
elif b > c:
    print("c on suurem kui a ja b " )