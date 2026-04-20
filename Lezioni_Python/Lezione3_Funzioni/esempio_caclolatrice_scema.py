# Crea uno script che esegue tutte le 4 operazioni matematiche di base ma solo con 2 numeri

import time

def somma(x,y):
    return x + y

def prodotto(x,y):
    res = x * y
    return res

def differenza(x,y):
    diff = x - y
    return diff

def quoziente(x,y):
    return x / y
    

def calcola_tutto(x,y):
    print("Sto calcolando tutto...")
    time.sleep(2)
    # print("Risultati delle 4 operazioni:")
    # print("Somma: ", somma(x,y))
    # print("Prodotto: ", prodotto(x,y))
    # print("Differenza: ", differenza(x,y))
    # print("Quoziente: ", quoziente(x,y))
    res_somma = somma(x,y)
    res_prod = prodotto(x,y)
    res_diff = differenza(x,y)
    res_quoz = quoziente(x,y)
    print("Risultati operazioni\n")
    print("Somma: ", res_somma)
    print("Prodotto: ", res_prod)
    print("Differenza: ", res_diff)
    print("Quoziente: ", res_quoz)


# calcola_tutto(9, 5)

def raccogli_numeri():
    print("Dovrai inserire dei numeri")
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    calcola_tutto(num1, num2)

raccogli_numeri()