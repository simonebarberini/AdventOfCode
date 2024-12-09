from funzioni import *

sinistra, destra = separa_colonne_da_file("Sfida1/input.txt")

somma = 0


lenght = len(sinistra)

i = 0

for i in range(lenght):
    sin = minimo_lista(sinistra)
    des = minimo_lista(destra)
    distanza = abs(des - sin)
    sinistra.remove(sin)
    destra.remove(des)
    somma += distanza


print(somma)



