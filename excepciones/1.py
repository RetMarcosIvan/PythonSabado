continuar=True

while continuar:

    try:
        a = float(raw_input("Primer Numero: "))
        b = float(raw_input("Segundo Numero: "))
        if(int(a)==a and int(b)==b):
            print int(a)/int(b)
        else:
            print a / b
    except ValueError as e:
        print "Solo ingrese numeros"
    except ZeroDivisionError as e:
        print "No se puede dividir un numero por 0"
    except Exception as e:
        print e
    else:
        letra = "a"
        while (letra != "s" and letra != "n"):

            letra = raw_input(("Continuar? (s/n) ")).lower()
        continuar = letra == "s"




