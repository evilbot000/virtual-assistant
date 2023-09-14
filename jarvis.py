import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
        print("Recognizing...")
        instruction = listener.recognize_google(audio)
        instruction = instruction.lower()
        if "jarvis" in instruction:
            instruction = instruction.replace('jarvis', '')
            print(instruction)
        return instruction
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""


    
    try:
        weather = owm.get_weather(city, units="metric")
        temperature = weather["temperature"]["temp"]
        description = weather["description"]
        humidity = weather["humidity"]
        
        return f"Current weather in {city}: Temperature: {temperature}°C, Description: {description}, Humidity: {humidity}%"
    except Exception as e:
        return f"Unable to get weather information for {city}"

def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.split('play', 1)[1].strip()
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date is " + date)
    elif 'how are you' in instruction:
        talk('I am Jarvis. What can I do for you?')
    elif 'What is your name' in instruction:
        talk('I am Jarvis. What can I do for you today?')
    elif 'who is' in instruction:
        human = instruction.replace('who is', "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk('Please repeat again')

play_Jarvis()
