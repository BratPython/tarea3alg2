class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_despues_de(self, nodo_objetivo, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == nodo_objetivo:
                nuevo_nodo = Nodo(dato)
                nuevo_nodo.anterior = actual
                nuevo_nodo.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = nuevo_nodo
                else:
                    self.cola = nuevo_nodo
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print("Nodo objetivo no encontrado")

    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente
        print("Dato no encontrado")

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")