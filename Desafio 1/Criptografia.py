from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import os

# Função para criar uma chave Fernet a partir de uma senha
def fernet(senha, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )
    chave = urlsafe_b64encode(kdf.derive(senha.encode()))
    return chave

# Função de criptografia
def criptografar_mensagem(message, chave):
    f = Fernet(chave)
    mensagem_criptografada = f.encrypt(message.encode())
    return mensagem_criptografada

# Função de descriptografia
def descriptografar_mensagem(mensagem_criptografada, chave):
    f = Fernet(chave)
    mensagem_descriptografada = f.decrypt(mensagem_criptografada)
    return mensagem_descriptografada.decode()

def salvar_salt(salt,name):
    with open(f"{name}.txt", "wb") as salt_file:
        salt_file.write(salt)

def carregar_salt(name):
    with open(f"{name}.txt", "rb") as salt_file:
        salt = salt_file.read()
    return salt

def gerar_salt(name):
    salt = os.urandom(16)  # É seguro usar um sal diferente cada vez
    salvar_salt(salt,name)
    return salt

def gen_all_salt():
    if os.path.exists("salt_1.txt"):
        salt_1 = carregar_salt("salt_1")
    else:
        salt_1 = gerar_salt("salt_1")

    if os.path.exists("salt_2.txt"):
        salt_2 = carregar_salt("salt_2")
    else:
        salt_2 = gerar_salt("salt_2")
        
    if os.path.exists("salt_3.txt"):
        salt_3 = carregar_salt("salt_3")
    else:
        salt_3 = gerar_salt("salt_3")
    return salt_1,salt_2,salt_3

# Gerar os três salts
salt_1,salt_2,salt_3 = gen_all_salt()

palavra_chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

# Gerar a chave a partir da senha e do sal
chave = fernet(palavra_chave, salt_1)

# Mensagem a ser criptografada
Senha_1 = "Me Contrata ModalGR"
Senha_2 = "ModalGR melhor empresa de tecnologia"
Senha_3 = "Melhor analista de dados da baixada santista"

# Criptografar a mensagem
criptografado = criptografar_mensagem(Senha_1, chave)
print(f"Mensagem criptografada: {criptografado}")

# Descriptografar a mensagem
descriptografado = descriptografar_mensagem(criptografado, chave)
print(f"Mensagem descriptografada: {descriptografado}")

# Gerar a chave a partir da senha e do sal
chave = fernet(palavra_chave, salt_2)

# Criptografar a mensagem
criptografado = criptografar_mensagem(Senha_2, chave)
print(f"Mensagem criptografada: {criptografado}")

# Descriptografar a mensagem
descriptografado = descriptografar_mensagem(criptografado, chave)
print(f"Mensagem descriptografada: {descriptografado}")

# Gerar a chave a partir da senha e do sal
chave = fernet(palavra_chave, salt_3)

# Criptografar a mensagem
criptografado = criptografar_mensagem(Senha_3, chave)
print(f"Mensagem criptografada: {criptografado}")

# Descriptografar a mensagem
descriptografado = descriptografar_mensagem(criptografado, chave)
print(f"Mensagem descriptografada: {descriptografado}")


