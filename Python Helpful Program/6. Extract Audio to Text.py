'''
---Install Package----
pip install SpeechRecognition==3.10.0
pip install moviepy == 1.0.3
'''

import os
import moviepy.editor as mp
import speech_recognition as sr

def extract_audio(video_path, filename):
    print("Extracting audio...")
    audio_folder = os.path.join(os.getcwd(), "Python Helpful Program", "File")  # Full path to the folder
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    audio_filename = os.path.splitext(filename)[0] + '.wav'
    audio_path = os.path.join(audio_folder, audio_filename)
    
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    
    return audio_path

def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Could not request results; check your internet connection"

video_path = r"Python Helpful Program\File\Muniba Mazari Inspirational Words - Motivational Video - Incredible You.mp4"
filename = os.path.basename(video_path)
print("File name is: ", filename)

audio_path = extract_audio(video_path, filename)
transcribed_text = audio_to_text(audio_path)
print("Transcribed text:\n", transcribed_text)
