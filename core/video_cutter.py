from services.ffmpeg_service import run_ffmpeg

def cut_video(video_path, start_time, duration, output_name):
    run_ffmpeg([
        "ffmpeg", "-y",
        "-ss", str(start_time),
        "-i", video_path,
        "-t", str(duration),
        "-c", "copy",
        output_name
    ])

def cut_and_crop_video(video_path, start_time, duration, output_name, crop_coords):
    x1, y1 = crop_coords[0]
    x2, y2 = crop_coords[1]
    width = x2 - x1
    height = y2 - y1

    run_ffmpeg([
        "ffmpeg", "-y",
        "-ss", str(start_time),
        "-i", video_path,
        "-t", str(duration),
        "-filter:v", f"crop={width}:{height}:{x1}:{y1}",
        "-c:a", "copy",
        output_name
    ])
