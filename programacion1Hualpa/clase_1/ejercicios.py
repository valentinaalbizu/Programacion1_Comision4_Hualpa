#ejercicio 6

# calcula la calificación final de un alumno en la materia de Algoritmos.

calificacion_parcial_1 = float(input("Ingresa la primera calificación parcial: "))
calificacion_parcial_2 = float(input("Ingresa la segunda calificación parcial: "))
calificacion_parcial_3 = float(input("Ingresa la tercera calificación parcial: "))
calificacion_examen_final = float(input("Ingresa la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

promedio_parciales = (calificacion_parcial_1 + calificacion_parcial_2 + calificacion_parcial_3) / 3

peso_parciales = promedio_parciales * 0.55
peso_examen_final = calificacion_examen_final * 0.30
peso_trabajo_final = calificacion_trabajo_final * 0.15

calificacion_final = peso_parciales + peso_examen_final + peso_trabajo_final

print(f"La calificación final en la materia de Algoritmos es: {calificacion_final}")

#ejercicio 7

# convierte un monto en dólares a pesos colombianos, pesos argentinos y euros.

TASA_COP = 4100.0  # Tasa de cambio de 1 USD a pesos colombianos (COP)
TASA_ARS = 875.0   # Tasa de cambio de 1 USD a pesos argentinos (ARS)
TASA_EUR = 0.93    # Tasa de cambio de 1 USD a euros (EUR)

monto_dolares = float(input("Ingresa el monto en dólares (USD) que deseas convertir: "))

monto_cop = monto_dolares * TASA_COP
monto_ars = monto_dolares * TASA_ARS
monto_eur = monto_dolares * TASA_EUR

print("Resultados de la Conversión ")
print(f"Monto en pesos colombianos (COP): ${monto_cop}")
print(f"Monto en pesos argentinos (ARS): ${monto_ars}")
print(f"Monto en euros (EUR): €{monto_eur}")

#ejercicio 8

# calcula los costos y el tiempo de un viaje en auto.

CONSUMO_POR_100_KM = 8.0  # Litros por cada 100 km
VELOCIDAD_PROMEDIO_KMH = 90.0 # Velocidad promedio en km/h

distancia_km = float(input("Ingresa la distancia total del viaje en kilómetros: "))
precio_gasolina_litro = float(input("Ingresa el precio de la gasolina por litro: "))

litros_necesarios = (distancia_km / 100) * CONSUMO_POR_100_KM

costo_viaje = litros_necesarios * precio_gasolina_litro

tiempo_horas = distancia_km / VELOCIDAD_PROMEDIO_KMH

print("Resultados del Viaje")
print(f"Litros de gasolina necesarios: {litros_necesarios} L")
print(f"Costo total del viaje: ${costo_viaje}")
print(f"Tiempo total de viaje: {tiempo_horas} horas")

#ejercicio 9

# calcula los detalles de un préstamo bancario.

INTERES_MENSUAL = 0.02  # 2% de interés fijo mensual
NUMERO_DE_CUOTAS = 12   # El préstamo se paga en 12 meses

monto_solicitado = float(input("Ingresa el monto del préstamo solicitado: $"))

interes_total = monto_solicitado * INTERES_MENSUAL * NUMERO_DE_CUOTAS

monto_total_a_devolver = monto_solicitado + interes_total

valor_cuota_mensual = monto_total_a_devolver / NUMERO_DE_CUOTAS

print("Detalles del Préstamo")
print(f"Monto total a devolver: ${monto_total_a_devolver}")
print(f"Valor de cada cuota mensual: ${valor_cuota_mensual}")