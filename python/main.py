from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL()

banco.connect()

aluno = Aluno(
    "José Maria",
    "jose.maria@gmsil.com",
    "98765432110",
    "0319444455555",
    "Rua Paineiras, Eldorado, 3000"
    
)

query = aluno.cadastrar()

# print(query)

banco.execute_query(query)

banco.disconnect()