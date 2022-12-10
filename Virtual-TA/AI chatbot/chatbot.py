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
import binarytree
from trees import AVL_Tree, PatriciaTrie

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

COMPLEXITY_COMPS = {
    'log(n':1,
    'n':2,
    'nlog(n':3,
    'n^2':4,
    '2^n':5,
    'n!':6
}

SORTING_ALGS = {
    'quick':1,
    'merge':2,
    'tim':3,
    'heap':4,
    'bubble':5,
    'insertion':6,
    'selection': 7,
    'tree': 8,
    'shell': 9,
    'bucket': 10,
    'count':11,
    'cube':12,
    'radix':13
}
#open intents file so the AI bot can be trained
with open(r"C:\Users\Timothy Choi\chatting\chat\.venv\intents.json", encoding="UTF-8") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
#this is where the nltk tokenizes the intents file that will later be used to compare the users input to the intents file data
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
    #fully connnected neural network that AI trains on
    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, 8)
    #net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 7)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)
    print(len(training[0]))
    print(len(output[0]))

    model = tflearn.DNN(net)
    #model.fit(training, output, n_epoch = 500, batch_size = 2, show_metric=True)
    #model.save("model.tflearn")
    try:
        model.load("model.tflearn")
    except:
        model.fit(training, output, n_epoch = 600, batch_size = 2, show_metric=True)
        model.save("model.tflearn")

#compares the users input to the data fed to the AI on what is simailar to give the tag
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)

#used to get what kind of time complexity is being asked
def getTime(i_words):
    for i in i_words:
        if i == "O(":
            return "O("
        elif i == "$theta(":
            return "Θ("
        elif i == "$Omega(":
            return "Ω("
        else:
            continue

def treeToken(i_words, vals):
    for word in i_words:
        if word == 'binary':
            root = binarytree.build(vals)
            return ' '.join(root.values)
        elif word == 'avl':
            tempTree = AVL_Tree()
            root = None
            for i in vals:
                root = tempTree.insert(root, i)
            tempTree.preOrder(root)
            return ' '.join(tempTree._data)
        elif word == 'pat':
            tempTree = PatriciaTrie()
            for i in vals:
                tempTree.add(i)
            return ' '.join(tempTree._storage)
    return "there seems to be a problem."

#checks to see if the user is comparing 2 time complexity of the same kind
def same(i_words):
    o = 0
    t = 0
    om = 0
    for i in i_words:
        if i == "O(":
            o = o + 1
        elif i == "$theta(":
            t = t + 1
        elif i == "$Omega(":
            om = om + 1
        else:
            continue
    if o == 2 or t == 2 or om == 2:
        return True
    return False

#oringally 2 different methods but as a temporally fix combined the 2 methods because the AI chatBot as of the current time is not able to identify the difference between Big-o and sorting
def compare(i_words):
    val1 = 0
    val2 = 0
    sign = getTime(i_words)
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
    if val2 != 0 and same(i_words):
        if COMPLEXITY_COMPS[val1] > COMPLEXITY_COMPS[val2]:
            return (f"{sign}{val1}) is slower than {sign}{val2}))")
        elif COMPLEXITY_COMPS[val1] == COMPLEXITY_COMPS[val2]:
            return (f"{sign}{val1}) is the same as {sign}{val2}))")
        else:
            return (f"{sign}{val1}) is faster than {sign}{val2}))")
    elif val2 != 0 and not same(i_words):
        return("You cannot compare different Time Complexity")
    elif val1 != 0:
        if "best" in i_words or "fastest" in i_words:
            if val1 == "bubble" or val1 == "insertion" or val1 == "tim" or val1 == "cube":
                return "Best time complexity is Ω(n)"
            elif val1 == "heap" or val1 == "quick" or val1 == "merge" or val1 == "shell" or val1 == "tree":
                return "Best time complexity is Ω(nlog(n))"
            elif val1 == "selection":
                return "Best time complexity is Ω(n^2)"
            elif val1 == "bucket" or val1 == "count":
                return "Best time complexity is Ω(n+k)"
            elif val1 == "radix":
                return "Best time complexity is Ω(nk)"
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
        elif "average" in i_words:
            if val1 == "selection" or val1 == "bubble" or val1 =="insertion":
                return ("Average time complexity is Θ(n^2)")
            elif val1 == "heap" or val1 == "quick" or val1 == "merge" or val1 == "shell" or val1 == "tim" or val1 == "tree" or val1 == "cube":
                return ("Average time complexity is Θ(nlog(n))")
            elif val1 == "bucket" or val1 == "count":
                return ("Average time complexity is Θ(n+k)")
            elif val1 == "radix":
                return ("Average time complexity is Θ(nk)")
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
        elif "worst" in i_words or "slowest" in i_words:
            if val1 == "selection" or val1 == "bubble" or val1 == "insertion" or val1 == "quick" or val1 == "bucket" or val1 == "shell" or val1 == "tree":
                return ("Worst time complexity is O(n^2)")
            elif val1 == "heap" or val1 == "merge" or val1 == "tim" or val1 == "cube":
                return ("Worst time complexity is O(nlog(n))")
            elif val1 == "radix":
                return ("Worst time complexity is O(nk)")
            elif val1 == "count":
                return ("Worst time complexity is O(n+k)")
            else:
                return ("I can not seem to find that algorithm. Either ask your Professor, TA, or Google.")
        else:
            return ("I can not seem to answer that question right now.")
    else:
        return("I did not quite get that please enter the question again")  

#edits the users input in order to get the desire input the methods ask for
def format(inps):
    inps = inps.replace("?"," ")
    inps = inps.replace("O(","O( ")
    inps = inps.replace("$theta(","$theta( ")
    inps = inps.replace("$Omega(","$Omega( ")
    inps = inps.replace(")"," )")
    return inps

#chat function that is called on from the frontend everytime the user types something and returns
@app.post("/data")
def chat():
    inp = request.get_json().get("title")

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == 'sorting':
            inpt = inp.replace("?"," ")
            inpt = format(inpt)
            i_words = inpt.split(" ")
            print("sorting")
            outs = compare(i_words)
            return { "Message": outs}
        elif tg['tag'] == 'Big-O':
            inp = format(inp)
            i_words = inp.split(" ")
            print("Big-o")
            print(i_words)
            outs = compare(i_words)
            return { "Message": outs}
        elif tg['tag'] == 'Tree':
            tempSplit = inp.split(":")
            i_words = tempSplit[-1].split(" ")
            print("tree")
            outs = treeToken(tempSplit[0].split(" "), i_words)
            return { "Message": outs}    
        elif tg['tag'] == tag:
            responses = tg['responses']
            outs = random.choice(responses)
            print(tag)
            print(type(outs))
            return { "Message": outs}
        else:
            continue
    return {"Message": "Enter in a question."}      

if __name__ == "__main__":
    app.run()
