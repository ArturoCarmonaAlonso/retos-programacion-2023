import random

def password():


    modulos = {1:'abcdefghyjclmnñopqrstuvwxyz',2:'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',3:'123456789'}
    ASCII = (32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126)

    # Convierto a simbolos el codigo ASCII
    simbolos = []
    for i in ASCII:
        simbolos.append(chr(i))
  

    # Declaracion de variables
    modulos[4]=simbolos
    longitud = random.randrange(8,17)


    ## Por defecto, incluyo aleatoriamente letras minusculas
    final = []
    maximo = random.randrange(8,17)
    cantidad = random.randrange(0,maximo)
    maximo = maximo - cantidad
    
    for i in range(cantidad):
        final.append(random.sample(modulos[1],1))
    

    # Resto de digitos
    while maximo>0:

            modulo_elegido = random.randrange(2,5)

            if modulo_elegido == 2 and maximo>0:  # Letras Mayusculas
                cantidad = random.randrange(1,maximo+1)
                maximo = maximo-cantidad
                for i in range(cantidad):
                    final.append(random.sample(modulos[2],1))

            elif modulo_elegido == 3 and maximo>0:  # Numeros
                cantidad = random.randrange(1,maximo+1)
                maximo = maximo - cantidad
                for i in range(cantidad): 
                    final.append(random.sample(modulos[3],1))

            elif modulo_elegido == 4 and maximo>0:  # Simbolos
                cantidad = random.randrange(1,maximo+1)
                maximo = maximo - cantidad
                for i in range(cantidad): 
                    final.append(random.sample(modulos[4],1))

    random.shuffle(final)  


    flat_list = [item for sublist in final for item in sublist]  # Reorganizo las sublistas en una unica lista de caracteres
    
    return "".join(flat_list)   # Extraigo los caracteres a una cadena desde la lista

print(password())
