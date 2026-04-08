# OPERATORI di CONFRONTO (producono un boolean)
# == uguale a ( 1 == 1 )
# != diverso
#  > maggiore
#  < minore
#  >= maggiore uguale
#  <= minore uguale

# Esempi
confronto1 = (10 > 5)
print(confronto1)

conf2 = (10 != 10)
print(conf2)

conf3 = 10 == 9
print(conf3)

parola = "Ciao"
saluto = "CIAO"

conf4 = (parola == saluto)
print(conf4)

# lower() metodo delle string che trasforma tutto in lowercase
conf5 = (parola.lower() == saluto.lower())
print(conf5)

# len() metodo di Py che conta il numero di caratteri in un string (incluso lo spazio)
conf6 = (parola.__len__() == saluto.__len__())
print(conf6)

lunghezzaParola = len(parola)
lunghezzaParola2 = parola.__len__()

print(lunghezzaParola)
print(lunghezzaParola2)