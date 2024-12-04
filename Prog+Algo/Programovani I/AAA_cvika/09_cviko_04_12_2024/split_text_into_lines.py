import sys
from string import ascii_lowercase


def read_input():
    out = []
    for line in sys.stdin.readlines():
        formatted_line = ""
        for char in line:
            if char.lower() in ascii_lowercase + " ":
                formatted_line += char
            else:
                formatted_line += " "
        for word in formatted_line.split():
            out.append(word)
    return out

words = read_input()

out = ""
line_len = 0
for word in words:
    word_len = len(word)
    line_len += word_len

    if word_len >= 30:  # if this word itself is longer than/equal to 30 characters
        line_len = 100  # ensure that the word will get its own line
        out += "\n"
    elif line_len > 30:   # if adding this word would exceed 30 characters
        line_len = word_len  # reset line_len
        out += "\n"

    out += word + " "
    line_len += 1 # account for the space after added word

print(out)
