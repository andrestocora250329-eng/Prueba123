
"""
Ejercicio resuelto 2:
Programa para convertir temperaturas entre Celsius,
Kelvin y Fahrenheit.
"""


def parar():
    """Pausa el programa hasta que el usuario presione ENTER."""
    input("Presione <ENTER> para continuar")


def capturar():
    """Captura la temperatura ingresada por el usuario."""
    try:
        temperatura = float(
            input("Por favor digite la temperatura: ")
        )
        return temperatura
    except ValueError as error:
        print(error)
        return None


def celsius_fahrenheit(c):
    """Convierte Celsius a Fahrenheit."""
    return (c * 9 / 5) + 32


def celsius_kelvin(c):
    """Convierte Celsius a Kelvin."""
    return c + 273.15


def kelvin_fahrenheit(k):
    """Convierte Kelvin a Fahrenheit."""
    return (k - 273.15) * 9 / 5 + 32


def kelvin_celsius(k):
    """Convierte Kelvin a Celsius."""
    return k - 273.15


def fahrenheit_kelvin(f):
    """Convierte Fahrenheit a Kelvin."""
    return (f - 32) * 5 / 9 + 273.15


def fahrenheit_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9


def main():
    """Ejecuta el menú principal de conversiones."""
    temperatura = 0.0
    continuar = True

    while continuar:
        print("\nSeleccione una opción:")
        print("1 --> Capturar temperatura")
        print("2 --> Celsius a Fahrenheit")
        print("3 --> Celsius a Kelvin")
        print("4 --> Kelvin a Fahrenheit")
        print("5 --> Kelvin a Celsius")
        print("6 --> Fahrenheit a Kelvin")
        print("7 --> Fahrenheit a Celsius")
        print("0 --> Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            resultado = capturar()
            if resultado is not None:
                temperatura = resultado
            else:
                print("Temperatura no válida.")
            parar()

        elif opcion == "2":
            print(
                f"{temperatura} °C = "
                f"{celsius_fahrenheit(temperatura)} °F"
            )
            parar()

        elif opcion == "3":
            print(
                f"{temperatura} °C = "
                f"{celsius_kelvin(temperatura)} K"
            )
            parar()

        elif opcion == "4":
            print(
                f"{temperatura} K = "
                f"{kelvin_fahrenheit(temperatura)} °F"
            )
            parar()

        elif opcion == "5":
            print(
                f"{temperatura} K = "
                f"{kelvin_celsius(temperatura)} °C"
            )
            parar()

        elif opcion == "6":
            print(
                f"{temperatura} °F = "
                f"{fahrenheit_kelvin(temperatura)} K"
            )
            parar()

        elif opcion == "7":
            print(
                f"{temperatura} °F = "
                f"{fahrenheit_celsius(temperatura)} °C"
            )
            parar()

        elif opcion == "0":
            print("Bye")
            continuar = False

        else:
            print("Seleccione una opción válida.")


if __name__ == "__main__":
    main()