from Die import Die
from Oracle import Oracle
#from ImprovedOracle import ImprovedOracle
#from Oracle import AlternateOracle

richiesta_utente = input("""Benvenuto nel software per giocare a solo D&D. Cosa vuoi fare? Scegli tra 
                         1. Lancia un dado
                         2. Consulta Oracolo
                         """)
match richiesta_utente:
    case 1:
        numero_tipo = input("Quanti e che tipo di dadi vuoi lanciare? Usa es 1d20 o 2d6: ")
        numero_tipo = list(map(lambda a : int(a), richiesta_utente.split("d")))

        dado = Die(numero_tipo[0], numero_tipo[1])

        print("Hai scelto: ", dado)
        print("Risultato: ", dado.throw())
    case 2:

        tipo_oracolo = int(input("""Che tipo di Oracolo vuoi consultare? Scegli tra
              1. Semplice
              2. Migliorato
              3. Alternativo"""))
        
        match tipo_oracolo:
            case 1:
                oracolo_semplificato = Oracle()
                print("Oracolo semplificato: ", oracolo_semplificato.consult())
            case 2:
                oracolo = ImprovedOracle()
                print("Oracolo migliorato: ", oracolo.consult())
            case 3:
                oracolo = AlternateOracle()
                print("Oracolo alternativo: ", oracolo.consult())