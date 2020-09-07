

#Uppgift 1. Skriv ett program som hälsar användaren 10 gånger.
​
indx = 0
​
while indx < 10: #räknaren går från 0-9, mao 10 gånger
    print("Hello user")
    indx+=1

'''Uppgift 2. Skriv ett program (med for-loop) som skriver ut följande:
1
22
333
4444
55555
666666
7777777
88888888
999999999'''

for indx in range(10): #n.b. range går -upp till- 10, ej inklusive
    for second_indx in range(indx): #gå igenom alla tal från 0 till nuvarande varvets tal
        print(indx, end="") #utan end="" får vi ny rad efter varje print
    print("\r") #när vi är klara att printa denna runda tal, gå till start av rad


#Alternativ lösning:

for indx in range(10):
   print(str(indx)*indx) #gånger-tecknet gör att print upprepar det som står i string:en index antal gånger


'''Uppgift 3. Skriv ett program som låter användaren gissa vilket tal du tänker på tills användaren gissar rätt.
Talet har du hårdkodat in i programmet och gissningen från användaren hämtas in via input gång på gång tills dess att gissning == input.'''
secret = 42
guess = 0
​
while secret != guess:
    guess = int(input("Enter an integer from 1 to 99: ")) 
    #Input hämtas här, kontrollen att secret !=guess görs senare. 
    #Därav exekveras else-satsen om guess ==secret, därefter skrivs Well done guessing ut
    if guess < secret:
        print("guess is too low")  
    elif guess > secret:
        print("guess is too high")
    else:
        print("you guessed it!")
        break
print("Well done guessing")

'''Uppgift 4 Skriv ett program som loopar över en lista innehållandes olika tal.
Om programmet stöter på ett ojämnt tal skrivs orden “Not allowed!” ut och loopen avbryts'''
​
number_array = [0, 2, 4, 6, 7, 8]
for number in number_array:
    if(number % 2 !=0): #om ej är jämt delbart med 2, dvs om talet är udda.
        print("Number not allowed", number)
        break
​
'''Uppgift 5
Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar
talet och dess position i first_list och skriver resultatet som en lista av tupler.'''

first_list = [3, 7 ,9, 2, 6]
second_list = [2, 3, 6, 7, 9]
​
result = []
for number in second_list: #Gå igenom alla tal i second_list
    result.append((number, first_list.index(number))) #hämta talets index i den första listan.
    #Lägg talet i en tupel tillsammans med detta index, och lägg till det i resultatlistan
print(result)

'''Uppgift 6
Upprepa uppgiften ovan, men använd denna gång list comprehension för att lösa problemet.'''


print([(number, first_list.index(number)) for number in second_list])
#Ta den gamla listan, gå igenom alla talen i den. Sätt in dem i en tupel tillsammans med talets index i first_list

#Alternativ lösning då man först sparar undan listan
result_list = [(number, first_list.index(number)) for number in second_list]
print(result_list)

'''Uppgift 7 - Handlingskorg
Du har följande lista på frukter:
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin
korg, och sedan fyller du denna korg (en lista) med frukter genom att loopa igenom
frukt-listan tills dess att korg-listan är full.'''

space_in_basket = 10
my_basket = []
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
​
for indx in range(space_in_basket):
    current_fruit_number = indx % len(fruits) #modulo ser till att vi inte "trillar över kanten" på index
    current_fruit = fruits[current_fruit_number]
    my_basket.append(current_fruit)
​
print(my_basket)
['apple', 'orange', 'pear', 'banana', 'grapes', 'apple', 'orange', 'pear', 'banana', 'grapes']

'''Uppgift 8 Skriv ett program som använder sig av nästlade while-loopar för att skriva ut alla primtal som är mindre än 100.
Vägledning: Primtal är ett tal som är större än 1 och som inte går att dela jämnt med
något tal annat än sig själv och 1.'''

i = 2
while(i < 100):
   j = 2
   while(j <i):
      if not(i%j): #alltså, om i modulo j INTE är lika med 0. Ex. 5%2 uppfyller detta krav 
        break
      j = j + 1
   if (j > i/j) : 
       print( i, " is prime")
   i = i + 1
​
print("Good bye!")


'''Extrauppgift Julius Caesars krypto
Din uppgift är nu att skriva ett program som krypterar text enligt någon form av
caesarskiffer (du får alltså själv välja hur många skiftningar du vill göra).
Skriv ett program som låtar användaren mata in hur många skiftningar hen vill ha, och
därefter mata in den text som hen vill få krypterad'''

input_text = input("Please write the text you wish to get encrypted ")
input_text = input_text.lower()
step = int(input("Please write the amount of shifts you'd like to use "))
​
encrypted_text = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä','ö']
​
for letter in input_text:
    if letter in alphabet:
        index = alphabet.index(letter)
        crypto_index = (index + step) % 29 #modulo igen! för att se till att index < len(minLista)
        encrypted_letter = alphabet[crypto_index]
        encrypted_text.append(encrypted_letter)
    else:
        print("Wrong format, only letters allowed")
        print("Forbidden input was: " + letter)
​
​
print(encrypted_text)

