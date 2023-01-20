from numpy.polynomial import polynomial as P

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

def calculate_coefficients():
    points = []
    n = int(input("Enter the number of points of the polynomial: "))
    for i in range(n):
        x, y = map(int, input("Enter x and y for point {}: ".format(i+1)).split())
        points.append((x, y))

    x = [p[0] for p in points]
    y = [p[1] for p in points]
    coefficients = P.polyfit(x, y, len(points) - 1)

    return [round(coef, 1) for coef in coefficients]

coefficients = calculate_coefficients()

def lagrange(f, x):
    value = 0
    for i in range(len(f)):
        value = value + f[i] * x ** i

    return value

x = input("Enter the point x for which you want to calculate the value of the polynomial: ")

print("The value of the polynomial in this point x is: ", lagrange(coefficients, int(x)))
