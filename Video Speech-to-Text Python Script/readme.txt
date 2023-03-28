This script uses the Python library speech_recognition to convert the audio from a video file into text, which is then tokenized using nltk. The resulting tokenized text is saved to a file.

Dependencies
This script requires the following libraries to be installed:

speech_recognition
moviepy
nltk
To download the required NLTK data, the punkt tokenizer needs to be downloaded.

Usage
To use the script, simply run it from the command line and follow the prompts.

Enter the name of the video file (including extension) when prompted.
The audio from the video is extracted and saved as a WAV file.
Speech recognition is performed on the audio using Google's speech recognition service.
The resulting text is saved to a text file.
The text is tokenized using NLTK, and the resulting tokenized text is saved to a separate file.
The script outputs the filename of the tokenized text file to the console.

Note
Google's speech recognition service is used in this script, which requires an internet connection. If the service is unavailable, the script will not be able to perform speech recognition on the audio.