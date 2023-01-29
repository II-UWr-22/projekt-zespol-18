import random
from decimal import Decimal
from polynomial import Polynomial

class SamirSecret(Polynomial):
    def __init__(self,s,k,n,p=61):
        self.s = s
        self.k = k
        self.n = n
        self.prime = 2 ** p - 1
        self.generated = self.generating_polynomial()

    def generating_polynomial(self):
        polynomial = [self.s]
        for i in range(self.k - 1):
            polynomial.append((random.randint(1, self.prime)))
        polynomial.reverse()
        shares = []
        for i in range(1, self.n + 1):
            shares.append((i, Polynomial.eval(polynomial, i) % self.prime))
        return shares

    def decipher1(self, klucz, val=0):
        points = self.generated[:klucz]
        x_values, y_values = zip(*points)
        result = 0
        for i in range(klucz):
            l, m = 1, 1
            for j in range(klucz):
                if i != j:
                    l *= val - x_values[j]
                    m *= x_values[i] - x_values[j]
            result += (Decimal(y_values[i]) * Decimal(l / m))
        return round(result % self.prime)

    # Rozszerzony algorytm Euklidesa
    def roz(a, b):
        if b == 0:
            return (1, 0)
        p1, p2 = SamirSecret.roz(b, a % b)
        return (p2, p1 - (a // b) * p2)

    # Odszyfrowywanie sekretu v2.
    def decipher2(self, klucz, val=0):
        points = self.generated[:klucz]
        x_values, y_values = zip(*points)
        result = 0
        for i in range(klucz):
            l = y_values[i] % self.prime
            m = 1
            for j in range(klucz):
                if i != j:
                    l *= (val - x_values[j]) % self.prime
                    m *= (x_values[i] - x_values[j]) % self.prime
                od, _ = SamirSecret.roz(m, self.prime)
            result = (result + (l * od)) % self.prime
        return result
