# While fa parte della famiglia dei cicli indefiniti

# Simulo il comportamento del ciclo for con un while

counter = 0

while counter < 10:
    print(f"Il contatore vale: {counter}")
    counter+=1

# ESEMPIO: trova la parola chiave

password = "abcdef"
tentativoUser = ""
numTentativi = 0

while tentativoUser != password:
    tentativoUser = input("Inserisci la password\n")
    numTentativi += 1

print(f"Bravo, hai trovato la password in {numTentativi} tentativi")


# Bloccare un ciclo infinito con BREAK
contatore = 1

while True:
    print(contatore)
    contatore += 1
    if contatore >= 100:
        break #Il break, usato all'interno degli if interrompe il ciclo che wrappa

print("Sono uscito dal while interrompendo lo statement")

#Saltare un giro con CONTINUE
numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0:
        continue

    print(numero)

#Esempio con lista
#Data una lista di numeri se leggi il numero 42 stampa DON'T PANIC, per tutti gli altri stampa solo il numero
listaNumeri = [80, 23, 11, 65, 1, 42, 3, 18, 26 ]

for num in listaNumeri:
    if num == 42:
        print("DON'T PANIC !!")
        # continue
        break

    print(num)

# Validazione Input

print("Validazione input utente")

while True:
    eta = int(input("Inserisci la tua età"))

    if eta < 0 or eta > 120:
        print("Età inserita non valida, riprova")
        continue
    
    print(f"Hai inserito {eta} anni")
    break
