#Записати задане трицифрове число в зворотньому порядку.
print("Введите число:")
x= input("x = ")
i = -1
x_ob = ""
while i >= -1 * len(x):
    x_ob = x_ob + x[i]
    i = i - 1
print(x_ob)