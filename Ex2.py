import math


def Equation(a,b,c):
    delta = (b*b) / (4*a*c)

    if delta < 0:
        print("no solution")
    elif delta == 0:
        sol = (-b) / (2*a)
        print(f"solution : {sol}")
    else :
        sol1 = (-b + math.sqrt(delta)) / (2*a)
        sol2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"solution 1 : {sol1} , solution 2 : {sol2}")


Equation(2,3,1)
