def contarVocales(palabra):
    cantidad_vocales = 0

    if not isinstance(palabra, str):
        raise TypeError

    for letra in palabra:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            cantidad_vocales += 1
    
    return cantidad_vocales