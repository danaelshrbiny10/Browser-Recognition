import speech_recognition
import webbrowser as web

if __name__=="__main__":
    path="C:/Program Files/Mozilla Firefox/firefox.exe %s"
    

recognaizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Wait please ...!!")
    recognaizer.adjust_for_ambient_noise(source,duration=1)
    auduio2 = recognaizer.listen(source)
    print("Recoginizing now ...")
    
    try:
        destination = recognaizer.recognize_google(auduio2)
        print(destination)
        web.get(path).open(destination)

    except Exception:
        print(Exception)