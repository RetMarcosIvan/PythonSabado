def busqueda(tupla,cadena):
    retorno=[]
    for aux in tupla:
        if cadena in str(aux[0]):
            retorno.append(aux)
    return retorno


print busqueda([("Marcos",42937212),("Marcsoss",42937212),("Marcsoss",42937212),("Marcsoss",42937212),("Marcsoss",42937212)],"z")
