#If Statement. Serve a controllare il valore di un confronto (condizione). Quello che si trova sotto l'if (body dell if) viene eseguito se la condizione è true

piove = True

if piove:
    print("Porto l'ombrello")
    print("Metto anche il Kway")



mioNumero = 5
tuoNumero = 30

if mioNumero > tuoNumero:
    print("Ho vinto io ")
else:
    print("Hai vinto tu")

# utilizzo int() per cast del dato. ATT: tutto ciò che recupero dall'input è SEMPRE una string. volendo confrontare dei numeri dei eseguire  il cast
miaEta = int(input("Quanti anni hai ?"))

if miaEta >= 18:
    print("Sei maggiorenne")
elif miaEta <= 0:
    print("Mi hai un valore non valido")
else:
    print("Sei minorenne")

# Questo sotto non può funzionare
if miaEta >= 18:
    print("Sei maggiorenne")
elif miaEta < 18:
    print("Sei minorenne")
else:
    print("Valore negativo, no valido")

# Questa sotto funziona tranquillamente
if miaEta < 0:
    print("Valore non valido")
elif miaEta < 18:
    print("Sei minorenne")
else:
    print("Sei maggiorenne")

# miaEta2 = input("Quanti anni hai oggi ?")
# if type(miaEta2) == int:
#     if miaEta2 < 0:
#         print("Valore non valido")
#     elif miaEta2 < 18:
#         print("Sei minorenne")
#     else:
#         print("Sei maggiorenne")
# else:
#     print("Mi stai dando qualcosa che non è un numero")

parolaChiave = input("Qual è la parola chiave ?")

if parolaChiave == "apritiSesamo":
    print("Benvenuto, puoi entrare")
else:
    print("Mi spiace, non puoi entrare")


parola = "Ciao"
saluto = "Addio"

if parola.lower() == saluto.lower():
    print("Le due parole sono identiche")
else:
    print("Le due parole sono diverse")

