import speech_recognition as sr
import speak


def spech_to_text():
    """
    Listen to the microphone and convert speech into text.

    Returns:
        str: Recognized speech text.
        None: If speech could not be recognized or there is no internet.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")

            # Adjust microphone for background noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

        print("Recognizing...")

        voice_data = recognizer.recognize_google(audio)

        print(f"You said: {voice_data}")

        return voice_data

    except sr.UnknownValueError:
        speak.speak("Sorry, I could not understand what you said.")
        return None

    except sr.RequestError:
        speak.speak(
            "No internet connection. Please turn on your internet."
        )
        return None

    except OSError:
        speak.speak(
            "I could not access the microphone. "
            "Please check your microphone."
        )
        return None

    except Exception as error:
        print(f"Speech recognition error: {error}")
        speak.speak("Sorry, something went wrong with speech recognition.")
        return None


if __name__ == "__main__":
    result = spech_to_text()

    if result:
        print("Recognized Text:", result)
