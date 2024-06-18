import os

CARGOS = ["CEO", "Desarrollador", "Analista de datos"]

trabajadores = []

def calcular_liquido(sueldo_bruto, cargo):
    if cargo == "CEO":
        descuento_de_salud = 70000
        descuento_de_afp = 120000
    elif cargo == "Desarrollador":
        descuento_de_salud = 50000
        descuento_de_afp = 90000
    elif cargo == "Analista de datos":
        descuento_de_salud = 60000
        descuento_de_afp = 100000
    else:
        descuento_de_salud = 0
        descuento_de_afp = 0
    
    liquido_a_pagar = sueldo_bruto - descuento_de_salud - descuento_de_afp
    return descuento_de_salud, descuento_de_afp, liquido_a_pagar

def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador = ")
    apellido = input("Ingrese el apellido del trabajador = ")
    
    print("Seleccione el cargo del trabajador:")
    for idx, cargo in enumerate(CARGOS, start=1):
        print(f"{idx}. {cargo}")
    
    cargo_idx = int(input("Ingrese el número del cargo =")) - 1
    cargo = CARGOS[cargo_idx]
    
    sueldo_bruto = int(input("Ingrese el sueldo bruto ="))
    
    descuento_de_salud, descuento_de_afp, liquido_a_pagar = calcular_liquido(sueldo_bruto, cargo)
    
    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "descuento de salud": descuento_de_salud,
        "descuento de afp": descuento_de_afp,
        "liquido_a_pagar": liquido_a_pagar
    }
    
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.\n")


def listar_trabajadores():
    if not trabajadores:
        print("No se encuentra trabajadores registrados.\n")
        return
    
    for trabajador in trabajadores:
        print(trabajador)

def imprimir_planilla():
    print("Seleccione una opción para imprimir: ")
    print("1. Imprimir a todos los trabajadores: ")
    print("2. Imprimir por cargo específico: ")
    
    opcion = int(input("Ingrese la opción == "))
    
    if opcion == 1:
        filename = "planilla_todos.txt"
        with open(filename, "a") as file:
            for trabajador in trabajadores:
                file.write(f"{trabajador['nombre']} {trabajador['apellido']}, Cargo = {trabajador['cargo']}, Sueldo Bruto = {trabajador['sueldo_bruto']}, Descuento de Salud = {trabajador['descuento_de_salud']}, Descuento de AFP = {trabajador['descuento_de_afp']}, Líquido a pagar = {trabajador['liquido_a_pagar']}\n")
        print(f"Planilla de todos los trabajadores impresa en {filename}\n")
    
    elif opcion == 2:
        print("Seleccione el cargo:")
        for idx, cargo in enumerate(CARGOS, start=1):
            print(f"{idx}. {cargo}")
        
        cargo_idx = int(input("Ingrese el número del cargo: ")) - 1
        cargo = CARGOS[cargo_idx]
        
        filename = f"planilla_{cargo.lower().replace(' ', '_')}.txt"
        with open(filename, "a") as file:
            for trabajador in trabajadores:
                if trabajador["cargo"] == cargo:
                    file.write(f"{trabajador['nombre']} {trabajador['apellido']}, Cargo = {trabajador['cargo']}, Sueldo Bruto = {trabajador['sueldo_bruto']}, Descuento de Salud =  {trabajador['descuento_de_salud']}, Descuento de AFP = {trabajador['descuento_de_afp']}, Líquido a pagar = {trabajador['liquido_a_pagar']}\n")
        print(f"Planilla de los trabajadores con cargo {cargo} impresa en {filename}\n")

def main():
    while True:
        print("Seleccione una opción:")
        print("1.==Registrar trabajador==")
        print("2.==Listar de todos los trabajadores==")
        print("3.==Imprimir planilla de los sueldos==")
        print("4.==Salir del programa==")
        
        opcion = int(input("Ingrese la opción = "))
        
        if opcion == 1:
            registrar_trabajador()
        elif opcion == 2:
            listar_trabajadores()
        elif opcion == 3:
            imprimir_planilla()
        elif opcion == 4:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.\n")

if "__main__":
    main()
