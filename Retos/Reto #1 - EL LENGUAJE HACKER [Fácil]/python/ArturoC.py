
# -Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# -Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  con el alfabeto y los números en "leet".
#  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")



def hacker_language(ref):

    try:
        hacker = ('4','13','[',')','3','|=','&','#','1',',_|','>|','1','/\/\ ','^/','0','|*','(_,)','12','5','7','(_)','\/','\/\/','><','j','2','L','R','E','A','S','b','T','B','g','o')
        abc = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0')

        lo = ref.lower()

        code = []

        for i in lo:

            if i in abc:
                code.append(hacker[abc.index(i)])
            elif i == ' ':
                code.append(' ')
            elif i == 'ñ':
                code.append(hacker[abc.index('n')])
            else:
                code.append('*')


    except Exception as e:
        print('An error typed as {} has ocurred, please try again'.format(type(e).__name__))
        
    else:
    	return ''.join(code) 



 

