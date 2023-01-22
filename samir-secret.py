import random
from decimal import Decimal

prime = 2 ** 61 - 1

# Obliczanie wartości wielomianu
def polynomial_value(x0, polynomial): 
    i = 0
    res = 0
    for power in reversed(range(0, len(polynomial))): 
        res += polynomial[i] * (x0 ** power) 
        i += 1   
    return res 

# Generowanie wielomianu
# 1. Jako pierwszy współczynnik zapisuję s - szyfrowaną liczbę.
# 2. Losuję współczynniki wielomianu, odwracam listę, 
#    tak aby potęgi przy współczynnikach malały.
# 3. Dla losowo wybranych punktów obliczam wartość wielomianu 
#    i zapisuje parę punktów.

def generating_polynomial(s, k, n):
    polynomial = [s] 

    for i in range(k-1):
        polynomial.append((random.randint(1, prime)))

    polynomial.reverse()
    shares = []

    for i in range(1, n+1):
        shares.append((i, polynomial_value(i, polynomial) % prime))   
    return shares

# Odszyfrowywanie sekretu v1.
# 1. Biorę wielomian w postaci wartościowej
# 2. Rozdzielam je na wartości x oraz wartości y
# 3. Stosuję wzór: https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing
# 4. Zwracam przybliżoną wartość

def decipher1(k, points, val):
    x_values, y_values = zip(*points)
    result = 0
    for i in range(k):
        l, m = 1, 1
        for j in range(k):
            if i != j:
                l *= val-x_values[j]
                m *= x_values[i] - x_values[j]
        result += Decimal(y_values[i] * Decimal(l/m))
    return round(result % prime)

# Rozszerzony algorytm Euklidesa
def roz(a, b):
    if b == 0:
        return (1, 0)
    p1, p2 = roz(b, a%b)
    return(p2, p1 - (a // b) * p2)

# Odszyfrowywanie sekretu v2.
def decipher2(k, points, val):
    x_values, y_values = zip(*points)
    result = 0
    for i in range(k):
        l = y_values[i] % prime
        m = 1
        for j in range(k):
            if i != j:
                l *= (val - x_values[j]) % prime
                m *= (x_values[i] - x_values[j]) % prime
            od, _ = roz(m, prime)
        result = (result + (l * od)) % prime
    return result

e = generating_polynomial(12345, 3, 6)

print(decipher1(3, e, 0))
print(decipher2(3, e, 0))