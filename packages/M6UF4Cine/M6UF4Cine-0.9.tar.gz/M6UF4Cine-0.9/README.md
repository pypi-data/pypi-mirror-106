# M06 UF4 - Cine

    pip install M6UF4Cine

Una vez tienes el proyecto solo tienes que importar las clases.

Después solo tienes que hacer tus propias funciones para resolver el problema o
puedes usar el main.py adjunto en el proyecto para probar las que ya estan hechas.

    from cine.Cine import *
    from cine.Pelicula import *
    from cine.Espectador import *

    import numpy as np
    from random import randint
    import pickle
    import time

    espectadores = list()


    def generarCine():
        binary_file = open('pickled_cine.bin', mode='wb')
        print('Generando cine...')
        cine = Cine('', generarPrecio())
        pickle.dump(cine, binary_file)
        binary_file.close()
        time.sleep(1.5)
        print('Ya está!')

        opcion = int(input('Quieres ver el precio de entrada?\n1. Si\t2. No\n'))

        if opcion == 1:
            binary_file = open('pickled_cine.bin', mode='rb')
            cine = pickle.load(binary_file)
            print(str(cine.precio) + '€')
            binary_file.close()

        elif opcion == 2:
            print('')


    def generarEspectadores():
        binary_file = open('pickled_espectadores.bin', mode='wb')
        nEspectadores = int(input('Introduce el numero de espectadores que quieres generar: '))
        print('Generando espectadores...')
        for i in range(nEspectadores):
            espectador = Espectador('Aleatorio{}'.format(i), generarEdad(), generarDinero())
            espectadores.append(espectador)
        pickle.dump(espectadores, binary_file)
        binary_file.close()
        time.sleep(2.5)
        print('Ya está!')

        for i in espectadores:
            print('Edad: ' + str(i.edad) + ' Dinero: ' + str(i.dinero))
        time.sleep(1)


    def generarPelicula():
        binary_file = open('pickled_pelicula.bin', mode='wb')
        print('Generando pelicula...')
        pelicula = Pelicula('', '', generarEdadMinima(), '')
        pickle.dump(pelicula, binary_file)
        binary_file.close()
        time.sleep(1.5)
        print('Ya está!')

        opcion = int(input('Quieres ver la edad minima de la pelicula?\n1. Si\t2. No\n'))

        if opcion == 1:
            binary_file = open('pickled_pelicula.bin', mode='rb')
            pelicula = pickle.load(binary_file)
            print(str(pelicula.edadMinima) + ' años')
            binary_file.close()

        elif opcion == 2:
            print('')


    def llenarSala(matriz):
        generarCine()
        generarPelicula()
        generarEspectadores()
        binary_file_pelicula = open('pickled_pelicula.bin', mode='rb')
        binary_file_cine = open('pickled_cine.bin', mode='rb')
        pelicula = pickle.load(binary_file_pelicula)
        cine = pickle.load(binary_file_cine)

        m = np.array(matriz)

        while haySitio(m) is True:
            for x in espectadores:
                if x.dinero > cine.precio and x.edad > pelicula.edadMinima:
                    for row in m[::-1]:
                        for elem in row:
                            if elem != '**':
                                m[randint(0, 7)][randint(0, 8)] = '**'
                                print('Siguiente!')
                                for i in m:
                                    print(str(i).replace('[', '').replace(']', '').replace("'", ''))
                else:
                    print('El espectador ' + x.nombre + ' no puede entrar al cine a ver la pelicula.')
                    continue
            haySitio(m)


    def haySitio(matriz):
        sitio = False

        for row in matriz:
            for elem in row:
                if elem != '**':
                    sitio = True
                elif elem == '**':
                    sitio = False

        return sitio


    def generarEdad():
        edad = randint(8, 100)
        return edad


    def generarPrecio():
        precio = randint(5, 20)
        return precio


    def generarEdadMinima():
        edadMinima = randint(8, 18)
        return edadMinima


    def generarDinero():
        dinero = randint(5, 20)
        return dinero


    def menu():
        print('1. Llenar sala')
        print('2. Salir')


    while True:

        menu()

        sala = [['8A', '8B', '8C', '8D', '8E', '8F', '8G', '8H', '8I'],
                ['7A', '7B', '7C', '7D', '7E', '7F', '7G', '7H', '7I'],
                ['6A', '6B', '6C', '6D', '6E', '6F', '6G', '6H', '6I'],
                ['5A', '5B', '5C', '5D', '5E', '5F', '5G', '5H', '5I'],
                ['4A', '4B', '4C', '4D', '4E', '4F', '4G', '4H', '4I'],
                ['3A', '3B', '3C', '3D', '3E', '3F', '3G', '3H', '3I'],
                ['2A', '2B', '2C', '2D', '2E', '2F', '2G', '2H', '2I'],
                ['1A', '1B', '1C', '1D', '1E', '1F', '1G', '1H', '1I']]

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            llenarSala(sala)
            print()

        elif opcion == '2':
            print("Saliendo...")
            time.sleep(1)
            break

URL's:

Repositorio github: https://github.com/daviduvi99/M6UF4Cine/tree/master

Repositorio pypi: https://pypi.org/project/M6UF4Cine/