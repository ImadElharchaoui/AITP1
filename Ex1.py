notes = []

for n in range(1,4) :
    while 1:
        note = int(input(f"saiser le {n} note:"))

        if note<=20 and note >=200:
            notes.append(note)
            break

moyen = sum(notes)/3

print(moyen)
if moyen >= 16 :
    print("Tres bien")
elif moyen >= 14 :
    print("bien")
elif moyen >= 12 :
    print('Assez bien')
elif moyen >=10 :
    print("Passable")
else:
    print("insuffisant")