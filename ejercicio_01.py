def LeerDocumento()
    '''Esta función dará la ruta de acceso al fichero a leer

    Parámetros:
    leer el documento e indentificar los articulos pagados

    Salida:
    tendremos una lista con los datos del fichero

    '''
lista = int(input("Escribe lo que necesitas de la lista"))
LeerDocumento = open("PAGADO.txt", "r")

with open(LeerDocumento, 'r') as file:
    lista = file.readlines()
    if len(lista) >=
    print(f"Lista {}: {lista[ - 1]}")
else:
print(f"El articulo no esta en la lista .")
LeerDocumento()