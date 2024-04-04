n1 = int(input("saiser 1er number : "))
n2 = int(input("saiser 2em number : "))

op = input("saiser operation (+,-,*,/)").lower().split()[0]

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    if n2== 0:
        print("il ne peut pas diviser sur 0")
    else:
        print(n1 / n2)