import socket
host = 'localhost'
porta = 7000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pergunta = 0

while(True):
    if(pergunta == 0):
        mensagem_cliente = input("Digite seu nome: ")
        cliente.sendto(mensagem_cliente.encode(), (host, porta))
    
    mensagem_servidor, endereco = cliente.recvfrom(1024)
    mensagem_servidor = mensagem_servidor.decode()
    mensagem_servidor = mensagem_servidor.split(", ") 

    for i in range(len(mensagem_servidor)):
        print(mensagem_servidor[i])

    if (pergunta == 5):
        break

    pergunta += 1
    
    cliente.sendto(input("Digite a letra referente a sua resposta: ").encode(), (host, porta))

print("O Quiz se encerra por aqui! Obrigado pela participação!")
cliente.close()