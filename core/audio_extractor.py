from services.ffmpeg_service import run_ffmpeg

def extract_audio(video_path, start_time, duration, output_audio):
    run_ffmpeg([
        "ffmpeg", "-y",
        "-ss", str(start_time),
        "-t", str(duration),
        "-i", video_path,
        "-q:a", "0",
        "-map", "a",
        output_audio
    ])
