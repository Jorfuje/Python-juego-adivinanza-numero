

from curses.ascii import isdigit
import random


def juegoAdivinanza():
    # Genrar un número del 1 al 100
    numeroSecreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras l+íneas del juego donde se da la bienvenida
    print('¡Bienvenido al juego de adivinanza de números!')
    print('Debes de adivinar un número entre 1 y 100')
    print('¡Intenta adivinarlo')

    while not adivinado:
        # Solicitar un número del 1 al 100
        adivinanza = input('Introduce un número del 1 al 100: ')

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)                # Se pasa de string a entero
            intentos += 1
            if adivinanza < numeroSecreto:
                print(f'El número secreto es mayor a {adivinanza}')
            elif adivinanza > numeroSecreto:
                print(f'El número secreto es menor a {adivinanza}')
            else:
                print(f'¡Felicidades has ganado! El numero {adivinanza} es el numero secreto y lo has logrado en {intentos} intentos.')
        else:
            print('Por favor ingresa un número válido entre 1 y 100.')

juegoAdivinanza()