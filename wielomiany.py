from numpy.polynomial import polynomial as P

# 1

# coefficient_form(f) function takes for argument a polynomial in form:
# "a(n)x^n +/- a(n-1)x^(n-1) +/- ... +/- a(1)x + a(0)" or
# "- a(n)x^n +/- a(n-1)x^(n-1) +/- ... +/- a(1)x + a(0)", where a(m) is positive integer
# and returns list of coefficients in form [a(n),a(n-1),...,a(1),a(0)]
#for example coefficient_form("5x^5 - 2x^3 + x - 1") returns [5, 0, -2, 0, 1, -1]
def coefficient_form(f):
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
            f0.append(f[i+1])
        elif f[i] == "-":
            if f[i] + f[i+1][0] == "-x":
                f0.append("-1" + f[i+1])
            else:
                f0.append("-" + f[i+1])
    if f0:
        f = f0
    powers = [power(x) for x in f]
    coefficients = [coefficient(x) for x in f]
    degree = powers[0]
    wyn = [0]*(degree+1)
    x = zip(powers,coefficients)

    for i, j in x:
        wyn[i] = j
    return(wyn[::-1])

x1 = coefficient_form(input("Podaj wielomian f(x): "))
print("Reprezentacja wielomianu w postaci listy wspolczynnikowej to:",x1)

#3

def eval(f,x):
	wartosc=0
	potega=0
	g=f[::-1]
	for i in g:
		wartosc+=i*x**potega
		potega+=1
	return wartosc


# 4 

#funkcja calculate_coefficients() oblicza współczynniki wielomianu na podstawie zbióru par wartości wielomianu w punktach
def calculate_coefficients():
    points = []
    n = int(input("Podaj liczbę punktów wielomianu: "))
    for i in range(n):
        x, y = map(int, input("Wprowadź x i y dla punktu {}: ".format(i+1)).split())
        points.append((x, y))

    x = [p[0] for p in points]
    y = [p[1] for p in points]
    coefficients = P.polyfit(x, y, len(points) - 1)

    return [round(coef, 1) for coef in coefficients]

coefficients = calculate_coefficients()

#funkcja lagrange(f, x) na podstawie obliczonych współczynników wyznacza wartość wielomianu dla podanego argumentu 
def lagrange(f, x):
    value = 0
    for i in range(len(f)):
        value = value + f[i] * x ** i

    return value

x = input("Wpisz punkt x, dla którego chcesz obliczyć wartość wielomianu: ")

print("Wartość wielomianu w tym punkcie x wynosi: ", lagrange(coefficients, int(x)))
