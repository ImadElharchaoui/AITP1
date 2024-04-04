age = int(input("saiser votre age:"))
sexe = input("saiser votre sexe (h,f) :").lower().split()[0]

if (sexe == "h" and age > 20 ) or (sexe == "f" and age >= 18 and age <= 35):
    print("paient l'empot")
else :
    print("n paient pas l'empot")