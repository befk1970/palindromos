def es_palindromo(palabra):
    i=0
    sigo=True
    while sigo and i < ((len(palabra)-1)/2):
        letra1 = palabra[i]
        letra2 = palabra[len(palabra)-1-i]
        if letra1 != letra2:
            sigo = False
        
        i+=1    
    return sigo