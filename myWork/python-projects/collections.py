a = [10,20,30,40,50]

a.append(5)
a.append(6)
a.append(7)
print(a)

a.remove(50)
print(a)
a.pop(2)
a.pop()
print(a)

a.sort()
print(a)

empty = []

for i in range(1,4):
    empty.append(a[i])

print(empty)


#Dictionary
fav_foods = {"Kathleen" : "pizza", "Yin" : "pizza", "Kericia" : "Italia", 
             "Owen" : "burgers"}

yin_favfood = fav_foods["Yin"]
print(yin_favfood)

for key in fav_foods:
    print(key, "'s favorite food is", fav_foods[key])