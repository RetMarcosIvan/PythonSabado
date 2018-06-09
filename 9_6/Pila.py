class Pila(object):
    __lista=[]

    def __init__(self):
        self.__lista=list()

    def push(self,agregar):
        self.__lista.append(agregar)        


    def pop(self):
        if(self.Tamanio==0):
            raise Exception("Error no se puede desapilar mas elementos")           
        return self.__lista.pop()

    def peek(self):
        if(self.Vacia):
             raise Exception("Error no se puede sacar mas elementos")
        return self.__lista[self.Tamanio -1]
    
    @property
    def Tamanio(self):
        tam=0
        for aux in self.__lista:
            tam+=1
        return tam
    @property
    def Vacia(self):
        return self.Tamanio==0

"""pila=Pila()
pila.push("Marcos")
pila.push("Ivan")
pila.push("Rey")
pila.push(19)

print pila.peek()

print pila.pop()
print pila.pop()
print pila.pop()
print pila.pop()"""




            

    




