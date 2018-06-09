#!/usr/bin/env python
import Cola
import Pila

cola=Cola.Cola()
cola.enqueue("Marcos")
cola.enqueue("Ivan")
cola.enqueue("Rey")
cola.enqueue(19)

print ""
print ""
print cola.peek()
print cola.dequeue()
print cola.dequeue()
print cola.dequeue()
print cola.dequeue()
print "------------------------"
print ""
print ""
pila=Pila.Pila()
pila.push("Marcos")
pila.push("Ivan")
pila.push("Rey")
pila.push(19)

print pila.peek()

print pila.pop()
print pila.pop()
print pila.pop()
print pila.pop()