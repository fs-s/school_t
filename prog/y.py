list1 = [6,5,3,1,1,2]

list1 = list(dict.fromkeys(list1))
list1.sort()
print("Väljund: ", list1[-2])