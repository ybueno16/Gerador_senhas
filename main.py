import string
from random import choice


n_senhas = int(input('Quantas senhas serão geradas?\n'))


for k in range(n_senhas):
    tamanho = int(input('Qual o tamanho de caracteres da senha?\n'))
    nome = str(input('Para que irá servir a senha?\n'))
    valores = string.ascii_letters+string.digits+string.punctuation
    senha = ''


    for i in range(tamanho):
        senha += choice(valores)
    print(senha)


    arquivo = open('senhas.txt','a')
    l_senhas = list()
    l_senhas.append(nome+':')
    l_senhas.append(senha)


    arquivo.writelines(nome+':')
    arquivo.writelines(senha)
    

    arquivo.write('\n')