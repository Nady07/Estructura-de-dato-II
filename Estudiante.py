class Estudiante:
    """
    Clase que representa a un estudiante con nombre, edad y calificación.

    Métodos getter y setter incluidos para cada atributo.
    """

    def __init__(self, nombre, edad, calificacion):
        self._nombre = nombre
        self._edad = edad
        self._calificacion = calificacion

    def obtener_nombre(self):
        return self._nombre

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_edad(self):
        return self._edad

    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser un número positivo.")

    def obtener_calificacion(self):
        return self._calificacion

    def establecer_calificacion(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 100:
            self._calificacion = nueva_calificacion
        else:
            print("La calificación debe estar entre 0 y 100.")

    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        print(f"Calificación: {self._calificacion}")


if __name__ == "__main__":
    estudiante = Estudiante("Lucía", 20, 85)
    estudiante.mostrar_informacion()

    print("\nActualizando edad y calificación...\n")
    estudiante.establecer_edad(21)
    estudiante.establecer_calificacion(95)
    estudiante.mostrar_informacion()
