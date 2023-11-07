# Programa de Empréstimo ModalGR

Este repositório contém um script em Python desenvolvido para facilitar a simulação de empréstimos para colaboradores da ModalGR que cumprem o requisito de tempo de casa superior a 5 anos.

## Arquivo

- `programa_emprestimo.py`: Script principal que executa todas as funções relacionadas à simulação de empréstimo.

## Funcionalidades

O script `programa_emprestimo.py` realiza as seguintes operações:

- **Verificação de elegibilidade**: Confirma se o colaborador está há mais de 5 anos na empresa.
- **Cálculo de empréstimo**: Permite a simulação de empréstimo de até duas vezes o valor do salário do colaborador, considerando que o valor solicitado seja múltiplo de 2.
- **Distribuição de cédulas**: Fornece ao colaborador opções para retirada do valor em cédulas de maior valor, menor valor ou uma combinação meio a meio.

### Detalhes das Funções

- `checa_data(data)`: Valida a data de admissão do colaborador e verifica se cumpre o critério de antiguidade.
- `maior_valor(emprestimo)`: Calcula a distribuição de cédulas começando pelas de maior valor.
- `menor_valor(emprestimo)`: Calcula a distribuição de cédulas começando pelas de menor valor.
- **Tratamento para cédulas de 1 real**: Devido à dificuldade de manejar valores que resultariam em 1 real, o script inclui uma condição adicional para considerar esta cédula.

## Como Usar

1. Inicie o script `programa_emprestimo.py`.
2. Forneça as informações solicitadas: nome do colaborador, data de admissão, salário atual e valor desejado para o empréstimo.
3. Escolha a opção de distribuição de cédulas para o empréstimo.
4. O script informará a distribuição das cédulas com base na opção selecionada.

## Testes

Para garantir a precisão e confiabilidade do programa, teste com diferentes cenários de entradas, variando as datas de admissão, valores de salário e quantias de empréstimo.

## Observações

- Caso o colaborador não atenda aos requisitos mínimos, será exibida uma mensagem informando a não elegibilidade.
- Se um valor de empréstimo inválido for inserido, o sistema solicitará a correção para prosseguir com a simulação.

## Dependências

- Python 3
- Módulo `datetime` para manipulação de datas (incluído na biblioteca padrão do Python).

---