import numpy as np

class CMatFloat:
    """Clase que representa una matriz dinámica 1D/2D."""

    def __init__(self):
        """Inicializa los atributos de la matriz con None y las dimensiones a 0."""
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """Crea una matriz bidimensional de ceros con dimensiones especificadas."""
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """Crea una matriz unidimensional de ceros usando CrearMatriz2D."""
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """Permite al usuario introducir valores decimales en la matriz."""
        if self.Existe():
            for i in range(self._m_nFilas):
                for j in range(self._m_nColumnas):
                    valor = leer_float(f"Introduce el valor para [{i}, {j}]: ")
                    self._Matriz[i, j] = valor
        else:
            print("Primero debe crear una matriz.")

    def Mostrar(self):
        """Muestra la matriz actual si está creada."""
        if self.Existe():
            print("Matriz:")
            print(self._Matriz)
        else:
            print("La matriz no ha sido creada.")

    def Existe(self):
        """Verifica si la matriz está creada y no vacía."""
        return self._Matriz is not None

    def SumarMatrices(self, otra_matriz):
        """Suma la matriz actual con otra matriz, si tienen las mismas dimensiones."""
        if self.Existe() and otra_matriz.Existe():
            if (self._m_nFilas, self._m_nColumnas) == (otra_matriz._m_nFilas, otra_matriz._m_nColumnas):
                return self._Matriz + otra_matriz._Matriz
            else:
                print("Las matrices deben tener las mismas dimensiones.")
        else:
            print("Ambas matrices deben estar creadas.")
        return None

    def RestarMatrices(self, otra_matriz):
        """Resta otra matriz de la matriz actual, si tienen las mismas dimensiones."""
        if self.Existe() and otra_matriz.Existe():
            if (self._m_nFilas, self._m_nColumnas) == (otra_matriz._m_nFilas, otra_matriz._m_nColumnas):
                return self._Matriz - otra_matriz._Matriz
            else:
                print("Las matrices deben tener las mismas dimensiones.")
        else:
            print("Ambas matrices deben estar creadas.")
        return None

# Funciones auxiliares

def leer_int(mensaje="Introduce un número entero: "):
    """Lee un número entero del usuario, repite si la entrada es inválida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    """Lee un número decimal del usuario, repite si la entrada es inválida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, introduce un número decimal válido.")

def crear_menu(opciones_menu):
    """Muestra un menú y retorna la opción seleccionada por el usuario."""
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    return leer_int("Seleccione una opción: ")

# Función principal con menú

def main():
    matriz = CMatFloat()
    while True:
        print("\nMenú Principal")
        opcion = crear_menu([
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ])

        if opcion == 1:
            nElementos = leer_int("Introduce el número de elementos para la matriz 1D: ")
            matriz.CrearMatriz1D(nElementos)
            print("Matriz 1D creada.")

        elif opcion == 2:
            nFilas = leer_int("Introduce el número de filas: ")
            nColumnas = leer_int("Introduce el número de columnas: ")
            matriz.CrearMatriz2D(nFilas, nColumnas)
            print("Matriz 2D creada.")

        elif opcion == 3:
            matriz.Introducir()

        elif opcion == 4:
            matriz.Mostrar()

        elif opcion == 5:
            print("\nSubmenú de Operaciones con Matrices")
            sub_opcion = crear_menu([
                "Sumar matrices",
                "Restar matrices",
                "Volver al menú principal"
            ])

            if sub_opcion == 1:
                otra_matriz = CMatFloat()
                nFilas = matriz._m_nFilas
                nColumnas = matriz._m_nColumnas
                otra_matriz.CrearMatriz2D(nFilas, nColumnas)
                otra_matriz.Introducir()
                resultado = matriz.SumarMatrices(otra_matriz)
                if resultado is not None:
                    print("Resultado de la suma:")
                    print(resultado)

            elif sub_opcion == 2:
                otra_matriz = CMatFloat()
                nFilas = matriz._m_nFilas
                nColumnas = matriz._m_nColumnas
                otra_matriz.CrearMatriz2D(nFilas, nColumnas)
                otra_matriz.Introducir()
                resultado = matriz.RestarMatrices(otra_matriz)
                if resultado is not None:
                    print("Resultado de la resta:")
                    print(resultado)

        elif opcion == 6:
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()
