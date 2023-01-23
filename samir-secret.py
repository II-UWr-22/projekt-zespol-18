import random
from decimal import Decimal


# Obliczanie wartości wielomianu
def eval(x, f):
	wartosc = 0
	potega = 0
	g = f[::-1]
	for i in g:
		wartosc += i * x ** potega
		potega += 1
	return wartosc

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
        shares.append((i, eval(i, polynomial) % prime))   
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
        result += (Decimal(y_values[i]) * Decimal(l/m))
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

sekret = int(input("Podaj sekret: "))
k = input("Podaj klucz oraz liczbę udziałów: ")
k = k.split()
p = int(input("Podaj poziom bezpieczeńśtwa (61, 89, 127): "))
prime = 2 ** p - 1

# Generowanie wielomianu
e = generating_polynomial(sekret, int(k[0]), int(k[1]))
print("Wygenerowane punkty:")

for i in e:
    print(i)
    
klucz = int(input("Podaj klucz: "))

x = e[:klucz]

#sposób 1 nie zawsze daje wynik za pierwszym razem
print(f"Odzyskany sekret sp.1: {decipher1(klucz, x, 0)}")
print(f"Odzyskany sekret sp.2: {decipher2(klucz, x, 0)}")