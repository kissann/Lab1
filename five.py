#Задача 5 Задано чотири точки паралелограма за допомогою координат його вершин.
# Визначити площу паралелограма та довжину його діагоналей. Результат округлити до тисячних.
print("Введите координаты первой точки:")
x1= input("x1 = ")
y1= input("y1 = ")
print("Введите координаты второй точки:")
x2= input("x2 = ")
y2= input("y2 = ")
x3=float(x1)+float(x2)
y3=float(y1)
x4=float(x3)-float(x1)-float(x2)
y4=float(y2)
print("(x1 = %.2f y1 = %.2f)\n(x2 = %.2f y2 = %.2f)\n(x3 = %.2f y3 = %.2f)\n(x4 = %.2f y4 = %.2f)\n" % (float(x1), float(y1),float(x2),float(y2),float(x3),y3,x4,y4))
a=float(x3)-float(x1)
h=float(y2)-float(y3)
print("Высота h = %.2f \nОснование а = %.2f" % (h,a))
S=a*h
print("Площа параллелограмма S = %.2f" % (S))