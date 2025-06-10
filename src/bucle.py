import random

numeroSecreto= random.randint(1,10)
adivinado = False

while not adivinado: 
    intento = int(input ("Adivina el numero (1-10)"))
    if intento== numeroSecreto: 
        print("✅Ganastes!")
        adivinado = True
    else:
        print("❌Intenta devuelta")
        







