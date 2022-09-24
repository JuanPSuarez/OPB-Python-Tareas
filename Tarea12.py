inputPaises = input("Ingrese nombre países separados por comas: ")


outputPaises = [i for i in inputPaises.split(",")]
print(",".join(sorted(list(set(outputPaises)))))