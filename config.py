import os

# Pega o diretório onde este arquivo (config.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define o caminho do banco TRAVADO na raiz do projeto
# Assim, não importa de onde você rode o comando, ele sempre acha o arquivo certo.
DB_PATH = os.path.join(BASE_DIR, "database", "employees.db")