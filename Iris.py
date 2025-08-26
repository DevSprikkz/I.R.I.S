# I.R.I.S - Intelligent Rational Interface System
import speech_recognition as sr
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    texto_para_falar = texto.replace("I.R.I.S", "Íris")
    engine.say(texto_para_falar)
    engine.runAndWait()

def ouvir():
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

def processar_comando(comando):
    if "olá" in comando or "oi" in comando:
        falar("Olá! Eu sou a I.R.I.S. Como posso ajudar?")
    elif "seu nome" in comando:
        falar("Meu nome é I.R.I.S, sua assistente virtual.")
    elif "que horas" in comando:
        from datetime import datetime
        agora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "sair" in comando or "tchau" in comando:
        falar("Até mais! Encerrando I.R.I.S.")
        return False
    else:
        falar("Desculpe, ainda não sei fazer isso.")
    return True

falar("I.R.I.S iniciada. Diga 'sair' para encerrar.")
ativo = True
while ativo:
    comando = ouvir()
    if comando:
        ativo = processar_comando(comando)
