def cambiarVocales(palabra):
    nueva_palabra = ""

    if not isinstance(palabra, str):
        raise TypeError

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