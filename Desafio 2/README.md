# Gerenciador de Aniversariantes

Este repositório contém scripts em Python para identificar e gerenciar aniversariantes do mês a partir de uma lista de funcionários.

## Arquivos

- `Aniversariantes.py`: Script para gerar uma lista de aniversariantes do mês atual.
- `Aniversariantes_automatico.py`: Script para gerar automaticamente uma lista de aniversariantes do mês atual e atualizar a lista a cada mudança de mês.
- `ExemploGrande.txt`: Arquivo de texto com uma lista de funcionários maior do que o exemplo normal para teste dos scripts.

## Funcionalidades

### Aniversariantes.py

Este script executa as seguintes funções:

- `read_txt()`: Lê um arquivo de texto chamado 'ExemploGrande.txt' que contém dados dos funcionários.
- `filter(lista)`: Filtra os aniversariantes do mês atual da lista fornecida.
- `gen_txt(lista)`: Gera um novo arquivo de texto com os aniversariantes do mês.

### Aniversariantes_automatico.py

Este script é uma versão automatizada que executa continuamente para:

- Verificar a mudança de mês.
- Atualizar a lista de aniversariantes ao início de cada mês.
- Remover a lista do mês anterior.
- Executar uma pausa de 24 horas (um dia) entre as verificações.

## Como Usar

1. Garanta que o arquivo `ExemploGrande.txt` esteja no mesmo diretório que os scripts.
2. Execute o script `Aniversariantes.py` para gerar a lista de aniversariantes do mês atual manualmente.
3. Execute o script `Aniversariantes_automatico.py` se deseja que o processo seja feito automaticamente todo mês.

## Testes

O arquivo `ExemploGrande.txt` é uma lista ampliada baseada no seguinte formato de exemplo:
Nome Completo|E-mail|Data de Nascimento
João Silva|joao.silva@email.com|15/02/1990
Maria Santos|maria.santos@email.com|03/06/1985
Carlos Pereira|carlos.pereira@email.com|20/11/1995
Ana Souza|ana.souza@email.com|10/04/1992
Pedro Oliveira|pedro.oliveira@email.com|28/09/1988


Certifique-se de substituir o conteúdo do `ExemploGrande.txt` com dados reais para testar em um cenário de produção.

## Dependências

- Python 3
- Módulo `datetime` para manipulação de datas (incluído na biblioteca padrão do Python).
- Módulo `os` para manipulação de arquivos e diretórios (incluído na biblioteca padrão do Python).
- Módulo `time` para as pausas entre as execuções do script automático (incluído na biblioteca padrão do Python).

---

