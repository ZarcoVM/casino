import random

colores = ["rojo", "negro"]
numeros = range(0, 37)

numero_usuario = int (input("Elige un numero: "))
color_usuario = input("Elige un color: ")

if numero_usuario not in numeros or
color_usuario.lower() not in colores:
  print("ERROR, DATOS NO VALIDOS")
  quit()

color_ganador = random.choice
