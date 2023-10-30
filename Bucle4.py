contador=0
altitud=int(input("Introduce lo alto que sera el triangulo: "))
contador2=altitud-1
while contador<=altitud:
    a="*"
    a=a*contador
    print(a)
    contador+=1
while contador2>=1:
    a2="*"
    a2=a2*contador2
    print(a2)
    contador2-=1