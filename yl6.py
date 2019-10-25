text = str(input("abi ")).lower()

vowelcount = 0

for char in text:
    if char in "aeiouõäöü":
        vowelcount += 1
        
print(vowelcount)