# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para o container
COPY . .

# Expõe a porta 5000 (padrão do Flask)
EXPOSE 5000

# Comando para rodar a aplicação usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
