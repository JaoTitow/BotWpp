#Bibliotecas
from pathlib import Path
from time import sleep

import Funções 

#Main
if __name__ == '__main__':
    contatos = ['Meu numero:', 'Teste 1', 'Teste 2']
    caminho_catalogo = str(Path(__file__).parent.parent/'catalogo.pdf')
    mensagem = """
    Olá {}!

    Foi um prazer conhecê-lo.

    Envio um catálogo dos nossos produtos, para que você possa explorá-lo.

    Um abraço!
    """
    Funções.abrir_janela_whatsapp()
    
    
    for contato in contatos:
        Funções.abrindo_a_conversa(contato)
        sleep(1)
        Funções.enviando_mensagens(mensagem.format(contato))
        sleep(1)
        Funções.enviando_documentos(caminho_catalogo)
        sleep(1)
        Funções.fechando_a_conversa()
        sleep(1)
    
    sleep(200)