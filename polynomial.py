from numpy.polynomial import polynomial as P

class Polynomial:

    def __init__(self, pol):

        if type(pol) is str:
            self.coefs = self.coefficient_form(pol)

        elif type(pol) is list:
            self.coefs = pol

        elif type(pol) is set:
            self.points = pol

    def coefficient_form(self,f):

        def coefficient(x):
            if "x" not in x:
                return int(x)
            elif "^" not in x:
                if x[0] != "x":
                    return int(x[:-1])
                else:
                    return 1
            else:
                if x[0] != "x":
                    return int(x[:(x.index("x"))])
                else:
                    return 1

        def power(x):
            if "x" not in x:
                return 0
            elif "^" not in x:
                return 1
            else:
                return int(x[x.index("^") + 1:])

        f = f.split()
        f = [x for x in f if x[:2] != "0x"]
        f0 = []
        if "x" in f[0]:
            f0.append(f[0])
        for i in range(len(f)):
            if f[i] == "+":
                f0.append(f[i + 1])
            elif f[i] == "-":
                if f[i] + f[i + 1][0] == "-x":
                    f0.append("-1" + f[i + 1])
                else:
                    f0.append("-" + f[i + 1])
        if f0:
            f = f0
        powers = [power(x) for x in f]
        coefficients = [coefficient(x) for x in f]
        degree = powers[0]
        wyn = [0] * (degree + 1)
        x = zip(powers, coefficients)

        for i, j in x:
            wyn[i] = j
        return (wyn[::-1])

    def eval(f, x):

        wartosc = 0
        potega = 0
        g = f[::-1]
        for i in g:
            wartosc += i * x ** potega
            potega += 1
        return wartosc

    def transform(f, A):

        return {(x, Polynomial.eval(f, x)) for x in A}

    def calculate_coefficients(points):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        coefficients = P.polyfit(x, y, len(points) - 1)

        return [round(coef, 1) for coef in coefficients]

    def lagrange(f, x):
        f = Polynomial.calculate_coefficients(f)
        value = 0
        for i in range(len(f)):
            value = value + f[i] * x ** i

        return value
