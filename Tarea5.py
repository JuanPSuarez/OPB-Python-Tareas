def añobisiesto(añoInput):
    
    if(añoInput % 4 == 0 and (añoInput % 100 != 0 or añoInput % 400 == 0)):
        print("El año", añoInput, "es bisiesto.")

    else:
        print("El año", añoInput, "no es bisiesto.")

a = int(input("Ingrese un año, el programa deducira si es bisiesto:  "))

añobisiesto(a)