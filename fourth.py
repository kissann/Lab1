#Знайти остачу від ділення першої цифри на останню у чотирицифровому числі.
print("Введите число:")
x= input("x = ")
i = 0
kol=len(x)
ost=int(x[kol-1])%int(x[0])
print(x[0])
print(x[kol-1])
print(ost)