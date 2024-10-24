import openai
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import urllib.parse
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading  
from google.cloud import dialogflow_v2 as dialogflow

engine = pyttsx3.init()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jeevanassistant-be7df79e0996.json" 

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is", Time)

def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("The current date is")
    speak(f"{day} {month} {year}")
    print(f"The current date is {day}/{month}/{year}")

def wishme() -> None:
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("Jeevan at your service sir, please tell me how may I help you.")
    print("Jeevan at your service sir, please tell me how may I help you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)
    speak(f"Screenshot saved at {img_path}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        speak(query)  
        return query.lower()

    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Sorry, I didn't catch that. Please say that again.")
        return "Try Again"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, there was an error with the speech recognition service.")
        return "Try Again"
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I encountered an error.")
        return "Try Again"

def search_youtube(query):
    query_encoded = urllib.parse.quote(query)
    wb.open(f"https://www.youtube.com/results?search_query={query_encoded}")


def ask_google_dialogflow(query):
    session_client = dialogflow.SessionsClient()

    project_id = "jeevanassistant"  
    session_id = "unique-session-id"  
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=query, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        response_text = response.query_result.fulfillment_text
        print("Response from Dialogflow:", response_text)
        speak("Here is the response from Google Dialogflow.")
        return response_text
    except Exception as e:
        print(f"Error in Dialogflow response: {str(e)}")
        speak("There was an issue getting a response from Google Dialogflow.")
        return "Error in getting response."



def run_jeevan():
    wishme()
    while True:
        print("Waiting for a command...")  
        query = takecommand()
        print(query)
 

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "take screenshot" in query:
            screenshot()

        elif "who are you" in query:
            speak("I'm Jeevan created by Mr. Mugesh Kumar, and I'm a desktop voice assistant.")
            print("I'm Jeevan created by Mr. Mugesh Kumar, and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else.")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "search for" in query:  
            query = query.replace("search for", "").strip()
            if query:
                search_youtube(query)
                speak(f"Searching for {query} on YouTube.")
            else:
                speak("Please specify what you want to search for.")

        elif "open google" in query:
            wb.open("google.com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            try:
                songs = [f for f in os.listdir(song_dir) if f.endswith(('.mp3', '.wav', '.flac', '.m4a'))]  
                if songs:
                    random_song = random.choice(songs)
                    os.startfile(os.path.join(song_dir, random_song))
                    speak(f"Playing {random_song}.")
                else:
                    speak("No music files found in the music directory.")
            except Exception as e:
                speak("I encountered an error trying to play music.")
                print(f"Error: {e}")
        
        elif "play song" in query:
            wb.open("https://open.spotify.com")

        elif "ask gpt" in query:
            speak("What do you want to ask Dialogflow?")
            user_question = takecommand()
            if user_question != "Try Again":
                response = ask_google_dialogflow(user_question)
                speak(response)
            else:
                speak("I couldn't understand your question, please try again.")

        elif "stop" in query:
            speak("Goodbye Sir!")
            quit()

def play_gif():
    root = tk.Tk()
    root.title("Jeevan Voice Assistant")

    gif_path = os.path.join("GIF", "Jeevan.gif")
    img = Image.open(gif_path)
    
    frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(img)]
    label = tk.Label(root)
    label.pack()

    def update_frame(index):
        frame = frames[index]
        index = (index + 1) % len(frames)
        label.configure(image=frame)
        root.after(100, update_frame, index)

    root.after(0, update_frame, 0)
    root.mainloop()

if __name__ == "__main__":
    threading.Thread(target=play_gif).start()
    run_jeevan()  
