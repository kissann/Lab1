#Second
import math

print("Введите радиус орбиты первой планеты, радиус орбиты второй планеты и период обращения первой планеты:")
R0= float(input("R0 = "))
T0 = float(input("T0 = "))
R1 = float(input("R1 = "))
print("Формула Кеплера T0^2/R0^3=T1^2/R1^3")
T1=math.sqrt((R1**3/R0**3)*T0**2)
print("T1 = %.2f" % (T1))