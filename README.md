
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
from speech import speech
import random, time

niveles = {
    "facil": ["agenda", "friend", "mouse"],
    "intermedio": ["computer", "algorithm", "developer"],
    "dificil": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    words = niveles.get(level, [])
    if not words:
        print("Nivel incorrecto")
        return
    score = 0
    num_intentos = 3
    for i in range(len(words)):
        random_word = random.choice(words)
        print(f"Por favor, pronuncie esta palabra: {random_word}")
        recog_word = speech()
        if recog_word == random_word:
            print("¡Es correcto!")
            score += 1
        else:
            print(f"Error, recuerda, la palabra era: {random_word}")
        time.sleep(2)
    print(f"¡El juego ha terminado! Tu puntuación es: {score}")

select_level = input("Seleccione un nivel: facil, intermedio o dificil: ").lower()
play_game(select_level)
```

### 4. **Ejecutar el Proyecto**



1. Selecciona el nivel de dificultad e intenta pronunciar correctamente las palabras que se te indiquen. ¡El juego calculará tu puntuación en función de cuántas palabras aciertes!

---

### Notas Finales

- Asegúrate de tener un micrófono correctamente configurado en tu sistema.
- Puedes mejorar el juego `bonus_game.py` añadiendo más palabras o niveles de dificultad.

---

