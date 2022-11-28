from typing import TextIO

import nltk

#nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
from tensorflow.python.framework import ops
import random
import json
import pickle
import re

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

COMPLEXITY_COMPS = {
    'log(n)':1,
    'n':2,
    'nlog(n)':3,
    'n^2':4,
    '2^n':5,
    'n!':6
}

SORTING_ALGS = {
    'quicksort':1,
    'mergesort':2,
    'timsort':3,
    'heapsort':4,
    'bubble sort':5,
    'insertion sort':6,
    'selection sort': 7,
    'tree sort': 8,
    'shell sort': 9,
    'bucket sort': 10,
    'counting sort':11,
    'cubesort':12
}
with open(r"C:\Users\Timothy Choi\chatting\chat\.venv\intents.json", encoding="UTF-8") as file:
    data = json.load(file)
    #data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)


    ops.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 5)
    net = tflearn.fully_connected(net, 6)
    net = tflearn.fully_connected(net, 5)
    #net = tflearn.fully_connected(net, 5)
    #net = tflearn.fully_connected(net, 7)
    #net = tflearn.fully_connected(net, 6)
    #net = tflearn.fully_connected(net, 6)
    #net = tflearn.fully_connected(net, 6)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch = 200, batch_size = 3, show_metric=True)
    #model.fit(training, output, n_epoch=400,validation_set=.2, batch_size=8, validation_batch_size=8, show_metric=True)

    model.save("model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def compare(i_words):
    val1 = 0
    val2 = 0
    for word in i_words:
        if word in COMPLEXITY_COMPS.keys():
            if val1==0:
                val1 = word
                continue
            else:
                val2 = word
                break
        if word in SORTING_ALGS.keys():
            if val1==0:
                val1 = word
                continue
    print(val1)
    print(val2)
    if val2 != 0:
        if COMPLEXITY_COMPS[val1] > COMPLEXITY_COMPS[val2]:
            return (f"O({val1}) is slower than O({val2})")
        else:
            return (f"O({val1}) is faster than O({val2})")
    else:
        if "best" in i_words:
            if val1 == "quicksort" or val1 == "mergesort" or val1 == "heapsort" or val1 == "tree sort" or val1 == "shell sort": 
                return ("Best time complexity is Ω(nlog(n))")
            elif val1 == "timsort" or val1 == "bubble sort" or val1 == "insertion sort" or 13:
                return ("Best time complexity is Ω(n)")
            elif val1 == "bucket sort" or val1 == "cubesort": 
                return ("Best time complexity is Ω(n+k)")
            elif val1 == "counting sort": 
                return ("Best time complexity is Ω(nk)")
            elif val1 == "selection sort" :
                return ("Best time complexity is Ω(n^2)")
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
        elif "average" in i_words:
            if val1 == "quicksort" or val1 == "mergesort" or val1 == "timsort" or val1 == "heapsort" or val1 == "tree sort" or val1 == 13:
                return ("Average time complexity is Θ(nlog(n)).")
            elif val1 == "bubble sort" or val1 == "insertion sort" or val1 == 7:
                return ("Average time complexity is Θ(n^2)")
            elif val1 == "shell sort": 
                return ("Average time complexity is Θ(n(log(n))^2)")
            elif val1 == "bucket sort" or val1 == "cubesort": 
                return ("Best time complexity is Ω(n+k)")
            elif val1 == "counting sort": 
                return ("Best time complexity is Ω(nk)")
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
        elif "worst" in i_words:
            if val1 == "mergesort" or val1 == "timsort" or val1 == "heapsort" or val1 == 13:
                return ("Worst time complexity is O(nlog(n))")
            elif val1 == "quicksort" or val1 == "bubble sort" or val1 == "insertion sort" or val1 == "selection sort" or val1 == "tree sort" or val1 == 10:
                return ("Worst time complexity is O(n^2)")
            elif val1 == "shell sort": 
                return ("Worst time complexity is O(n(log(n))^2)")
            elif val1 == "counting sort": 
                return ("Best time complexity is Ω(nk)")
            elif val1 == "cubesort": 
                return ("Best time complexity is Ω(n+k)")
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")  
"""
def bigOComp(i_words):
    print("BIG-O")
    val1 = 0
    val2 = 0
    for word in i_words:
        if word in COMPLEXITY_COMPS.keys():
            if val1==0:
                val1 = word
                continue
            else:
                val2 = word
                break
    if val1 != "0" and val2 != "0":
        if COMPLEXITY_COMPS[val1] > COMPLEXITY_COMPS[val2]:
            return (f"O({val1}) is slower than O({val2})")
        else:
            return (f"O({val1}) is faster than O({val2})")
    else:
        return "Sorry cant seem to answer that question right now."

def runtime(i_words):
    print("SORTING")
    val1 = 0
    for n in i_words:
        if n in SORTING_ALGS.keys():
            if val1 == 0:
                val1 = n
                continue
    print(val1)
    if "best" in i_words:
        if val1 == "quicksort" or val1 == "mergesort" or val1 == "heapsort" or val1 == "tree sort" or val1 == "shell sort": 
            return ("Best time complexity is Ω(nlog(n))")
        elif val1 == "timsort" or val1 == "bubble sort" or val1 == "insertion sort" or 13:
            return ("Best time complexity is Ω(n)")
        elif val1 == "bucket sort" or val1 == "cubesort": 
            return ("Best time complexity is Ω(n+k)")
        elif val1 == "counting sort": 
            return ("Best time complexity is Ω(nk)")
        elif val1 == "selection sort" :
            return ("Best time complexity is Ω(n^2)")
        else:
            return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
    elif "average" in i_words:
        if val1 == "quicksort" or val1 == "mergesort" or val1 == "timsort" or val1 == "heapsort" or val1 == "tree sort" or val1 == 13:
            return ("Average time complexity is Θ(nlog(n)).")
        elif val1 == "bubble sort" or val1 == "insertion sort" or val1 == 7:
            return ("Average time complexity is Θ(n^2)")
        elif val1 == "shell sort": 
            return ("Average time complexity is Θ(n(log(n))^2)")
        elif val1 == "bucket sort" or val1 == "cubesort": 
            return ("Best time complexity is Ω(n+k)")
        elif val1 == "counting sort": 
            return ("Best time complexity is Ω(nk)")
        else:
            return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
    elif "worst" in i_words:
        if val1 == "mergesort" or val1 == "timsort" or val1 == "heapsort" or val1 == 13:
            return ("Worst time complexity is O(nlog(n))")
        elif val1 == "quicksort" or val1 == "bubble sort" or val1 == "insertion sort" or val1 == "selection sort" or val1 == "tree sort" or val1 == 10:
            return ("Worst time complexity is O(n^2)")
        elif val1 == "shell sort": 
            return ("Worst time complexity is O(n(log(n))^2)")
        elif val1 == "counting sort": 
            return ("Best time complexity is Ω(nk)")
        elif val1 == "cubesort": 
            return ("Best time complexity is Ω(n+k)")
        else:
            return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.") 
    else:
        return "I can not seem to find that algorithm. Either ask your Professor, TA, or Google." 
"""

@app.post("/data")
def chat():
    #print("Start talking with the bot (type quit to stop)!")
    inp = request.get_json().get("title")

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == 'sorting':
            inpt = inp.replace("?"," ")
            i_words = inpt.split(" ")
            #outs = runtime(i_words)
            outs = compare(i_words)
            return { "Message": outs}
        elif tg['tag'] == 'Big-O':
            inpt = inp.replace("O("," ")
            inpt = inp.replace(")"," ")
            i_words = inpt.split(" ")
            #outs = bigOComp(i_words)
            outs = compare(i_words)
            return { "Message": outs}   
        elif tg['tag'] == tag:
            responses = tg['responses']
            outs = random.choice(responses)
            print(type(outs))
            return { "Message": outs}
        else:
            continue
    return {"Message": "Enter in a question."}      

if __name__ == "__main__":
    app.run()
