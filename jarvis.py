import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices' ,voices[0].id)
Assistant.setProperty('rate' ,170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()
    
    
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........") 
        command.pause_threshold = 1
        audio = command.listen(source)
        
        
        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")
            
        except Exception as Error:
            return "none"
        
        return query.lower()
    
def TaskExe():
    
    while True:
        
        query = takecommand()
        
        if 'hello' in query:
            Speak("Hello Arpit , I Am Gojo Saturo")
            Speak("You Personal Ai Assistat")
            Speak("How May I help You?")
            
        elif 'How are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats Aout You?")
            
        elif 'You need a break' in query:
            Speak("Ok Sir, You Can call me anytime !")
            break
        
        elif 'kya haal hai' in query:
            Speak("Main Badiya hun Aap Btao!")
            
        elif 'bye' in query:
            Speak("Ok Sir , Bye!")
            break
        
        elif 'main achcha hoon' in query:
            Speak("main bhi")

TaskExe()