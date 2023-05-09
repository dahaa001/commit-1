# Oppgave 1.10 
# Ta inn to tall der du sjekker om det andre er større enn det første i en variabel.
#  Skriv ut resultatet av sjekken. 
tall = 0 

print("while-løkker")
while tall < 10:
    print (tall)
    tall += 1

print("For-løkke")
for i in range (10):
    print(i)


print("Hvilket av tallene er størst...")
tall1 = int(input("Tall 1: "))
tall2 = int(input("Tall 2: "))

print("while-løkker")
if tall1 < tall2:
    print (tall1, "is less then",tall2)
elif tall1 > tall2:
    print (tall1, "is more then",tall2)
else:
    tall1 = tall2
    print ("The number you have typed has the same value")