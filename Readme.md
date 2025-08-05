# Video Editor CLI - Crop, GIF, Image, Audio

Ferramenta CLI para recortar vídeos, criar GIFs, extrair imagens e áudio de trechos de vídeos usando OpenCV e FFmpeg.

---

## Funcionalidades

- Seleção interativa de região do vídeo para crop (via mouse).
- Exportação como GIF, imagem, vídeo recortado ou áudio extraído.
- Uso de FFmpeg para manipulação eficiente do vídeo e áudio.
- Interface simples no terminal com prompts para entrada.

---

## Pré-requisitos

- Docker instalado (para rodar em container)  
  ou
- Python 3.8+
- FFmpeg instalado na máquina
- OpenCV para Python (`pip install opencv-python`)

---

## Rodando com Docker

### Build da imagem

```bash
docker build -t video-editor .
```

Rodando o container com Docker CLI

docker run -it --rm -v "$(pwd)":/app video-editor

Rodando com Docker Compose

docker-compose up

## Estrutura do Projeto

video_editor/
│
├── main.py
├── ui/
├── core/
├── services/
├── utils/
├── Dockerfile
├── docker-compose.yml
├── README.md

## Como Usar

- Execute o script (python main.py ou via Docker).
- Informe o caminho do vídeo.
- Use o mouse para selecionar a área para recorte.
- Escolha o tipo de saída (GIF, imagem, vídeo, áudio).
- Informe os tempos e nomes conforme solicitado.
- Aguarde a geração do arquivo.

Qualquer dúvida ou sugestão, só perguntar!
