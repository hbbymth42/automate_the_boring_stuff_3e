import yt_dlp, whisper, os

model = whisper.load_model('base')

dl_video_list = ['[YT links here]']

audio_options = {
    'quiet': True,  # Suppress the output.
    'no_warnings': True,  # Suppress warnings.
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{# Extract audio using ffmpeg.
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'm4a',
                        }]
}

video_options = {
    'quiet': True,  # Suppress the output.
    'no_warnings': True,  # Suppress warnings.
    'format': 'mp4/bestaudio/best'
}

for video in dl_video_list:
    with yt_dlp.YoutubeDL(audio_options) as ydl:
        ydl.download([video])

        info = ydl.extract_info(video)
        json_info = ydl.sanitize_info(info)

        result = model.transcribe(f'{json_info["title"]} [{json_info["id"]}].m4a')
        write_function = whisper.utils.get_writer('srt', '.')
        write_function(result, f'{json_info["title"]} [{json_info["id"]}]')

        os.remove(f'{json_info["title"]} [{json_info["id"]}].m4a')

    with yt_dlp.YoutubeDL(video_options) as ydl:
        ydl.download([video])
