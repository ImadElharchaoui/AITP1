while 1 :
    n = int(input("saiser le nombre sauf 0: "))
    if n != 0 :
        break

sum = 0
for i in range(1,n+1):
    sum += i*i

print(sum)