import psycopg2

try:
    cnx = psycopg2.connect(
        user="angra",
        password="Emanuell3",
        host="djangobd.postgres.database.azure.com",
        port=5432,
        database="postgres"
    )
    print("Conexão bem-sucedida")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
