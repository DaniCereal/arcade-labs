import random

pregunta = ""
respuestas = []
correcta = ""
puntuacion = 0
respuestaUsuario = ""

with open("lab03-preguntas/preguntas.txt", 'r', encoding='utf8') as f:
    for line in f:
        respuestas = []
        lineaDividida = line.split("|")
        pregunta = lineaDividida[0]
        correcta = lineaDividida[1].upper()
        for respuesta in lineaDividida[1:-1]:
            respuestas.append(respuesta)
    
        random.shuffle(respuestas)
        print(pregunta, "\n")
        for respuestaPosible in respuestas:
            print(respuestaPosible)
        while not (respuestas.__contains__(respuestaUsuario.capitalize())): 
            respuestaUsuario = input("\nInserta la respuesta correcta\n").capitalize()
            if respuestaUsuario.upper() == correcta:
                puntuacion += 5
            if not (respuestas.__contains__(respuestaUsuario.capitalize())): 
                print("La respuesta no es una opcion")

    print("Felicidades, tienes ", puntuacion, " puntos!")
