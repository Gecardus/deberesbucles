factorial=1
numero=int(input("Introduce el numero del que quieres el resultado factorial: "))
contador=1
while contador <=numero:
    factorial*=contador
    contador+=1
print(factorial)