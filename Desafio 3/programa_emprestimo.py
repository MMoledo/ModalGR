import datetime


def checa_data(data):
    data_formato = "%d/%m/%Y"  # Define o formato da data
    hoje = datetime.datetime.now()
    # Converte a string para um objeto datetime
    try:
        data_objeto = datetime.datetime.strptime(data, data_formato)
    except ValueError:
        print("A data informada não está no formato esperado ou é inválida.")
        return False
    if hoje.year - data_objeto.year < 5:
        return False
    else:
        return True


def maior_valor(emprestimo):
    notas = [100, 50, 20, 10, 5, 2]
    for nota in notas:
        if emprestimo >= nota:
            print(f"{emprestimo//nota} x {nota} reais")
            emprestimo = emprestimo % nota
    if emprestimo == 1:
        print("1 x 1 real")


def menor_valor(emprestimo):
    notas = [20, 10, 5, 2]
    for nota in notas:
        if emprestimo >= nota:
            print(f"{emprestimo//nota} x {nota} reais")
            emprestimo = emprestimo % nota
    if emprestimo == 1:
        print("1 x 1 real")


# Pedindo o nome do colaborador
nome = input("Digite seu nome: ")
# Checando se o colaborador está a mais de 5 anos na empresa
data = input("Digite sua data de admissão (dd/mm/aaaa): ")
if checa_data(data):
    # Checando o Salário e o Valor do Empréstimo para ver se o valor do empréstimo é maior que 2 vezes o salário
    salario = int(input("Digite seu salário: "))
    valor_emprestimo = int(input("Digite o valor do empréstimo (o valor não pode ser maior que duas vezes o valor do salário e tem que ser múltiplo de 2): "))

    while valor_emprestimo > salario * 2 or valor_emprestimo % 2 != 0:
        print("Insira um valor válido!")
        valor_emprestimo = int(input("Digite o valor do empréstimo: "))

    print("Simular empréstimo")
    print("1 - Notas de maior valor")
    print("2 - Notas de menor valor")
    print("3 - Notas meio a meio")
    
    escolha = int(input("Digite a opção desejada: "))
    while escolha > 3 or escolha < 1:
        print("Opção inválida!")
        escolha = input("Digite a opção desejada: ")
    if escolha == 1:
        maior_valor(valor_emprestimo)
    elif escolha == 2:
        menor_valor(valor_emprestimo)
    else:
        maior_valor(valor_emprestimo//2)
        menor_valor(valor_emprestimo//2)
else:
    print("Agradecemos seu interrese, mas você não atende aos requisitos mínimos do programa.")
