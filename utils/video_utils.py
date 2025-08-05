from services.ffmpeg_service import get_video_duration

def validate_times(start_time, duration, video_duration):
    if start_time >= video_duration:
        raise ValueError("Tempo inicial é maior que a duração do vídeo.")
    if start_time + duration > video_duration:
        duration = video_duration - start_time
    return duration
