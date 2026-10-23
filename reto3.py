def visitar(dato):
    global cabeza, cola, actual

    nuevo = {
        "dato": dato,
        "anterior": actual,
        "siguiente": None
    }

    if actual is None:
        cabeza = nuevo
    else:
        actual["siguiente"] = None
        actual["siguiente"] = nuevo

    actual = nuevo
    cola = nuevo


def retroceder():
    global actual

    if actual is not None and actual["anterior"] is not None:
        actual = actual["anterior"]


def avanzar():
    global actual

    if actual is not None and actual["siguiente"] is not None:
        actual = actual["siguiente"]


def mostrar_actual():
    if actual is None:
        print("No hay ninguna página abierta")
    else:
        print("Página actual:", actual["dato"])