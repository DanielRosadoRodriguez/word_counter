# Este es un comentario y no se debe contar como línea física.

"""Docstring de módulo
Este docstring abarca varias líneas y no se contará.
"""

import os  # Importa módulo os (línea lógica)
import sys  # Importa módulo sys (línea lógica)

# Definición de una clase
class MiClase:
    """Docstring de la clase (no se cuenta)"""
    atributo = 42  # Asignación a nivel de clase (línea lógica)

    def __init__(self, valor):
        self.valor = valor  # Asignación en el constructor (no se cuenta dentro del cuerpo de la función)

    def metodo(self):
        """Docstring del método (no se cuenta)"""
        if self.valor > 0:
            print("Positivo")  # No se cuenta el cuerpo
        elif self.valor == 0:
            print("Cero")  # Cada cabecera if/elif cuenta 1 línea lógica
        else:
            print("Negativo")  # else cuenta 1 línea lógica

x=10;y=10
# Definición de una función
def funcion_prueba(a, b):
    """Función que suma dos números (cabecera cuenta 1 línea lógica)"""
    x = a  # Asignación (línea lógica)
    y = b  # Asignación (línea lógica)
    total = (x + y +
             0)  # Instrucción con continuación, cuenta como 1 línea lógica
    return (total +
            1)  # Sentencia return (línea lógica)

# Asignación de una expresión lambda (se rige por la regla de asignación)
f = lambda x: x * 2

# Uso de with: cuenta 1 línea lógica
with open("archivo.txt", "w") as f_archivo:
    f_archivo.write("Prueba")

# Bucle for con try-except-else-finally
for i in range(3):
    try:
        resultado = funcion_prueba(i, i + 1)  # try cuenta 1 línea lógica
    except Exception as e:
        print("Error:", e)  # cada except cuenta 1 línea lógica
    else:
        print("Resultado:", resultado)  # else cuenta 1 línea lógica
    finally:
        print("Finalizado")  # finally cuenta 1 línea lógica

if (
    x and
    y == 3
    ):
    print("hello")