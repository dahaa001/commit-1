timelønn = int(input("Hva er din timelønn?" "\n"))
timer_jobbet = int(input("Hvor mange timer har du jobbet i dag?" "\n"))

print("Du har tjent ",timelønn * timer_jobbet ,"kr på en dages arbeid" "\n" "\n")
print("Bruttolønn for et helt år blir ",timelønn * timer_jobbet * 20 * 12,"Kr", "\n")
print("Etter skatt for ",timelønn * timer_jobbet * 20 * 12/100 * 75, "kr" "\n")
