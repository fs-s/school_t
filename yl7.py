first_name = input("Mis on sinu nimi? ")
print("tere "+ first_name + "!")
location = input ("Kus te elate? ")
if location.lower("saaremaal"):
    print("lahe")

age = int(input("Vanus: "))
if age <= 17:
    print("te olete liiga noor,et autot juhtida ")
elif age == 18:
    print("te olete täisealine ja võite teha autojuhilube ")
else:
    print("võite autot juhtida" )