# you can install av and speech_recognition by running the following commands in your terminal or command prompt:
# pip install av
# pip install SpeechRecognition


import os
import shutil
import speech_recognition as sr
import moviepy.editor as mp
import nltk
import re

# Download the punkt tokenizer if not already downloaded
nltk.download('punkt')

# Get the video file name from the user
video_file = input("Enter the name of the video file (with extension): ")

# Get the base file name (without extension)
base_name = os.path.splitext(video_file)[0]

# Extract the audio from the video and save it as a WAV file
clip = mp.VideoFileClip(video_file)
clip.audio.write_audiofile(f"{base_name}.wav")

# Perform speech recognition on the audio
r = sr.Recognizer()
with sr.AudioFile(f"{base_name}.wav") as source:
    audio = r.record(source)
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        text = ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        text = ""

# Write the output text to a file
text_file = f"{base_name}.txt"
with open(text_file, "w") as f:
    f.write(text)

# Read the text from the file
with open(text_file, "r") as f:
    text = f.read()

# Tokenize the text using NLTK
sentences = nltk.sent_tokenize(text)

# Write the tokenized sentences to a file
output_file = f"{base_name}_tokenized.txt"
with open(output_file, "w") as f:
    for sentence in sentences:
        # Add punctuation to the end of the sentence if it doesn't already have any
        if not re.search(r'[.?!]\s*$', sentence):
            sentence += '.'
        f.write(sentence + "\n")

print(f"Output written to {output_file}")
