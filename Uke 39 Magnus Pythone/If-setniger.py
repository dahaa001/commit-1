from decimal import Overflow


navn = input("Navn")

tall1 = int(input("Tall 1: "))
tall2 = int(input("Tall 2: "))
tall3 = float(input("Tall 3: "))
resultat = (tall1+tall2)/tall3
print(f" ({tall1} + {tall2} / {tall3} = {resultat}")

