# OPERATORI LOGICI
# AND logico  
# OR logico

# booleano prodotto sulla base della tabella delle verità

#  cond1  |  cond2  |  cond1 and cond2 | cond1 or cond2
#    T         T              T                T
#    F         T              F                T
#    T         F              F                T
#    F         F              F                F

# Esempio and logico. Per poter accedere al corso devo essere maGGIORENne e avere un titolo valido
miaEta = 16
titoloValido = False

if miaEta >= 18 and titoloValido:
    print("Ciao, puoi partecipare al corso")
elif miaEta < 18 and titoloValido:
    print("Mi spiace, non sei ancora maggiorenne pur avendo un titolo valido")
elif miaEta >= 18 and not titoloValido:
    print("Mi spiace sei maggiorenne ma non hai un titolo valido")
else:
    print("Mi spiace, non puoi partecipare perché sei minorenne e non hai un titolo valido")


# In altri corsi posso partecipare in due modi: o sono maggiorenne oppure ho un titolo valido

if miaEta >= 18 or titoloValido:
    print("Puoi parrtecipare")
else:
    print("Non puoi partecipare")