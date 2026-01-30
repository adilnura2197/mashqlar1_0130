#1-misol
roy = [10, 20, 30, 40, 50]
print(len(n))

print(f"Uchinchi element: {n[3]}")

if 30 in roy:
    print(f"Ro'yxatda bor!")
else:
    print("Ro'yxatda yo'q!")

yangi_roy = roy[-2:]
print(yangi_roy)

summa = sum(roy)
print(summa)


#2-misol
fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)

fruits.pop(1)
print(fruits)

index = fruits.index('cherry')
fruits.insert(index, 'peach')
print(fruits)

fruits.sort()
print(fruits)

print(fruits)
