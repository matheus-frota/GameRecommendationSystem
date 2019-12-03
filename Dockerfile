# Imagem padrão
FROM python:3.6-slim

# Identificacao
LABEL maintainer = "matheusfrota"

# Diretório de trabalho
WORKDIR /project

# Instalando requerimentos para execução do aplicativo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Executando aplicação
COPY ./gameRecommender ./
COPY ./data ./data
CMD ["python", "./main.py"]