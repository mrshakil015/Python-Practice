from gtts import gTTS
import os

def text_to_audio(text, output_filename):
    tts = gTTS(text=text, lang='en')  # 'en' indicates English, change it for other languages
    tts.save(output_filename)

text = "I am able to convert any text into the audio file."
output_filename = "audio.mp3"
audio_folder = os.path.join(os.getcwd(), "Python Helpful Program", "File")
audio_path = os.path.join(audio_folder, output_filename)

text_to_audio(text, audio_path)
