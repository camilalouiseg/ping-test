# Importa a biblioteca os
import os

# Imprime '#' 40 vezes e explica a função da aplicação
print('#' * 20 + '  Verificar PING  ' + '#' * 20)

# Variável que recebe o IP
ip_ou_host = input('Digite o IP ou host a ser verificado: ')

print('-' * 20 + '  Verificando...  ' + '-' * 20)

# Chama system da biblioteca os, comando ping enviando 6 pacotes
os.system('ping -n 6 {}'.format(ip_ou_host))

print('-' * 60)