from faker import Faker
import mysql.connector

bancoDeDados = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

meuCursor = bancoDeDados.cursor()
quantidadeDePessoas = 150
counter = 0
while (counter <= quantidadeDePessoas):
    faker = Faker()

    nome = faker.first_name()
    nome = str(nome)
    email = faker.email()
    email = str(email)

    dados = (nome, email)
    query = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    meuCursor.execute(query, dados)
    bancoDeDados.commit()
    counter += 1
