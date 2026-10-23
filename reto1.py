def buscar(dato):
    nodo = cabeza

    while nodo is not None:
        if nodo["dato"] == dato:
            return True
        nodo = nodo["siguiente"]

    nodo = cola

    while nodo is not None:
        if nodo["dato"] == dato:
            return True
        nodo = nodo["anterior"]

    return False