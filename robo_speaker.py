import pyttsx3 

def text_to_speech(text):
    a = pyttsx3.init()
    a.say(text)
    a.runAndWait()

text = input("Enter the text here")

    

text_to_speech(text)

while True:
    speech = input("Enter what you want to speech ")
    if __name__ == "__main__":
        b = pyttsx3.init()
        b.say(speech)
        b.runAndWait()
        if speech == "q":
       
            break

