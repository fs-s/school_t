sampleText = ("I love You Name")
letters = dict()
letters = dict()

for x in sampleText.lower().replace(" ", ""):
    if x not in letters:
        letters[x] = 1
    else:
        letters[x] = letters[x] + 1

lettersSorted = {k: letters[k] for k in sorted(letters)}

print (lettersSorted)  