import os
import subprocess
import webbrowser
from datetime import datetime
from core import falar

def abrir_programa(programa):
    """Abre um programa local."""
    try:
        usuario = os.getlogin()  # pega o usuário logado automaticamente
        if programa == "chrome":
            subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            falar("Abrindo o Google Chrome.")
        elif programa == "vs code" or programa == "vscode":
            caminho_vscode = f"C:\\Users\\{usuario}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            subprocess.Popen(caminho_vscode)
            falar("Abrindo o Visual Studio Code.")
        else:
            falar(f"Não sei como abrir {programa}.")
    except Exception as e:
        falar(f"Erro ao abrir {programa}: {e}")

def abrir_site(site):
    """Abre um site no navegador padrão."""
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
    """Processa o comando de voz e executa a ação correspondente."""
    if "olá" in comando or "oi" in comando:
        falar("Olá! Eu sou a I.R.I.S. Como posso ajudar?")
    elif "seu nome" in comando:
        falar("Meu nome é I.R.I.S, sua assistente virtual.")
    elif "que horas" in comando:
        agora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "abrir" in comando:
        # Simplificando a lógica de "abrir"
        if "chrome" in comando:
            abrir_programa("chrome")
        elif "vs code" in comando or "vscode" in comando:
            abrir_programa("vs code")
        elif "youtube" in comando:
            abrir_site("youtube")
        elif "gmail" in comando:
            abrir_site("gmail")
        elif "google" in comando:
            abrir_site("google")
        else:
            falar("Não entendi o que você quer abrir. Por favor, seja mais específico.")
    elif "sair" in comando or "tchau" in comando:
        falar("Até mais! Encerrando I.R.I.S.")
        return False  # Sinaliza para o loop principal terminar
    else:
        falar("Desculpe, ainda não sei fazer isso.")
    return True # Sinaliza para o loop principal continuar
