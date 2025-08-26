import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import subprocess

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

def abrir_programa(programa):
    try:
        usuario = os.getlogin()  # pega o usuário logado automaticamente
        if programa == "chrome":
            subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif programa == "vs code" or programa == "vscode":
            caminho_vscode = f"C:\\Users\\{usuario}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            subprocess.Popen(caminho_vscode)
        else:
            falar(f"Não sei como abrir {programa}.")
    except Exception as e:
        falar(f"Erro ao abrir {programa}: {e}")

def abrir_site(site):
    urls = {
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "google": "https://www.google.com"
    }
    url = urls.get(site)
    if url:
        webbrowser.open(url)
        falar(f"Abrindo {site}")
    else:
        falar(f"Não conheço o site {site}")

def processar_comando(comando):
    if "olá" in comando or "oi" in comando:
        falar("Olá! Eu sou a I.R.I.S. Como posso ajudar?")
    elif "seu nome" in comando:
        falar("Meu nome é I.R.I.S, sua assistente virtual.")
    elif "que horas" in comando:
        from datetime import datetime
        agora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "abrir" in comando:
        if "site" in comando or "youtube" in comando or "gmail" in comando:
            if "youtube" in comando:
                abrir_site("youtube")
            elif "gmail" in comando:
                abrir_site("gmail")
            elif "google" in comando:
                abrir_site("google")
            else:
                falar("Qual site você quer abrir?")
        else:
            if "chrome" in comando:
                abrir_programa("chrome")
            elif "vs code" in comando or "vscode" in comando:
                abrir_programa("vs code")
            else:
                falar("Qual programa você quer abrir?")
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
