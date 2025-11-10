# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan") #muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"{summa(x, y)}") # muutos bugikorjaus-branchissa
print(f"{erotus(x, y)}") # muutos bugikorjaus-brancissa
=======
print(f"{summa(x, y)}") # muutos mainissa
print(f"{erotus(x, y)}") # muutos mainissa
>>>>>>> main

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa
