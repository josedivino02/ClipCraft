from services.ffmpeg_service import run_ffmpeg
import os

def create_gif(input_video, crop_coords, output_gif, final_size="128:128"):
    x1, y1 = crop_coords[0]
    x2, y2 = crop_coords[1]
    crop_w = abs(x2 - x1)
    crop_h = abs(y2 - y1)
    crop_x = min(x1, x2)
    crop_y = min(y1, y2)

    cropped_video = "cam_crop_temp.mp4"
    run_ffmpeg([
        "ffmpeg", "-y", "-i", input_video,
        "-filter:v", f"crop={crop_w}:{crop_h}:{crop_x}:{crop_y}",
        cropped_video
    ])

    run_ffmpeg([
        "ffmpeg", "-y", "-i", cropped_video,
        "-vf", f"fps=15,scale={final_size}:flags=lanczos",
        "-gifflags", "-transdiff", output_gif
    ])

    if os.path.exists(cropped_video):
        os.remove(cropped_video)
