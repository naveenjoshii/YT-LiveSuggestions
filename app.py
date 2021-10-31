from flask import Flask,render_template,request
from pytube import YouTube
import speech_recognition as sr
from moviepy.editor import *
from pydub import AudioSegment
import time
from textblob import TextBlob
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
import re
import wikipedia
import os
app = Flask(__name__)
# where to save
SAVE_PATH = "D:/Rohith-LiveSuggestions/temp/"
AUDIO_PATH = "D:/Rohith-LiveSuggestions/Audio/"
def extract_audio_from_video(video_full_path):
    video = VideoFileClip(video_full_path)
    audio = video.audio
    milliseconds = int(round(time.time() * 1000))
    path = AUDIO_PATH + str(milliseconds) +".wav"
    audio = audio.write_audiofile(path)
    return path

def convert_audio_to_text(path):
    query=""
    r = sr.Recognizer()
    fa = sr.AudioFile(path)
    with fa as source:
        at = r.record(source)
    try:
        query = r.recognize_google(at, language='en-in')
    except:
        pass
    return query


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        video_link = request.form['link']
        video_link = video_link.split("/")[-1]

        link="https://www.youtube.com/watch?v="+video_link

        try:
            yt = YouTube(link)
        except:
            print("Connection Error")

        for stream in yt.streams:
            if stream.mime_type == "video/mp4" and stream.resolution == "360p":
                print(stream)
                break
        try:
            milliseconds = int(round(time.time() * 1000))
            path = SAVE_PATH + str(milliseconds) + ".mp4"
            print("Downloading Video to process........")
            stream.download(filename=path)
        except:
            print("Some Error!")
        print('Video Download Completed : '+path)
        print('Extracting Audio...........')
        audio_path = extract_audio_from_video(path)
        print("Audio Extracted : "+audio_path)
        text = convert_audio_to_text(audio_path)
        blob = TextBlob(text)
        res = []
        s1 = list(set(blob.noun_phrases))

        s2 = list(set([w for (w, pos) in blob.pos_tags if pos[0] == 'N']))

        for s in s2:
            for i in s1:
                if s.lower() in i:
                    res.append(s2[s2.index(s)])

        final_out = s1+[i for i in s2 if i not in res]
        print("Extracted Nouns and Noun Phrases!")
        print(final_out)
        res_dict = {}
        # res_dict = {
        # "word1" :{
        #     "desc":"this is desc",
        #     "links": [1,2,3,4,5] } ,
        # "word2" :{
        #     "desc":"this is desc",
        #     "links": [1,2,3,4,5] }
        # }
        temp_dict = {}
        for i in  final_out:
            result = ""
            try:
                result = wikipedia.summary(search, sentences = 2)
            except:
                result = "No results found in wikipedia! "
            res_dict[i] = temp_dict
            temp_dict["desc"] = result
            page = requests.get(f"https://www.google.com/search?q={i}&num={20}")
            soup = BeautifulSoup(page.content, "html5lib")
            res = []
            links = soup.findAll("a")
            for link in links :
                link_href = link.get('href')
                if "url?q=" in link_href and not "webcache" in link_href:
                    val = link.get('href').split("?q=")[1].split("&sa=U")[0]
                    res.append(val)
            temp_dict["links"] = res[:5]
            temp_dict = {}
            print(res_dict)

    return render_template('home.html',video_link = video_link,words = final_out)













if __name__ == '__main__':
    app.run()
    app.debug = True
    app.run(debug=True)
    app.debug = True
