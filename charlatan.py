# charlatan.py
# charlatan crear un ficheiro de texto con palabras pseudoaleatorias que se toman 
# dunha lista que pode definir o programador

import random

ficheiro = open("charlatan.txt","a") 
PsudoRandomWords = ["Hamburguesa ", "Ensalada ", "Pizza ", "Bocadillo ", "Canelones ", "Whisky ", "Cocacola ","Limonada ", "Churrasco ", "Empanada "]

index = 0
#Increase the range to make a bigger file
#15000000 -> 112MB
#30000000 -> 223MB

numero_palabras = 150000000

for x in range(numero_palabras):
   index = random.randint(0,9)
   ficheiro.write(PsudoRandomWords[index])
   if x % 20 == 0:
      ficheiro.write('\n')
