import datetime
from time import sleep
import os

def read_txt():
    arquivo = open('ExemploGrande.txt', 'r')
    lista = arquivo.readlines()
    arquivo.close()
    return lista

def filter(lista):
    mes_atual = datetime.date.today().month
    mes_atual_str = f'/{mes_atual:02d}/'
    lista_aniversariantes = []

    for funcionario in lista[1:]:  # Ignorando o cabeçalho da tabela
        partes = funcionario.strip().split("|")
        data_nascimento = partes[2]  # A terceira coluna contém a data de nascimento
        if  data_nascimento.find(mes_atual_str) != -1:
            lista_aniversariantes.append(funcionario)

    return lista_aniversariantes

def gen_txt(lista,mes_atual):
    arquivo = open(f'Aniversariantes_{mes_atual}.txt', 'w')
    arquivo.write('Nome Completo|E-mail|Data de Nascimento\n')
    arquivo.write(''.join(lista))
    arquivo.close()


# Definindo o mes passado como 0 para que a primeira vez que o programa rode ele gere o arquivo
mes_passado = 0
while True:
    mes_atual = datetime.date.today().month
    print(mes_atual)
    if mes_passado != mes_atual:
        # Apagando a ultima lista gerada
        if os.path.exists(f'Aniversariantes_{mes_passado}.txt'):
            os.remove(f'Aniversariantes_{mes_passado}.txt')
        mes_passado = mes_atual
        gen_txt(filter(read_txt()),mes_atual)


    sleep(24*60*60) # 1 dia