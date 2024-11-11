"""Counting word occurences in Shakespeare plays"""


histogram = {}
punctuation = {ord(i): " " for i in "\".,:;-!?=[]()"}

with open("Programovani I/counting words/kjv.txt", "r", encoding="utf8") as file:
    for line in file.readlines():
        line = (line
                .translate(punctuation)
                .strip()
                .upper()
                .split()
                )

        for word in line:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

i = 1
for word in sorted(histogram, key=histogram.get, reverse=True):
    print((word + " " + str(histogram[word])).rjust(15)[-15:], end=" | ")

    if i % 10 == 0:
        input()
    i += 1
    
    
    
    
