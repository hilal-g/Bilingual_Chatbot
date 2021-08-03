import datetime 
import fasttext
import nltk
import numpy as np 
import psycopg
import random 

from pycountry import languages
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from neural_network import model
from parse_args import args
from preprocess import words, labels, data 

def bag_of_words(s, words):

    bag = [0 for x in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for x in s_words:
        for i, w in enumerate(words):
            if w == x:
                bag[i] = 1
            
    return np.array(bag)

def chat():
    print('\033[1m' + '\n'
          + "Start talking with the bot! Type 'quit' to exit."
          + '\n' + '\033[0m')
    while True:
        my_input = input("You: ")
        if my_input.lower() == "quit":
            break

        else:
            results = model.predict([bag_of_words(my_input, words)])
            results_index = np.argmax(results)
            tag = labels[results_index]

            fasttext.FastText.eprint = lambda x: None 
            lang_model = fasttext.load_model('lid.176.ftz')
            detect_lang = lang_model.predict(my_input, k=1)[0][0]
            lang_name = languages.get(alpha_2=detect_lang[-2:]).name

            if args.use_database == True:

                DB_NAME = "bilingual_chatbot"
                DB_HOST = "localhost"

                pgdb = psycopg.connect(dbname = DB_NAME, host = DB_HOST)
                pgcursor = pgdb.cursor()

                sql = "INSERT INTO user_queries (query, detected_language) VALUES (%s, %s)"

                pgcursor.execute(sql, (my_input, lang_name))
                pgdb.commit()


            if detect_lang != "__label__en" and detect_lang != "__label__es":
                
                    response = "Sorry, I don't speak " + lang_name + ". I only speak English and Spanish."
                    print(response)
            
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

                        print(response)

                    elif topic["tag"] == tag and tag == "date":
                        response = "Today is " \
                                    + datetime.datetime.now().strftime("%A") \
                                    + " " \
                                    + datetime.datetime.now().strftime("%B") \
                                    + " " \
                                    + datetime.datetime.now().strftime("%d") \
                                    + ", " \
                                    + datetime.datetime.now().strftime("%Y")

                        print(response)

                    elif topic["tag"] == tag:
                        responses = topic["responses"]

                        response = random.choice(responses)
                        print(response)

chat()