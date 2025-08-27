from core import falar, ouvir
from commands import processar_comando

def main():
    """Função principal que executa o loop da assistente."""
    falar("I.R.I.S iniciada. Diga 'sair' para encerrar.")
    ativo = True
    while ativo:
        comando = ouvir()
        if comando:
            ativo = processar_comando(comando)

if __name__ == "__main__":
    main()
