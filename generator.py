import random
import numpy

ADJECTIVES = "dic/adjectives.txt"
NOUNS = "dic/nouns.txt"
VERBS = "dic/verbs.txt"
TEMPLATE = "ANVAN"

def random_line(filename):
    lines = open(filename).read().splitlines()
    myline = random.choice(lines)
    return myline

def random_lines(filename, amount):
    lines = lines = open(filename).read().splitlines()
    mylines = random.sample(lines, amount)
    return mylines

quote = ""
for char in TEMPLATE:
    if(char == "A"):
        range = numpy.random.choice(numpy.arange(0, 5), p=[0.2, 0.4, 0.2, 0.1, 0.1])
        adjectives = random_lines(ADJECTIVES, range)
        for index, adjective in enumerate(adjectives):
            quote += adjective
            if (index + 1 == range):
                quote += " "
            else:
                quote += ", "
    if(char == "N"):
        quote += random_line(NOUNS) + " "
    if(char == "V"):
        quote += random_line(VERBS) + " "
print(quote)
