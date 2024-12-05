import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Bienvenido Gael!")
    audio = r.listen(source)

try:
    print("Usted dijo " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Perdón señor no entendí lo que me dijo")
except sr.RequestError as e:
    print("Error fatal papu")
