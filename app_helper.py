import datetime 
import fasttext
import nltk
import numpy as np 
import random 

from pycountry import languages
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from preprocess import words, labels, data
from neural_network import model 

def bag_of_words(s, words):

    bag = [0 for x in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for x in s_words:
        for i, w in enumerate(words):
            if w == x:
                bag[i] = 1
            
    return np.array(bag)

def chat(my_input):

    results = model.predict([bag_of_words(my_input, words)])
    results_index = np.argmax(results)
    tag = labels[results_index]

    fasttext.FastText.eprint = lambda x: None 
    lang_model = fasttext.load_model('lid.176.ftz')
    detect_lang = lang_model.predict(my_input, k=1)[0][0]
    lang_name = languages.get(alpha_2=detect_lang[-2:]).name

    if detect_lang != "__label__en" and detect_lang != "__label__es":
        
        response = "Sorry, I don't speak " + lang_name + ". I only speak English and Spanish."
        return response, lang_name
    
    else:

        for topic in data["intents"]:

            if topic["tag"] == tag and tag == "time":
                response = "The time is " \
                            + datetime.datetime.now().strftime("%I") \
                            + ":" \
                            + datetime.datetime.now().strftime("%M") \
                            + ":" \
                            + datetime.datetime.now().strftime("%S") \
                            + " " \
                            + datetime.datetime.now().strftime("%p") \

                return response, lang_name

            elif topic["tag"] == tag and tag == "date":
                response = "Today is " \
                            + datetime.datetime.now().strftime("%A") \
                            + " " \
                            + datetime.datetime.now().strftime("%B") \
                            + " " \
                            + datetime.datetime.now().strftime("%d") \
                            + ", " \
                            + datetime.datetime.now().strftime("%Y")

                return response, lang_name

            elif topic["tag"] == tag:
                responses = topic["responses"]
                response = random.choice(responses)
                return response, lang_name
