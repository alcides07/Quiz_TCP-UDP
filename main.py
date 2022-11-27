import os
import subprocess

opcao = -1

print("")
while(opcao != 1 or opcao != 2):
    print("1 - TCP")
    print("2 - UDP")
    opcao = input("Digite a opção que deseja executar nosso quiz: ")
    print("")

    if (opcao == '1'):
        print("Executando com TCP\n")
        subprocess.Popen(['python3 ./TCP/servidor.py'], stdin = subprocess.PIPE, shell = True)
        i = 0
        while (i < 100000):
            i += 1
        if (i >= 100000):
            os.system('python3 ./TCP/cliente.py')
        break

    elif(opcao == '2'):
        print("Executando com UDP\n")
        subprocess.Popen(['python3 ./UDP/servidor.py'], stdin = subprocess.PIPE, shell = True)
        i = 0
        while (i < 100000):
            i += 1
        if (i >= 100000):
            os.system('python3 ./UDP/cliente.py')
        break