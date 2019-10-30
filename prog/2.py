import random

yMin=0
yMax=101
goal=random.randint(yMin,yMax)
algarv=102

while algarv != goal:
    algarv= int(input("arv: "))
    if algarv > goal:
        print ("liiga suur")
    elif algarv < goal:
            print("liiga väike")
print("õige vastus")