from Speech import speech
import random, time


niveles = {
    "facil": ["agenda", "friend", "mouse"],
    "intemedio": ["computer", "algorithm", "developer"],
    "dificil": ["neural network", "machine learning", "artificial intelligence"]
}


def  play_game(level):
    words = niveles.get(level, [])
    if not words:
        print("Nivel incorrecto")
        return
    score = 0
    num_intentos = 3
    for i in range(len(words)):
        random_word = random.choice(words)
        print(f"Por favor, pronuncie esta palabra {random_word}")
        recog_word = speech()
        if recog_word==random_word:
            print("Es correcto!")
            score+=1
        else:
            print(f"Eror, recuerda, la palabra es: {random_word}")
        time.sleep(2)
    print(f"El juego se terminó! su puntuación es: {score}")

select_level = input("Seleccione un nivel: facil, intermedio o dificil").lower()
play_game(select_level)