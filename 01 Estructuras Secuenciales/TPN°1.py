#Ej1
variable=" "
print(bool(variable))

print("hola mundo")

#Ej2

nombre=input("Por favor ingrese su nombre ")
print(f"Hola {nombre} ")

#Ej3

nombre= input("Por favor ingrese su nombre ")
apellido= input("Por favor ingrese su apellido ")
edad= input("Por favor ingrese su edad ")
residencia = input("Por favor ingrese su nresidencia ")

print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#Ej4

radio= float(input("ingrese el radio del circulo "))
area= 3.1416 *radio ** 2
perimetro= 2*radio*3.1416

print(f"El area es {area}, el perimetro es {perimetro}")


#Ej5

segundos=int(input("Por favor ingrese segundos"))
minutos = (segundos/60)
print(f"Los {segundos} segundos, equivalen a {minutos} minutos")

#Ej6

numero= int(input("Por favor ingrese un numero y se le devolvera la tabla de multiplicar"))
print(f"1*{numero} =  {1*numero} ")
print(f"2*{numero} =  {2*numero} ")
print(f"3*{numero} =  {3*numero} ")
print(f"4*{numero} =  {4*numero} ")
print(f"5*{numero} =  {5*numero} ")
print(f"6*{numero} =  {6*numero} ")
print(f"7*{numero} =  {7*numero} ")
print(f"8*{numero} =  {8*numero} ")
print(f"9*{numero} =  {9*numero} ")
print(f"10*{numero} =  {10*numero} ")

#Ej7

numero1= int(input("Ingeres un numero distinto de cero "))
numero2= int(input("Ingrese otro numero distinto de cero "))
suma= numero1+numero2
resta = numero1-numero2
multiplicacion = numero1*numero2
division = numero1/numero2

print(f"La suma es: {suma}. La resta es: {resta}. La multiplicacion es: {multiplicacion}. La divison es: {division}")

#Ej8

peso= float(input("Por favor ingrese su peso "))
altura= float (input("Por favor ingrese su altura "))
IMC= peso/(altura**2)
print(f"El IMC es: {IMC}")


#Ej9
grados_celcius= float(input("Por favor ingrese la temperatura en grados celcius"))
grados_farenheit= (9/5)*grados_celcius+32

print(f"La temperatura en Farenheit es: {grados_farenheit}")


#Ej10

num1= int(input("Por favor ingrese un numero"))
num2= int(input("Por favor ingrese un numero"))
num3= int(input("Por favor ingrese un numero"))
prom= (num1+num2+num3)/3

print(f"El promedio es: {prom}")

