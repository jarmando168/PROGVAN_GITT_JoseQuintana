# PROGVAN_GITT_JoseQuintana
Practica 1&2
 Jose Armando Quintana Denis

Primera pregunta: Chatgpt -> Hola, necesito ayuda urgente, tengo el siguiente codigo :

def leer_numeros():
    """Lee una lista de números enteros del usuario y la devuelve."""
    numeros = []
    while True:
        try:
            numero = int(input("Ingrese un número (o 'q' para salir): "))
            if numero == 'q':
                break
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    return números

Mi problema era a la hora de pedir números, los pide bien pero cuando presiono 'q' no se sale de la petición.

La resolución que me proporciono Chatgpt es no convertir la entrada del usuario a un numero entero con int().

Segunda pregunta: Gemini -> Como puedo agregar un limite de tareas para que no sobrepase la "memoria" de un ordenador.

La resolución que me proporciono Gemini fue definir una variable global (MAX_TAREAS) y  mediante el comando if len(tareas)<MAX_TAREAS limitamos el numero de tareas dadas por el usuario.


Tercera pregunta: Gemini -> Le he ordenado con una orden autoritaria que me realice las dos ultimas funciones del ejercicio 6.

Me ha dado varias soluciones utilizando el operador "is" para verificar si dos cadenas son en realidad el mismo objeto.


Cuarta pregunta: Gemini -> Le he preguntado como se modificaría el codigo para mostrar las cadenas con longitud menor de 10.
Con las líneas len(cadena)<10 y  cadenas_cortas.append(cadena) realizamos un bucle for para imprimir las cadenas cortas.



