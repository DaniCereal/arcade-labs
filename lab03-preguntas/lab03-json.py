import random
import json
pregunta = ""
respuestas = []
correcta = ""
puntuacion = 0
respuestaUsuario = ""

with open("lab03-preguntas/preguntas.json", 'r', encoding='utf8') as f:
    contenidoLineaJson = json.load(f)
    for line in contenidoLineaJson:
        respuestas = []
        pregunta = line["pregunta"]
        correcta = line["correcta"].upper()
        for respuesta in line["opciones"]:
            respuestas.append(respuesta)
    
        random.shuffle(respuestas)
        print(pregunta, "\n")
        for respuestaPosible in respuestas:
            print(respuestaPosible)
        while not (respuestas.__contains__(respuestaUsuario.capitalize())): 
            respuestaUsuario = input("\nInserta la respuesta correcta\n").capitalize()
            if respuestaUsuario.upper() == correcta:
                puntuacion += 1
            if not (respuestas.__contains__(respuestaUsuario.capitalize())): 
                print("La respuesta no es una opcion")

    print("Felicidades, tienes ", puntuacion, " puntos!")