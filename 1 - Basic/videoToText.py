import speech_recognition as sr 
import moviepy.editor as mp

#load the video
clip = mp.VideoFileClip(r"source.mp4")
#save only the audio from the video
clip.audio.write_audiofile(r"converted.wav")


# recognizer object 
r = sr.Recognizer()

#load the audio
cAudio = sr.AudioFile("converted.wav")

# open file and convert renerate the text to result 
with cAudio as source:
    audio_file = r.record(source)
    
result = r.recognize_google(audio_file)

# save to a text file 
with open('recognized.txt', mode='w') as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(result)
    print("File ready!")