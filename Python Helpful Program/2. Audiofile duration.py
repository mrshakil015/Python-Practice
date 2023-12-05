from moviepy.editor import AudioFileClip

audio = AudioFileClip("audio.mp3")
duration = audio.duration
print(f"Duration of the audio: {duration} seconds")