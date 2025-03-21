class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaCircularDoble:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = NodoCircular(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            ultimo = self.cabeza.anterior
            ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = ultimo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo

    def eliminar(self, dato):
        if not self.cabeza:
            print("Lista vacía")
            return
        actual = self.cabeza
        while True:
            if actual.dato == dato:
                if actual.siguiente == actual:  # Único nodo
                    self.cabeza = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    if actual == self.cabeza:
                        self.cabeza = actual.siguiente
                return
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("Dato no encontrado")

    def mostrar(self):
        if not self.cabeza:
            print("Lista vacía")
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(cabeza)")