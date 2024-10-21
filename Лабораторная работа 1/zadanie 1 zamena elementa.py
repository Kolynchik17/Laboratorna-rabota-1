numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
kol=len(numbers)
i=0
while (i<=kol):
    if (numbers[i]==None):
        break
    else:
        i+=1
sym=0
for x in range(0,i):
    sym=sym+numbers[x]
for x in range(i+1, kol):
    sym=sym+numbers[x]
numbers[i]=sym/kol
print("Измененный список:", numbers)
