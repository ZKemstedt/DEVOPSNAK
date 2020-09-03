X = 1
Y = 4
adresses = {"Adam": "Ormvägen",
			"Bella": "Klockgatan 1",
			"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}


# Svar på frågor.
#
# Q1: 	Vilken datatyp har variablerna `X` och `Y`?
# A1: 	int, int
print(f'A1: X: {type(X)}, Y: {type(Y)}')
#
# Q2: 	Vilken datatyp har variablen `adresses`?
# A2: 	dict
print(f'A2: {type(adresses)}')
#
# Q3: 	Hur kan man få ut bellas adress ur variabeln `adresses`?
# A3: 	`adresses['Bella']`
print(f"A3: `adresses['Bella']` \n\t-> `{adresses['Bella']}`")
#
# Q4: 	Vad händer om man skriver `adresses["Daniel"] = "Prinsgränd 2"` ?
# A4: 	Nyckel-Värde paret `'Daniel': 'Prinsgränd 2'` läggs till i `adresses`
adresses["Daniel"] = "Prinsgränd 2"
print(f'A4: `adresses["Daniel"] = "Prinsgränd 2"` \n\t-> adresses: {adresses}')
#
# Q5: 	Få ditt programm att skriva ut hur många keys `adresses` har.
print(f'A5: The variable `addresses` has {len(adresses)} keys.')
#
#	Q5.1: 	Utöka programmet så att adressen skrivs ut till den personen som
# 			kommer sist i bokstavsordning.
print('A5.1: The person who\'s name is the first alphabetically in the list of '
	f'adresses lives at {adresses[sorted(adresses.keys())[0]]}')
#
#	Q5.2: 	Utöka programmet så att namnet skrivs ut på den personen som bor på
#			adressen som kommer först i bokstavsordning. Tips: följande rad
# 			byter plats på keys och values i `my_dict`:
#			`my_dict = {v:k for k, v in my_dict.items()}`
#			Förklaring kommer nästa lektion!
residents = {v:k for k, v in adresses.items()}
print(f'A5.2: {residents[sorted(residents.keys())[-1]]} lives at the adress that '
	'appears last alphabetically in the list of adresses')
#
# Q6: 	Vilken datatyp har variabeln `cars`? 
# A6: 	list		`
print(f'A6: {type(cars)}')
# 
# Q7: 	Vad returneras om man skriver `cars[X]`?
# A7: 	"Opel"
print(f'A7: {cars[X]}')
#
# Q8: 	Vad returneras om man skriver `cars[Y]`?
# A8: 	Ingenting, vi får en exception istället eftersom att `Y` är 4 och cars har
#		har längden 3 (alltså index pekar utanför listan)
try:
	cars[Y]
except IndexError as e:
	print(f'A8: {type(e)}: \'{e}\'') # technically not a return value
# Q9: 	Vad returneras om man först skriver `cars.sort()` och på nästa rad skriver
# 		`cars[0]`?
# A9:	`'BMW'`
print(f'A9: {cars[0]}')
#
# Q10:	Skapa en variabel genom att skiva `cars_2` = cars, och på följande rad ska
#		strängen `"Saab"` läggas till i cars med hjälp av append(). Notera att det
# 		alltså bara är ena variabeln som ska utökas. Vad innehåller variablerna
#		`cars_2` och `cars` nu? Förklara!
cars_2 = cars
cars.append('Saab')
print(f'A10: cars: {cars}, cars_2: {cars_2}')
#
#	Q10.1:	Skapa ytterligare en variabel `cars_3` som får sina element av `cars` 
#			men som inte påverkas av vad som läggs till i `cars`.
cars_3 = cars.copy()
print(f'A10.1 {cars_3}')
#
#	Q10.2:	Utöka variabeln `cars` så att den innehåller dubbletter av varje 
#			bilmärke sorterat i omvänd bokstvasordning.
cars += cars
cars.sort()
print(f'A10.2: {cars}')
#
#	Q10.3: 	Från den utökade version av `cars` ifrån förra uppgiften, skapa
#			variabeln `unique_cars` som ska vara en lista där varje bilmärke
#			finne med exakt en gång.
unique_cars = []
for car in cars:
	if car not in unique_cars:
		unique_cars.append(car)
print(f'A10.3: {unique_cars}')
#
# Q11: 	Vilken datatyp har variablerna `numbers1` och `numbers2`?
# A11:	set
print(f'A11: {type(numbers1)}, {type(numbers2)}')
#
# Q12: 	Vilka Värden finns lagrade i variablerna `numbers1` och `numbers2`
# A12:	{1, 2, 3, 1, 6} och {4, 2, 3, 4, 7}
print(f'A12: numbers1: {numbers1}, numbers2: {numbers2}')
# 
# Q13: 	Vad är snittet (intersection) mellan variablerna `numbers1 `och `numbers2`?
# A13: 	{2, 3}
print(f'A13: {numbers1 & numbers2}') # set1 intersect set2
#
# Q14: 	Vad är unionen mellan variablerna `numbers1` och `numbers2`?
# A14:  {1, 2, 3, 3, 4, 6, 7}
print(f'A14: {numbers1 | numbers2}') # set1 union set2
#
# Q15: 	Vilken är den symmetriska differensen mellan `numbers1` och `numbers2`?
# A15: 	{1, 4, 6, 7}
print(f'A15: {numbers1 ^ numbers2}') # symmetric-diff set1 set2
#
