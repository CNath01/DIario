
---

# Proyecto de Transcripción de Audio a Texto y Juego de Pronunciación

Este proyecto utiliza la biblioteca de **SpeechRecognition** para transcribir audio a texto. También incluye un juego de pronunciación en el que el usuario debe repetir palabras correctamente.

## Instrucciones Paso a Paso

### 1. **Crear un Entorno Virtual**

#### a) **Instalar pipenv**

Instala `pipenv` si no lo tienes instalado previamente:

```bash
pip install pipenv
```

#### b) **Crear y activar el entorno virtual**

En la terminal de Visual Studio Code o cualquier terminal, crea y activa el entorno virtual con los siguientes comandos:

```bash
pipenv shell
```

### 2. **Instalar las Dependencias Necesarias**

Dentro del entorno virtual, instala las bibliotecas necesarias:

```bash
pipenv install SpeechRecognition
```

Si estás trabajando con archivos de audio, puedes instalar también `PyAudio` para mejorar la captura de audio:

```bash
pipenv install PyAudio
```

> **Nota**: En algunos sistemas, la instalación de `PyAudio` puede requerir un instalador binario precompilado. Consulta la documentación oficial de PyAudio para más detalles.

### 3. **Crear los Archivos del Proyecto**

#### a) **Archivo `speech.py`**

Crea un archivo llamado `speech.py` y pega el siguiente código para la transcripción de audio a texto usando la biblioteca `SpeechRecognition`:

```python
import speech_recognition as speech_recog

#### V1 - función
def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-EN")
```

Esta función captura el audio del micrófono y lo transcribe utilizando el servicio de Google.

#### b) **Archivo `bonus_game.py`**

Crea un archivo adicional llamado `bonus_game.py`. Este archivo contiene un simple juego en el que los usuarios deben repetir palabras en inglés correctamente para ganar puntos:

```python
from Speech import speech
# Importa el módulo `speech` desde un archivo llamado `Speech`. Este módulo probablemente contiene una función que captura y transcribe la voz del usuario.

import random, time
# Importa las bibliotecas `random` y `time`. `random` se usa para seleccionar elementos aleatorios y `time` para manejar pausas temporales.

niveles = {
    "facil": ["agenda", "friend", "mouse"],
    "intemedio": ["computer", "algorithm", "developer"],
    "dificil": ["neural network", "machine learning", "artificial intelligence"]
}
# Crea un diccionario llamado `niveles` que organiza las palabras en tres niveles de dificultad: fácil, intermedio y difícil.

def play_game(level):
    # Define una función llamada `play_game` que toma un parámetro `level` (nivel de dificultad elegido por el usuario).

    words = niveles.get(level, [])
    # Busca en el diccionario `niveles` las palabras asociadas al nivel elegido. Si el nivel no existe, devuelve una lista vacía.

    if not words:
        print("Nivel incorrecto")
        return
    # Si no se encontraron palabras para el nivel, se imprime un mensaje y la función termina.

    score = 0
    # Inicializa el puntaje del jugador en 0.

    num_intentos = 3
    # Define que el jugador tendrá tres intentos para pronunciar palabras.

    for i in range(num_intentos):
        # Inicia un bucle que se repetirá tres veces (una por cada intento).

        random_word = random.choice(words)
        # Selecciona una palabra aleatoria de la lista correspondiente al nivel.

        print(f"Por favor, pronuncie esta palabra {random_word}")
        # Muestra en pantalla la palabra que el jugador debe pronunciar.

        recog_word = speech()
        # Llama a la función `speech()` para capturar y transcribir lo que el jugador pronuncia.

        if recog_word == random_word:
            # Compara la palabra transcrita (`recog_word`) con la palabra objetivo (`random_word`).

            print("Es correcto!")
            # Si coinciden, el jugador respondió correctamente.

            score += 1
            # Incrementa el puntaje del jugador en 1.

        else:
            # Si las palabras no coinciden:

            print(f"La palabra que dijo: {recog_word}")
            # Informa cuál fue la palabra pronunciada por el jugador.

            print(f"Error, recuerda, la palabra es: {random_word}")
            # Muestra un mensaje indicando la palabra correcta.

        time.sleep(2)
        # Pausa la ejecución durante 2 segundos antes del siguiente intento.

    print(f"El juego se terminó! su puntuación es: {score}")
    # Cuando el bucle termina, muestra el puntaje total del jugador.

select_level = input("Seleccione un nivel: facil, intermedio o dificil: ").lower()
# Solicita al jugador que elija un nivel de dificultad escribiendo su nombre. La entrada del usuario se convierte a minúsculas para facilitar la comparación.

play_game(select_level)
# Llama a la función `play_game` con el nivel seleccionado por el jugador.

```
## Resumen de funcionamiento
- El usuario elige un nivel de dificultad.
- El programa selecciona palabras del nivel correspondiente y las muestra al jugador para que las pronuncie.
- Utiliza el módulo speech para transcribir la voz del jugador.
- Compara la transcripción con la palabra original y calcula un puntaje basado en las coincidencias.
- Muestra el puntaje final al terminar los intentos.
  
### 4. **Ejecutar el Proyecto**



1. Selecciona el nivel de dificultad e intenta pronunciar correctamente las palabras que se te indiquen. ¡El juego calculará tu puntuación en función de cuántas palabras aciertes!

---

### Notas Finales

- Asegúrate de tener un micrófono correctamente configurado en tu sistema.
- Puedes mejorar el juego `bonus_game.py` añadiendo más palabras o niveles de dificultad.

---

