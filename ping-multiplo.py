# Importa bibliotecas
import os
import time

# Abre o arquivo no modo leitura e lê todas as linhas do arquivo
with open('./ping/hosts.txt') as file:
    
    # Obtem uma lista de strings, sendo cada linha uma string
    dump = file.readlines()

    # Itera sobre cada linha do arquivo
    for ip in dump:

        # Remove espaços em branco do início e do fim da linha
        ip = ip.strip()
        print('-' * 25 + ' Verificando o IP {} ... '.format(ip) + '-' * 25)
        # Executa o comando ping no IP atual, com 2 pacotes e aguarda 5 segundos entre cada execução
        os.system('ping -n 2 {}'.format(ip))
        # Aguarda 5 segundos antes de verificar o próximo IP
        time.sleep(5)