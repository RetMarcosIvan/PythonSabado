continuar=True

while continuar:

    try:
        a = int(raw_input("Primer Numero: "))
        b = int(raw_input("Segundo Numero: "))
        print float(a) / b
    except ValueError as e:
        print "Solo ingrese numeros "
        continue
    except ZeroDivisionError as e:
        print "No se puede dividir un numero por 0"
        continue
    except Exception as e:
        print e
        continue
    else:
        letra = "a"
        while (letra != "s" and letra != "n"):

            letra = raw_input(("Continuar? (s/n) ")).lower()
        continuar = letra == "s"




