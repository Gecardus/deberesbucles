contador=0
lista=[]
while contador<3:
    nombre=input("Introdueix un nom: ")
    contador+=1
    lista.append(nombre)
    
print("Les paraules concatenades són " + str(lista))