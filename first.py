#First
import math

print("Введите площадь и число на которое основание больше чем высота треугольника:")
S= float(input("S = "))
x = float(input("x = "))
discr = x ** 2 + 8 * S
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    h1 = (-x + math.sqrt(discr)) / (2)
    h2 = (-x - math.sqrt(discr)) / (2)
    if all([h1>0,h2>0]):
        print("h1 = %.2f \nh2 = %.2f" % (h1, h2))
    else :
        if h1>0:
            print("h1 = %.2f" % (h1))
        if h2>0:
            print("h2 = %.2f" % (h2))

elif discr == 0:
    x = -x / (2)
    print("x = %.2f" % x)
else:
    print("Корней нет")