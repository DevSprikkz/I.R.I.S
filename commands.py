from datetime import datetime
from core import falar

def processar_comando(comando):
    """Processa o comando de voz e executa a ação correspondente."""
    if "olá" in comando or "oi" in comando:
        falar("Olá! Eu sou a I.R.I.S. Como posso ajudar?")
    elif "seu nome" in comando:
        falar("Meu nome é I.R.I.S, sua assistente virtual.")
    elif "que horas" in comando:
        agora = datetime.now().strftime("%H:%M")
        falar(f"Agora são {agora}")
    elif "sair" in comando or "tchau" in comando:
        falar("Até mais! Encerrando I.R.I.S.")
        return False  # Sinaliza para o loop principal terminar
    else:
        falar("Desculpe, ainda não sei fazer isso.")
    return True # Sinaliza para o loop principal continuar
