import datetime


liberado = True
nome = input(" Digite seu nome: ")

# Checando se o colaborador está a mais de 5 anos na empresa
hoje = datetime.datetime.now()
data = int(input(" Digite sua data de admissão: "))
if hoje.year - data < 5:
    print("Agradecemos seu interrese, mas você não atende aos requisitos mínimos do programa.")
else:
    # Checando o Salário e o Valor do Empréstimo para ver se o valor do empréstimo é maior que 2 vezes o salário
    salario = float(input(" Digite seu salário: "))
    valor_emprestimo = float(input(" Digite o valor do empréstimo: "))
    while valor_emprestimo > salario * 2:
        print("Insira um valor válido!")
        valor_emprestimo = float(input(" Digite o valor do empréstimo: "))
        
