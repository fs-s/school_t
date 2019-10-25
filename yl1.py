#vaja kirjutada list ja lisada 3 puuvilja, väljastada esimene väärtus
thislist = ["õun","pirn","kirss"]
print(thislist[0])
#lisada uus puuvili
thislist.append("ploom")
print (thislist[3])
thislist = ["õun","pirn","kirss","banaan"]
thislist[1] = "kiivi"
print(thislist)
thislist = ["õun","pirn","kirss","ploom"]
if "õun" in thislist:
    print("jah, 'õun' on puuvilja listis olemas")
thislist = ["õun","pirn","kirss","kiivi","banaan"]
print(len(thislist))
thislist = ["õun","pirn","kirss","kiivi","banaan"]
thislist.remove("banaan")
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.sort()
print(thislist)