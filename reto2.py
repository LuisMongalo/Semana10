def insertar_despues(referencia, dato):
    global cola

    nodo = cabeza

    while nodo is not None:
        if nodo["dato"] == referencia:
            nuevo = {
                "dato": dato,
                "anterior": nodo,
                "siguiente": nodo["siguiente"]
            }

            if nodo["siguiente"] is not None:
                nodo["siguiente"]["anterior"] = nuevo
            else:
                cola = nuevo

            nodo["siguiente"] = nuevo
            return True

        nodo = nodo["siguiente"]

    return False