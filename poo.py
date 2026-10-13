class Vehiculo:
    def __init__(self, marca, color, velocidad, puertas):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad
        self.puertas = puertas

    def mostrar(self):
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, color, velocidad,sonido):
        super().__init__(marca,color,velocidad,0)
        self.sonido = sonido

    def ruido(self):
        print(f"marca:{self.marca}")
        print(f"sonido:{self.sonido}")

Vehiculos = []

while True: 
    print("\n1. Crear vehiculo")
    print("2. Crear moto")
    print("3. Ver vehiculos")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        marca = input("Marca: ")
        color = input("Color: ")
        velocidad = input("Velocidad: ")
        puertas = input("Número de puertas: ")

        Vehiculo = Vehiculo(marca, color, velocidad, puertas)
        Vehiculos.append(Vehiculo)

        print("vehiculo agregado✅")

    elif op == "2":
        marca = input("marca: ")
        color = input("color: ")
        velocidad = input("velocidad: ")
        sonido = input("sonido de la moto: ")
        moto= Moto (marca,color,velocidad,sonido)
        Vehiculos.append(moto)
        print("moto agregado✅")
     

    elif op == "3":
           if len(Vehiculos)==0:
               print ("no hay vehiculos registrados.")
           else:
               for i, Vehiculo in enumerate(Vehiculos):
                print(f"\nvehiculo {i+1}")
                Vehiculo.mostrar()
                if isinstance(Vehiculo,Moto):
                    Vehiculo.ruido()
    elif op =="4":
        print("programa finalizado")
        break
    else:
        print("Opción inválida❌")