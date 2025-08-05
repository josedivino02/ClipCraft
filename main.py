import os
import sys
import cv2

from ui.user_input import (
    ask_video_path, ask_output_type, ask_gif_size,
    ask_file_name, ask_time
)
from services.ffmpeg_service import get_video_duration
from core.crop_selector import select_crop_region
from core.gif_creator import create_gif
from core.image_creator import create_image
from core.video_cutter import cut_video, cut_and_crop_video
from core.audio_extractor import extract_audio
from utils.video_utils import validate_times
from utils.file_utils import file_exists, remove_file, ensure_output_folder

def main():
    cut_video_temp = None
    
    video_path = ask_video_path()
    if not file_exists(video_path):
        print("❌ Arquivo não encontrado.")
        return

    video_duration = get_video_duration(video_path)
    if video_duration is None:
        print("❌ Não foi possível obter a duração do vídeo.")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Não foi possível abrir o vídeo.")
        return

    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("❌ Não foi possível ler o primeiro frame.")
        return

    crop_coords = select_crop_region(frame)
    if crop_coords is None:
        print("🚫 Operação cancelada pelo usuário.")
        return

    print(f"📐 Região selecionada: {crop_coords}")

    output_type = ask_output_type()

    if output_type in ("1", "3", "4"):
        start_time = ask_time("⏱️ Tempo inicial do corte (em segundos): ")
        duration = ask_time("⏱️ Duração do corte (em segundos): ")
        try:
            duration = validate_times(start_time, duration, video_duration)
        except ValueError as e:
            print(f"❌ {e}")
            return

        cut_video_temp = "recorte_temp.mp4"
        cut_video(video_path, start_time, duration, cut_video_temp)

        if output_type == "1":
            final_size = ask_gif_size()
            gif_name = ask_file_name("💾 Nome do GIF (ex: emote.gif): ", ".gif")
            gif_path = os.path.join("output", gif_name)
            create_gif(cut_video_temp, crop_coords, gif_path, final_size)
            print(f"✅ GIF criado: {gif_name}")

        elif output_type == "3":
            output_name = ask_file_name("🎬 Nome do clipe de vídeo (ex: clipe.mp4): ", ".mp4")
            output_path = os.path.join("output", output_name)
            cut_and_crop_video(video_path, start_time, duration, output_path, crop_coords)
            print(f"✅ Clipe de vídeo criado: {output_name}")

        elif output_type == "4":
            output_name = ask_file_name("🔊 Nome do áudio (ex: audio.mp3): ", ".mp3")
            output_path = os.path.join("output", output_name)
            extract_audio(cut_video_temp, 0, duration, output_path)
            print(f"✅ Áudio criado: {output_name}")

        if cut_video_temp and file_exists(cut_video_temp):
            remove_file(cut_video_temp)
            print("🧹 Arquivo temporário removido.")

    elif output_type == "2":
        frame_time = ask_time("🕒 Tempo do frame para imagem (em segundos): ")
        if frame_time > video_duration:
            frame_time = max(0, video_duration - 0.1)
        image_name = ask_file_name("🖼️ Nome da imagem (ex: emote.png): ", ".png")
        image_path = os.path.join("output", image_name)
        try:
            create_image(video_path, crop_coords, frame_time, image_path)
            print(f"✅ Imagem criada: {image_name}")
        except Exception as e:
            print(f"❌ Erro: {e}")

    else:
        print("❌ Opção inválida.")

    if cut_video_temp and file_exists(cut_video_temp):
        remove_file(cut_video_temp)
        print("🧹 Arquivo temporário removido.")

if __name__ == "__main__":
    main()
    ensure_output_folder()
