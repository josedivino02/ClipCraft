from services.ffmpeg_service import run_ffmpeg
import cv2
import os

def create_image(video_path, crop_coords, frame_time, output_image):
    temp_frame = "frame_temp.png"
    run_ffmpeg([
        "ffmpeg", "-y",
        "-ss", str(frame_time),
        "-i", video_path,
        "-vframes", "1",
        temp_frame
    ])

    frame_img = cv2.imread(temp_frame)
    if frame_img is None:
        raise Exception("Erro ao carregar frame.")

    x1, y1 = crop_coords[0]
    x2, y2 = crop_coords[1]
    crop_x = min(x1, x2)
    crop_y = min(y1, y2)
    crop_w = abs(x2 - x1)
    crop_h = abs(y2 - y1)

    crop_frame = frame_img[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]

    cv2.imwrite(output_image, crop_frame)

    if os.path.exists(temp_frame):
        os.remove(temp_frame)
