import socket
host = 'localhost'
porta = 8000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))

pergunta = 1

while True:
    mensagem = cliente.recv(1024).decode()
    mensagem = mensagem.split(", ") 

    for i in range(len(mensagem)):
        print(mensagem[i])
    
    if (pergunta == 6):
        break

    pergunta += 1
    enviada = input("Digite a letra referente a sua resposta: ")
    cliente.send(enviada.encode())

print("O Quiz Acabou. Obrigado pela participação!")
cliente.close()