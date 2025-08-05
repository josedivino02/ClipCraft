# Usamos imagem oficial do Python com OpenCV já instalado
FROM python:3.11-slim

# Dependências de sistema para ffmpeg e opencv
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1-mesa-glx \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Definindo diretório de trabalho
WORKDIR /app

# Copiando o código para dentro do container
COPY . /app

# Instalando dependências Python
RUN pip install --no-cache-dir opencv-python imageio

# Comando padrão para rodar o script
ENTRYPOINT ["python", "main.py"]
