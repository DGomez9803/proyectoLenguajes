#clase nodo que representa los estado de un automata
class Nodo:

    #contructor cdel nodo co valores y relaciones
    #@param relaciones es un diccionario con las relaciones de este nodo con otros nodos
    #@param valores son el diccionario con el valore o nombre del nodo, los fragmentos de la gramatica

    def __init__(self,valores,relaciones):
        self.valores=valores
        self.relaciones=relaciones
    def getValores(self):
        return self.valores

    def getRelaciones(self):
        return self.relaciones