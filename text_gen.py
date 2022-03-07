
import random

# hello my name is sid k=4
#   x     y     frequency
# hell    o        1
# ello    _        1
# llo_    m        1
# lo_m    y        1
# o_my    _        1

# to generate table of words
def generateTable(data, k=4):

    T = {}
    for i in range(len(data) - k):
        x = data[i:i+k]
        y = data[i+k]

        if T.get(x) is None:
            T[x] = {}
            T[x][y] = 1
        else:
            if T[x].get(y) is None:
                T[x][y] = 1
            else:
                T[x][y] += 1
    return T

T = generateTable("hello hello hella helli")
#print(T)

# to convert freqency of words coming after 4 words into probability
def convertFreqintoProb(T):
    for kx in T.keys():
        s = sum(T[kx].values())
        for k in T[kx].keys():
            T[kx][k] = T[kx][k]/s
    return T

T = convertFreqintoProb(T)
#print(T)

# Read the Data written in the file
def load_text(filepath):
    with open(filepath) as f:
        return f.read().lower()
text = load_text('speech.txt')
#print(text)

# Creating Train Markov Chains
def trainMarkovChain(text, k=4):
    T = generateTable(text, k)
    T = convertFreqintoProb(T)
    return T
model = trainMarkovChain(text)
#print(model)


# to get next digit or word
def sample_next(context, T, k):
    context = context[-k:]
    if T.get(context) is None:
        return " "

    possible_chars = list(T.get(context).keys())
    possible_probabs = list(T.get(context).values())
    return random.choices(possible_chars, weights=possible_probabs)[0]
a = sample_next("politics ", model, 4)
#print(a)


# to get the next sentence
def generateText(starting_sent, T, k=4, maxlen=100):
    sentence = starting_sent
    context = starting_sent[-k:]

    for i in range(maxlen):
        next_pred = sample_next(context, T, k)
        sentence += next_pred
        context = sentence[-k:]
    return sentence

cc = generateText("politics", model, k=4, maxlen=100)
#print(cc)

