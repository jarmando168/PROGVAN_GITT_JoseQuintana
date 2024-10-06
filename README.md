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


Quinta pregunta: Chatgpt -> ¿Por qué es importante el uso de excepciones en Python?
 La LLM explica que el uso de excepciones es esencial para manejar errores de forma controlada, evitando que el programa falle inesperadamente. En este caso, la excepción ValueError se usa correctamente para controlar entradas no numéricas en el código.

Conclusión: Respuesta correcta. El manejo de excepciones asegura que los programas respondan a errores de manera controlada, mejorando la robustez del código.


Sexta pregunta: Chatgpt -> ¿Qué sucede si una cadena vacía es ingresada en la función comparar_objetos?
 La LLM aclara que si una cadena vacía es ingresada, la función comparar_objetos devolvería "Cadenas no encontradas en la lista", a menos que haya cadenas vacías almacenadas en la lista original.

Conclusión: Respuesta correcta. La comparación de objetos en Python considera las cadenas vacías como válidas, pero la lógica de la función debe estar preparada para manejarlas correctamente.


Séptima pregunta: Chatgpt -> ¿Qué cambios recomiendas para que el código sea más fácil de entender?
Chatgpt me sugiere añadir más comentarios dentro de las funciones para explicar mejor el propósito de cada una, así como utilizar nombres de variables más descriptivos. También propone simplificar algunas estructuras de control, como los bucles for o las comparaciones.

