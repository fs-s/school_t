string= input("sisestage string. ")
string.strip()
a = len(string)
b = float(len(string) / 2)

if a>= 7 and (a%2) !=0:
    print (string[int(b-1.5):int(b+1.5)])
    print("true")
else:
    print("false")