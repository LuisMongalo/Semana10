
def crear_nodo(dato):
    return {"dato": dato, "siguiente": None}


def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo["siguiente"] = cabeza
    return nuevo


def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)

    if cabeza is None:
        return nuevo

    actual = cabeza

    while actual["siguiente"] is not None:
        actual = actual["siguiente"]

    actual["siguiente"] = nuevo
    return cabeza


def mostrar(cabeza):
    actual = cabeza

    while actual is not None:
        print(actual["dato"], end=" → ")
        actual = actual["siguiente"]

    print("None")


def buscar(cabeza, dato):
    actual = cabeza
    posicion = 0

    while actual is not None:
        if actual["dato"] == dato:
            return posicion

        actual = actual["siguiente"]
        posicion += 1

    return -1


def eliminar(cabeza, dato):
    if cabeza is None:
        return None, False

    if cabeza["dato"] == dato:
        return cabeza["siguiente"], True

    anterior = cabeza
    actual = cabeza["siguiente"]

    while actual is not None:
        if actual["dato"] == dato:
            anterior["siguiente"] = actual["siguiente"]
            return cabeza, True

        anterior = actual
        actual = actual["siguiente"]

    return cabeza, False


def contar(cabeza):
    total = 0
    actual = cabeza

    while actual is not None:
        total += 1
        actual = actual["siguiente"]

    return total


# RETO 14.1: Atender el primer turno
def atender(cabeza):
    if cabeza is None:
        return None, None

    nombre = cabeza["dato"]
    nueva_cabeza = cabeza["siguiente"]

    return nueva_cabeza, nombre


# RETO 14.2: Insertar después de un nombre
def insertar_despues(cabeza, referencia, dato):
    actual = cabeza

    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)
            nuevo["siguiente"] = actual["siguiente"]
            actual["siguiente"] = nuevo
            return cabeza, True

        actual = actual["siguiente"]

    return cabeza, False


# RETO 14.3: Invertir los enlaces
def invertir(cabeza):
    anterior = None
    actual = cabeza

    while actual is not None:
        siguiente = actual["siguiente"]
        actual["siguiente"] = anterior
        anterior = actual
        actual = siguiente

    return anterior


def menu():
    cabeza = None

    while True:
        print("\n--- SISTEMA DE TURNOS ---")
        print("1. Agregar turno")
        print("2. Mostrar turnos")
        print("3. Buscar turno")
        print("4. Eliminar turno")
        print("5. Contar turnos")
        print("6. Atender primer turno")
        print("7. Insertar después de un nombre")
        print("8. Invertir lista")
        print("0. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            print("Programa finalizado.")
            break

        elif opcion == "1":
            nombre = input("Nombre: ").strip()

            if not nombre:
                print("Escriba un nombre.")
                continue

            cabeza = insertar_final(cabeza, nombre)
            print("Turno agregado.")

        elif opcion == "2":
            mostrar(cabeza)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()

            if not nombre:
                print("Escriba un nombre.")
                continue

            posicion = buscar(cabeza, nombre)

            if posicion == -1:
                print("No encontrado")
            else:
                print("Posición:", posicion)

        elif opcion == "4":
            nombre = input("Nombre a eliminar: ").strip()

            if not nombre:
                print("Escriba un nombre.")
                continue

            cabeza, eliminado = eliminar(cabeza, nombre)
            print("Eliminado" if eliminado else "No encontrado")

        elif opcion == "5":
            print("Total:", contar(cabeza))

        elif opcion == "6":
            cabeza, nombre = atender(cabeza)

            if nombre is None:
                print("No hay turnos pendientes.")
            else:
                print("Turno atendido:", nombre)

        elif opcion == "7":
            referencia = input("Insertar después de: ").strip()
            nombre = input("Nombre nuevo: ").strip()

            if not referencia or not nombre:
                print("Escriba ambos nombres.")
                continue

            cabeza, insertado = insertar_despues(
                cabeza, referencia, nombre
            )

            print(
                "Turno insertado."
                if insertado
                else "Nombre de referencia no encontrado."
            )

        elif opcion == "8":
            cabeza = invertir(cabeza)
            print("Lista invertida.")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
