class Cola(object):

    def __init__(self):
        self.__lista=list()


    def enqueue(self,agregar):
        self.__lista.insert(0,agregar)       


    def dequeue(self):
        if(self.Tamanio==0):
            raise Exception("Error no se puede sacar mas elementos")

        return self.__lista.pop()

    def peek(self):
        if(self.Vacia):
             raise Exception("Error no se puede sacar mas elementos")
        return self.__lista[self.Tamanio - 1]

    @property
    def Tamanio(self):
        tam=0
        for aux in self.__lista:
            tam+=1
        return tam
    @property
    def Vacia(self):
        return self.Tamanio==0



"""cola=Cola()
cola.enqueue("Marcos")
cola.enqueue("Ivan")
cola.enqueue("Rey")
cola.enqueue(19)

print cola.peek()
print cola.dequeue()
print cola.dequeue()
print cola.dequeue()
print cola.dequeue()"""

