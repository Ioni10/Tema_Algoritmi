# Euclid Extins:
def euclid_extins(a,b):
    if b == 0:
        return a, 1, 0
    d, x1 , y1 = euclid_extins(b, a%b)
    x = y1
    y = x1 - (a//b) * y1
    return d, x ,y

a = 30
b = 20
gcd = 10
d, x,y = euclid_extins(a,b)
solutie = f"30 *1 + 20*(-1) = {d}"
print(solutie)
