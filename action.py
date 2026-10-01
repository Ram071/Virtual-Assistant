import datetime
import os
import random
import webbrowser

import speak
import weather


def Action(send):
    """
    Process commands given to the virtual assistant.
    """

    if send is None:
        return None

    data_btn = send.lower().strip()

    # --------------------------------------------------
    # 1. WHAT IS YOUR NAME
    # --------------------------------------------------

    if "what is your name" in data_btn:
        response = "My name is Virtual Assistant."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 2. HELLO / HI / HYE / HAY / HEY
    # --------------------------------------------------

    elif (
        data_btn == "hello"
        or data_btn == "hi"
        or data_btn == "hye"
        or data_btn == "hay"
        or data_btn == "hey"
        or "hello" in data_btn
        or "hey" in data_btn
    ):
        response = random.choice([
            "Hello Rajaram. How can I help you?",
            "Hey Rajaram. How can I help you?",
            "Hi Rajaram. What can I do for you?"
        ])

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 3. HOW ARE YOU
    # --------------------------------------------------

    elif "how are you" in data_btn:

        response = "I am doing great these days, Rajaram."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 4. THANK YOU / THANKU / THANK
    # --------------------------------------------------

    elif (
        "thanku" in data_btn
        or "thank you" in data_btn
        or data_btn == "thank"
    ):

        response = "It's my pleasure, Rajaram."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 5. GOOD MORNING
    # --------------------------------------------------

    elif "good morning" in data_btn:

        response = "Good morning Rajaram. How can I help you?"

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 6. TIME NOW
    # --------------------------------------------------

    elif (
        "time now" in data_btn
        or "what is the time" in data_btn
        or "current time" in data_btn
    ):

        current_time = datetime.datetime.now()

        time = current_time.strftime("%I:%M %p")

        response = f"The current time is {time}."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 7. SHUTDOWN
    # --------------------------------------------------

    elif (
        "shutdown" in data_btn
        or "quit" in data_btn
    ):

        response = "ok sir"

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 8. PLAY MUSIC / SONG
    # --------------------------------------------------

    elif (
        "play music" in data_btn
        or "play song" in data_btn
        or data_btn == "song"
    ):

        webbrowser.open(
            "https://gaana.com/"
        )

        response = "Gaana is ready for you. Enjoy your music."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 9. OPEN GOOGLE / GOOGLE
    # --------------------------------------------------

    elif (
        data_btn == "google"
        or "open google" in data_btn
    ):

        webbrowser.open(
            "https://www.google.com/"
        )

        response = "Google is open."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 10. YOUTUBE / OPEN YOUTUBE
    # --------------------------------------------------

    elif (
        data_btn == "youtube"
        or "open youtube" in data_btn
    ):

        webbrowser.open(
            "https://www.youtube.com/"
        )

        response = "YouTube is open."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # 11. WEATHER
    # --------------------------------------------------

    elif "weather" in data_btn:

        try:
            answer = weather.Weather()

            speak.speak(answer)

            return answer

        except Exception as error:

            response = "Sorry Rajaram, I could not get the weather."

            print("Weather Error:", error)

            speak.speak(response)

            return response

    # --------------------------------------------------
    # 12. MUSIC FROM MY LAPTOP
    # --------------------------------------------------

    elif (
        "music from my laptop" in data_btn
        or "play music from my laptop" in data_btn
    ):

        music_folder = r"D:\music"

        if not os.path.exists(music_folder):

            response = "I could not find the music folder on your laptop."

            speak.speak(response)

            return response

        songs = [
            file
            for file in os.listdir(music_folder)
            if file.lower().endswith(
                (".mp3", ".wav", ".m4a", ".flac")
            )
        ]

        if not songs:

            response = "I could not find any songs in your music folder."

            speak.speak(response)

            return response

        song = random.choice(songs)

        song_path = os.path.join(
            music_folder,
            song
        )

        os.startfile(song_path)

        response = f"Playing {song}."

        speak.speak(response)

        return response

    # --------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------

    else:

        response = "Sorry Rajaram, I don't understand that command."

        speak.speak(response)

        return response
