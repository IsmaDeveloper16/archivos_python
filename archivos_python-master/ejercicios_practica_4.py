# CODE:39
# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

def desafio(ambientes):
    contador_2 = 0
    contador_3 = 0 
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'
    with open('propiedades.csv') as csvfile:
        propiedades = list(csv.DictReader(csvfile))
    for data in propiedades:
        try:
            ambi = data["ambientes"]
        except:
            pass
        if ambi == "2":
            contador_2 += 1
        elif ambi == "3":
            contador_3 += 1
    if ambientes == "2_ambientes":
        print ("estos son la cantidad de departamentos con 2 ambientes: ", contador_2)
        return contador_2
    elif ambientes == "3_ambientes":
        print("esta es la cantidad de departamentos con 3 ambientes: ", contador_3)
        return contador_3
    else:
        print("valor ingresado no disponible, prueba con 2_ambientes o 3_ambientes para ver los departamentos disponibles.")

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("2_ambientes")
