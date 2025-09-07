# Avem nevoie de este prim (pentru ca verifica daca este prim numarul nostru)
def este_prim(p):
    if p < 2: return False
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def gaseste_radacina(p):
    if not este_prim(p):
        return -1
    phi = p - 1
    factori = set()
    n = phi
    i = 2
    while i*i <= n:
        if n % i == 0:
            factori.add(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factori.add(n)
    for r in range(2, p):
        ok = True
        for f in factori:
            if pow(r, phi // f, p) == 1:
                ok = False
                break
        if ok:
            return r
    return -1



p = 7
print('Radacina primitica a lui ',p , "este:",gaseste_radacina(p))

