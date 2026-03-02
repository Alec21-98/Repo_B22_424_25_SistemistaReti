# Le variabili sono "contenitori" di un'informazione singola
# Il valore di una variabile, può cambiare nel corso dello script
# Le variabili devono avere dei nomi "parlanti"
# Regole per la denominazione
# camelCase (saldoConto)
# PascalCase (SaldoConto)
# snake_case (saldo_conto)
# kebab-case (saldo-conto) SCONSIGLIATO
# UPPER_CASE (SALDO_CONTO) Solitamente utilizzato con le costanti
# 

#Istanzio una variabile (dichiaro e assegno un valore)
nome = "Dario"
cognome = "Mennillo"
eta = 36 #i numeri non hanno bisogno di ""
corsi = 5
studentiTotali = 250
corsoAttuale = "Sistemista Reti"

#Richiamo le variabili (leggere il suo valore)
#Utilizzo la , per concatenare variabili e stringhe
print("Ciao mi chiamo",nome,"sono un docente sul corso", corsoAttuale, "in totale ho", studentiTotali, "studenti")

#Facciamo un po' di matematica d'Egitto
num1 = 52
num2 = 41

somma = num1 + num2
differenza = num1 - num2
prodotto = num1 * num2
quoziente = num1 / num2

print("I risultati delle operazioni sono: ")
print("Somma: ", somma)
print("Diff: ", differenza)
print("Prod: ", prodotto)
print("Quoz", quoziente)