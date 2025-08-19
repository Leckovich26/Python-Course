
frutas= ["banano", "pera", "uva"]
print(frutas)

color= ["green","silver","brown"] 
print(color[0])
print(color[-1])

numbers= [1,2,3,4,5,6]
numbers[3]= 7
print(numbers)
numbers.append(8)
print(numbers)
numbers.remove(7)
print(numbers)

names=["Car", "House", "Paper", "Dragon"]
for name in names:
    print("Hi", name)


numeros=[1,2,3,4,2,3,5,1,6,2,4,3,5,2]
print(numeros.count(2))

ages=[34,56,12,43,23,93,22,52,18,64,32]
ages.sort()
print(ages)

ventas= [1500, 2500, 7500, 200]
venta= sum(ventas)
print("La venta total fue de ", venta)

ventas= [1500, 2500, 7500, 200]
venta= sum(ventas)
print(f"La venta total fue de {venta}")

