'''
---Install Package----
pip install moviepy == 1.0.3
'''
import os
import moviepy.editor as mp

def extract_audio(video_path, filename):
    print("extract audio")
    audio_folder = os.path.join(os.getcwd(), "Python Helpful Program", "File")  # Full path to the folder
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    audio_filename = os.path.splitext(filename)[0] + '.wav'
    audio_path = os.path.join(audio_folder, audio_filename)
    
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

video_path = r"Python Helpful Program\File\Muniba Mazari Inspirational Words - Motivational Video - Incredible You.mp4"

filename = os.path.basename(video_path)
print("file name is: ", filename)
extract_audio(video_path, filename)
