#ejercicios condicionales (Lucas godoy, Ramiro salcedo, Sofia blangetti y Valentina albizu)

#ejrcicio 1 - sistema de becas estudiantiles
Nombre_apellido = input("ingrese nombre y apellido: ")

edad = int(input("ingrese su edad: "))

if (edad <= 17 or edad >= 70 ):
    print("edad invalida")  
else: 
    nom_edad= (f"{Nombre_apellido}, {edad} años")

promedio = float(input("ingrese su promedio: "))

if (promedio <= 0 or promedio >= 10):
  print("promedio invalido")
else:
    if(promedio < 6):
        print("Beca rechazada")
    else: 
        prom= (f"promedio:{promedio}") 

ingresos = int(input("ingrese sus ingresos $: "))

if (ingresos <= 0):
     print("ingresos invalidos ")
elif (ingresos < 300000):
   beca= ("Beca Completa")
elif (ingresos >= 300000 and ingresos <= 600000):
   beca = ("Media beca")
elif (ingresos >600000):
    beca= ("Beca Rechazada")


print("---DATOS DEL POSTULANTE DE LA BECA---")

print(f"✔ {nom_edad}")
print(f"Promedio: {prom}")
print(f"Ingresos: {ingresos:2f})
      