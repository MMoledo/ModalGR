# Sistema de Criptografia ModalGR

Este repositório contém um script em Python desenvolvido para criptografar senhas de forma segura para a ModalGR, utilizando uma chave secreta única e três métodos de criptografia distintos.

## Arquivos

- `Criptografia.py`: Script principal que executa as funções de criptografia e descriptografia.
- `requirements.txt`: Lista das bibliotecas necessárias para executar o script.

## Funcionalidades

O script `Criptografia.py` realiza as seguintes operações:

- **Geração de Salts**: Cria três arquivos distintos de 'salt' para uso na criptografia das senhas.
- **Criptografia**: Usa uma chave baseada na senha e no salt para criptografar três mensagens diferentes.
- **Descriptografia**: Capaz de descriptografar as mensagens usando a mesma chave.

### Detalhes das Funções

- `fernet(senha, salt)`: Gera uma chave segura para criptografia usando PBKDF2HMAC.
- `criptografar_mensagem(mensagem, chave)`: Criptografa a mensagem fornecida usando a chave gerada.
- `descriptografar_mensagem(mensagem_criptografada, chave)`: Descriptografa a mensagem fornecida usando a chave gerada.
- `salvar_salt(salt, name)`: Salva o salt gerado em um arquivo para uso posterior.
- `carregar_salt(name)`: Carrega o salt de um arquivo existente.
- `gerar_salt(name)`: Gera um novo salt aleatório e o salva em um arquivo.
- `gen_all_salt()`: Gera ou carrega os salts necessários para a criptografia.

## Como Usar

1. Certifique-se de que todas as dependências listadas em `requirements.txt` estão instaladas.
2. Execute o script `Criptografia.py` para gerar os salts e criptografar as senhas.
3. As senhas criptografadas serão exibidas na saída do console.
4. Para descriptografar uma mensagem, você precisará da chave e da mensagem criptografada.

## Testes

Recomenda-se realizar testes utilizando diferentes senhas e verificando a consistência das senhas criptografadas e descriptografadas.

## Observações

- Não inclua a chave secreta diretamente no script. Armazene-a de maneira segura e insira-a apenas quando necessário.
- O script está configurado para criar arquivos de salt se eles não existirem, garantindo que os salts não sejam perdidos entre as execuções.

## Dependências

Para instalar as dependências, execute o seguinte comando:

```
pip install -r requirements.txt
```

As bibliotecas necessárias incluem:
cryptography: Provedor dos algoritmos de criptografia utilizados.
os: Utilizado para gerar salts seguros e manipular arquivos no sistema.



