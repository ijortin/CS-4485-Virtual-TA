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
import binarytree
from trees import AVL_Tree, PatriciaTrie, patricia

from flask import Flask, jsonify, request

app = Flask(__name__)

COMPLEXITY_COMPS = {
    'log(n)':1,
    'n':2,
    'nlog(n)':3,
    'n^2':4,
    '2^n':5,
    'n!':6
}

with open(r'C:\Users\Timothy Choi\chatting\chat\.venv\intents.json') as file:
    data = json.load(file)

try:
    with open("data.pickle", "rt") as f:
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
        # net = tflearn.fully_connected(net, 6)
    net = tflearn.fully_connected(net, 5)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)
    model.fit(training, output, n_epoch=100, batch_size=1, show_metric=True)
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

def bigOComp(i_words):
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
    if COMPLEXITY_COMPS[val1] > COMPLEXITY_COMPS[val2]:
        return (f"O({val1}) is slower than O({val2})")
    else:
        return (f"O({val1}) is faster than O({val2})")

def treeToken(i_words, vals):
    for word in i_words:
        if word == 'binary':
            root = binarytree.build(vals)
            return ' '.join(root.preorder)
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

@app.post("/data")
def chat():
    print("Start talking with the bot (type quit to stop)!")
    inp = request.get_json().get("title")

    results = model.predict([bag_of_words(inp, words)])
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    for tg in data["intents"]:
        if tg['tag'] == 'Big-O':
            i_words = inp.split(" ")
            outs = bigOComp(i_words)
            return { "Message": outs,}  
        elif tg['tag'] == 'Tree':
            tempSplit = inp.split(":")
            i_words = tempSplit[-1].split(" ")
            outs = treeToken(tempSplit[0].split(" "), i_words)
            return { "Message": outs,} 
        elif tg['tag'] == tag:
            responses = tg['responses']
            outs = random.choice(responses)
            return { "Message": outs,}      
    

if __name__ == "__main__":
    app.run()
