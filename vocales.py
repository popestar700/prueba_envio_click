def contarVocales(palabra):
    cantidad_vocales = 0

    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            cantidad_vocales += 1

    print("La cantidad de vocales es: {0}".format(cantidad_vocales))
    print("La palabra/parrafo ingresado(a) es: {0}".format(palabra))
    print("La nueva palabra/parrafo con diferentes vocales es: {0}".format(nuevaPalabra(palabra)))

def nuevaPalabra(palabra):
    nueva_palabra = ""

    for letra in palabra:
        if letra == 'a':
            nueva_palabra += "e"

        elif letra == 'e':
            nueva_palabra += 'i'
        
        elif letra == 'i':
            nueva_palabra += 'o'
        
        elif letra == 'o':
            nueva_palabra += 'u'
        
        elif letra == 'u':
            nueva_palabra += 'a'

        else:
            nueva_palabra += letra

    return nueva_palabra

contarVocales("un nuevo parrafo")