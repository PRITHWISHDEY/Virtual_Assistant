import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
# acquiring all the voices

engine.setProperty("voice", voices[1].id)
# setting the voice to a female voice from all the voices


def greetings():

    engine.say("Hello user, you are welcome!")
    engine.runAndWait()
    engine.say("I am your assistant.....susan")
    engine.runAndWait()


def talk(text):
    # print(text)
    engine.say(text)
    engine.runAndWait()
    # print(text)


greetings()


def start_command():

    with sr.Microphone() as source:
        print("listening.....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "susan" in command:
            command = command.replace("susan", "")
            # print(command)

    return command


def actions():
    getcommand = start_command()
    print(getcommand)
   
    try:
        if "play" in getcommand:
            """
            playing a song from you tube
            
            """
            song = getcommand.index("play")
            find_song = getcommand[song+2:]
            talk("playing "+find_song)
            pywhatkit.playonyt(find_song)

        elif "time" in getcommand:
            """
            acquiring the current time
            
            """
            time = datetime.datetime.now().strftime("%H:%M %p")
            talk("The time currently is "+time)
            print("The time currently is "+time)

        elif "date" in getcommand:
            """
            getting a response for date
            """
            response = "I like dates.....I would think aout it"
            talk(response)
            print(response)

        elif "single" in getcommand:
            """
            getting a response to be asked if single
            """
            response = "No sir....I am in a relationship with wifi"
            talk(response)
            print(response)

        elif "joke" in getcommand:
            """
            getting a joke
            """
            jokes = pyjokes.get_joke()
            talk(jokes)
            print(jokes)

        elif "who is" or "what is" in getcommand:
            """
            finding about the term from wikipedia
            """
            find_about = getcommand.index("is")
            finding_about = getcommand[find_about+2:]
            talk("Searching the... wikipedia... for... "+finding_about)
            info = wikipedia.summary(finding_about, 3)
            talk("what we found out is "+info)
            print(info)
            
        else:
            """
            if the command is out of bounds (not from any of the conditions)
            """
            msg = "I don't understand.... can you please repeat it!"
            talk(msg)
            print(msg)

    except:
        raise Exception("There is some error in understanding the commands!")


while True:
    actions()
