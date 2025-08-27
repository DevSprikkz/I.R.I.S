import speech_recognition as sr
import pyttsx3

def falar(texto):
    """Converte texto em fala."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    texto_para_falar = texto.replace("I.R.I.S", "Íris")
    engine.say(texto_para_falar)
    engine.runAndWait()

def ouvir():
    """Ouve o microfone e retorna o texto reconhecido."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro no serviço de reconhecimento.")
        return ""
