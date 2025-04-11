Z = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "MAE": " Forma de llamar a una persona",
            "TUANIS": "Cool u otra forma de decir bien",
            }
while True:
    print("Hola")
    X = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if X in Z.keys():
        print(Z[X])
        print('---------------------')
    
    # ¿Qué debemos hacer si se encuentra la palabra?
    else:
        print("Nose")
        print('---------------------')
    # ¿Qué hacer si no se encuentra la palabra?
