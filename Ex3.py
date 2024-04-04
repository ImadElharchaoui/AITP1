T = int(input("Saisir temp en second"))


h = T//3600
m = (T - (h*3600))//60
s = (T- h*3600 - m*60)

print(f"temps : {h} : {m} : {s}")
