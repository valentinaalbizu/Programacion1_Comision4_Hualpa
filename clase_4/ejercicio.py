#Generar una matriz con nombres engrupos de 4

import random

def generar_matriz_grupos(lista, tamaño_grupo=4):
    random.shuffle(lista)
    total_elementos = len(lista)
    cantidad_grupos = total_elementos // tamaño_grupo
    lista_recortada = lista[:cantidad_grupos * tamaño_grupo]

    matriz = []
    for i in range(0, len(lista_recortada), tamaño_grupo):
        grupo = lista_recortada[i:i + tamaño_grupo]
        matriz.append(grupo)
    return matriz

def buscar_grupo(nombre, matriz):
    for i, grupo in enumerate(matriz, start=1):
        if nombre in grupo:
            return i, grupo
    return None, None

nombres = [
    "Valentina De Los ángeles Albizú",
    "Pablo Andres Allende",
    "Luca Valentín Argumedo",
    "Pablo Avalos",
    "Lucas Avila",
    "Santino Barone",
    "Sofia Blangetti",
    "Nicolás Bohm",
    "Renzo Valentino Borello Canizo",
    "Juan Manuel Carrillo Taglio",
    "Facundo Gustavo Chacon Catalan",
    "Agustin Emiliano Contardi",
    "Jeronimo Coronel Alvarez",
    "Gabriel Emiliano Denis",
    "Facundo Gustavo Deseff",
    "Juan Martin García",
    "Enzo Giaquinta",
    "Sabrina Gimenez",
    "Joaquin Godoy",
    "Lucas Facundo Godoy",
    "Santino Alejo Godoy Galdeano",
    "Valentina Antonela Gordillo Moreno",
    "Lautaro Agustin Guardatti Esquivel",
    "Tiago Nahuel Guillot Duran",
    "Mateo Lautaro Liendo",
    "Juan Ignacio Martinez Quiroga",
    "Maximo Exequiel Monardez",
    "Tomas Agustin Mora Gonzalez",   "Pablo Isaias Morinigo Lima",
    "Ares Martín Ocaña Martinez",
    "Thiago Santino Oviedo Saldaño",
    "Amanda Lucrecia Pagano",
    "Máximo Juan Cruz Quiroga",
    "Facundo Agustín Ramírez García",
    "Franco Agustin Rios Alzamora",
    "Leonel Enrique Rojas",
    "Matias Nicolas Ruiz Vargas",
    "Ramiro Ezequiel Salcedo",
    "Ismael Saleme Padolsky",
    "Ignacio Exequiel Sanchez",
    "Fabrizio Jonathan Simon Santos",
    "Cristian Gabriel Soto",
    "Giovanna Mercedes Suarez",
    "Ismael Mauricio Suarez",
    "Fernando Agustín Torrez",
    "Luca Nicolas Valdez",
    "Tiziano Ignacio Valentini",
    "Matias Nicolas Vargas",
    "Juan Ignacio Videla Continella",
    "Pablo Exequiel Avalos"
]

matriz_grupos = generar_matriz_grupos(nombres)

for i, grupo in enumerate(matriz_grupos, start=1):
    print(f"Grupo {i}: {grupo}")

nombre_usuario= input("Ingresa tu nombre o el que deseas buscar para saber en que grupo se encuentra: ")

grupo_numero, grupo = buscar_grupo(nombre_usuario, matriz_grupos)

if grupo:
    print(f"{nombre_usuario} está en el Grupo {grupo_numero}: {', '.join(grupo)}")
else:
    print(f"{nombre_usuario} no se encuentra en los grupos generados.")

   
matriz_grupos = generar_matriz_grupos(nombres)


print("Grupos generados:")
for i, grupo in enumerate(matriz_grupos, start=1):
    print(f"Grupo {i}: {', '.join(grupo)}")


nombre_usuario = input("Ingresá tu nombre para saber en qué grupo estás: ")

grupo_numero, grupo = buscar_grupo(nombre_usuario, matriz_grupos)

if grupo:
    print(f"{nombre_usuario} está en el Grupo {grupo_numero}: {', '.join(grupo)}")
else:
    print(f"{nombre_usuario} no se encuentra en los grupos generados.")