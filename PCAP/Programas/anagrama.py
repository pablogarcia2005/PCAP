#anagrama.py

'''
Coprueba si dos textos son anagramas entre si (contienen las mismas letras).

EJEMPLOS DE ANAGRAMAS:
Roma-Amor
Taco-Acto
Embalsadero-Reembolsado

'''

while True:
    
    text1 = input("Introduce la 1ª palabra:")
    if not text1.isalpha():
        print("Error, la palabra no es una cadena alfabética")
        break
    else:
        text2 = input("Introduce la 2ª palabra:")
        if not text2.isalpha():
            print("Error, la palabra no es una cadena alfabética")
            break
        
    if sorted(text1) == sorted(text2):
        print("'"+text1+"' y '"+text2+"' son ANAGRAMAS." )
    else:
        print(" NO son ANAGRAMAS." )