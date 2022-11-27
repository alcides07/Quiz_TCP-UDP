pergunta_1 = "BEM-VINDO AO QUIZ DA TURMA DA MÔNICA!, \nPergunta - Qual é a cor do cachorro do cebolinha?, a) Azul, b) Rosa, c) Roxo, d) Verde, e) Laranja\n"

pergunta_2 = "\nPergunta - Qual é o nome do personagem caipira da Turma da Mônica?, a) Francisco José, b) Chico Bento, c) Bento Medeiros, d) Chaves Bento, e) Kleber Silva"

pergunta_3 = "\nPergunta - Qual a cor da roupa da Mônica?, a) Vermelho, b) Roxo, c) Laranja, d) Verde, e) Cinza"
    
pergunta_4 = "\nPergunta - Qual o nome do autor da Turma da Mônica?, a) Monteiro Lobato, b) Andrew Gorge, c) Tarsila do Amaral, d) Stan Lee, e) Maurício de Sousa"

pergunta_5 = "\nPergunta - Qual é o nome e a cor do coelho da Mônica?, a) Sansão (Azul), b) Floquinho (Verde), c) Bidu (Azul), d) Sansão (Laranja), e) Monicão (Azul)"

perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
gabaritos = ['d', 'b', 'a', 'e', 'a']

def acertou():
  if (pergunta == len(perguntas)):
    return (f"\nRESPOSTA CORRETA!, Pontuação Atual: {acertos}\n")
  else:
    return (f"\nRESPOSTA CORRETA!, Pontuação Atual: {acertos}, {perguntas[pergunta]}\n")

def errou():
  if (pergunta == len(perguntas)):
    return (f"\nRESPOSTA ERRADA!, Pontuação Atual: {acertos}\n")
  return (f"\nRESPOSTA ERRADA!, Pontuação Atual: {acertos}, {perguntas[pergunta]}\n")

import socket
host = 'localhost'
porta = 7000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((host, porta))

pergunta = 0
acertos = 0

def per():
  servidor.sendto(perguntas[pergunta].encode(), endereco)

mensagem, endereco = servidor.recvfrom(1024)

while(True):
    
    if (pergunta > len(perguntas) - 1):
       break
    if (pergunta == 0):
      per()

    mensagem, endereco = servidor.recvfrom(1024)
    mensagem = mensagem.decode()

    if (mensagem == gabaritos[pergunta]):
        acertos += 1
        pergunta += 1
        servidor.sendto(acertou().encode(), endereco)

    else:
        pergunta += 1
        servidor.sendto(errou().encode(), endereco)
      
servidor.close()