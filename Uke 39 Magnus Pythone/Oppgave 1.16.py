# Ta inn hvor mange biler brukeren har solgt, 
# og gi en bonus på 5000kr dersom det er solgt flere enn 70 biler.
#  Regn så ut hvor mye brukeren får i lønn,
#  hver bil gir 500kr i lønn. Skriv til konsoll.
kr_bil = 500


solgte_biler = int(input("Antall biler solgt: "))

if (solgte_biler > 70):
    lonn = solgte_biler*kr_bil + 5000
elif (solgte_biler > 60):
    print(f'Bra jobba,det var nesten bonus du mangler bare {70-solgte_biler} biler')
    lonn = solgte_biler*kr_bil
else:
    lonn = solgte_biler*kr_bil
print(f"Du fikk  {lonn} kr i lønn for du solgte hele {solgte_biler} biler")

# Det koden gjør her ta imot selgers antall solgte biler.
# Regner ut hvor mye penger selger for alle biler solgt.
# Men også hvor mange biler han manglet vis han fikk over 60 salg av biler.