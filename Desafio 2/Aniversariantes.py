import datetime

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

def gen_txt(lista):
    arquivo = open('Aniversariantes.txt', 'w')
    arquivo.write('Nome Completo|E-mail|Data de Nascimento\n')
    arquivo.write(''.join(lista))
    arquivo.close()

gen_txt(filter(read_txt()))
