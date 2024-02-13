# Use a imagem oficial do Python
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o código-fonte do seu aplicativo para o contêiner
COPY . .

# Instala as dependências do seu aplicativo Python
RUN pip install --no-cache-dir psycopg2 requests

# Comando para executar o seu aplicativo
CMD ["python", "script.py"]
