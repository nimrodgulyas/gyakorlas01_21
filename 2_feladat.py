"""
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! 
A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából,
majd írja ki a módosított listát a képernyőre!

"""
import random

veletlen = []

for i in range(10):
    veletlen.append(random.randint(1,3))
print(veletlen)
torolt_szam = int(input("Adj meg egy számot 1-3 között!: "))
for i in veletlen:
    veletlen.remove(torolt_szam)
print(veletlen)