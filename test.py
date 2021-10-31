from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from textblob import TextBlob
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
text = "hello internet people in this video I show you how to embed a YouTube video in HTML how to make a responsible for the wise in our view how you can easily adjust and better options such as out to play with a YouTube video on your site on the video Quicken share and select in bed now a popular appear within bed code and some extra parameters you can set there are actually much more options than what's this year but I'll show you how to get the extra was a bit later in this video just click on copy go to HTML code and paste the code you just copied you should see some CO2 with word iframe in it just say there is more good and now you can view the video on your website ok dude looks good on desktop but what about mobile less check it just right-click and select inspect and then here on the writers l i call mobile to speak on it ok doesn't look like the video is responsive by default it won't be and you need a bit of CSS to make a responsive no problem or just added Dev around iframe give the class name iframe dash and here is the CSS code the you need just make it easier for you to find it at the download in the description so now if we check the website mobile and even if we change the screen size the videos De sponsor and as a bonus tip if you want to know how to get different number of options like how to play to go to Google and search for YouTube embed generator from class in a message but essentially they are all the same here you will need to add video URL and you will be able to see all the different options that are YouTube video can have to speak the features you need and then copy the embed code into your HTML my name is Robert and if you're looking to master the digital world while getting into tane this is the channel for you so hit that subscribe button in the bell Icon so you get notified about new videos and here are videos you might like"
text = "have you ever lost your meals how often do you were your mouse to Pune Aundh to try and find you can tell it's there some of his place where I do over time special been working on of permanent fair is that anything is attractive finding it right away as simple as the secret just press the control key and related the trick is releasing the control key when you press the control and a girl with extra questions on your screen and gets smaller and smaller focusing on the cricket just listen to your mouth and child again if you do Rekha both times I remain in a memory that said I don't have to waste time trying to figure out where is fine motor factors does start.com"
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(text)
#
# filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#
# print(set(filtered_sentence))
res = []

blob = TextBlob(text)

s1 = list(set(blob.noun_phrases))

s2 = list(set([w for (w, pos) in blob.pos_tags if pos[0] == 'N']))

for s in s2:
    for i in s1:
        if s.lower() in i:
            res.append(s2[s2.index(s)])
final_out = s1+[i for i in s2 if i not in res]
print()
