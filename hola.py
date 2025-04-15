# #declaracion de variables
# nombre="Link"
edad=64
# #ejemplo de concatenacion
# print("Hola", nombre, "y su edad es", edad)

# print("ingrese su nombre")
# nombre=input()

# print("Hola", nombre, "y su edad es", edad)

# n1=9
# n2=20
# print(n1+n2)

# #suma de dos numeros
# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# print("el resultado de la suma es" , n1+n2)

# #sacar promedio 3 numeros
# print("Ingrese 3 numeros  para sacar su promedio")
# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# n3=int(input("ingrese un numero "))
# prom=(n1+n2+n3)/3
# print("el promedio es" , prom)

# if prom>=40:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")

# # varificacion de mayoria de edad
# edad=int(input("ingrese si edad "))

# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

# # "niño" menor de 12
# #adolescente entre 12 y 17
# #mayor de edad mas o igual  a 18

# edad = int(input("ingrese su edad: "))

# if edad < 12:
#     print("tiene", edad, "por tanto es un niño")
# elif edad >= 12 and edad <= 17:
#     print("tiene", edad, "por tanto es adolescente")
# else:
#     print("tiene", edad, "por tanto es mayor de edad")

# #ingrese 3 numeros y muestre el mayor de ellos

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese otro numero "))
# n3=int(input("ingrese otro numero "))

# if n1>n2 and n1>n3:
#     print(" EL numero ", n1, "es el mayor")
# elif n2>n3:
#     print(" EL numero ", n2, "es el mayor")
# else:
#     print(" EL numero ", n3, "es el mayor")


n1=int(input("ingrese un numero "))

if n1 % 2==0:
    print("El numero es par")
else:
    print("El numero es impar")