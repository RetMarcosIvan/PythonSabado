def papaApata():	
	palabra="papa"
	lista=list(palabra)
	lista[2]="t"
	print "".join(lista)
	print palabra

def mostrarNombres(array1):
	return " ".join(array1)

def mostrarNumeros(array1=[i for i in range(100)]):
	return " ".join([str(e) for e in array1])

def par(array1=range(1000)):
	return " ".join([str(i) for i in array1 if i%5==0])

def saludar(mensajeSaludo,nombreCompleto):
	print	mensajeSaludo[0],nombreCompleto[0],mensajeSaludo[1]

def triplicar(nro=10):
	print nro*3



	

