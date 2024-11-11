import sys

def read_freq():
    freq = [0] * (ord('Z') - ord('A') + 1)
    nof_chars = 0

    for line in sys.stdin:
        nof_chars += 1
        for c in line.upper():
            nof_chars += 1
            if ord('A') <= ord(c) <= ord('Z'):
                freq[ord(c) - ord('A')] += 1

    return freq, nof_chars

def max_leter(freq):
    ma = freq[0]
    idx = 0
    for i, f in enumerate(freq):
        if f > ma:
            ma = f
            idx = i

    return idx, ma

def print_histogram(freq, nof_chars):
    for i, f in enumerate(freq):
        print(f"{chr(ord('A')+i)} {'*'*(round(100 * f / nof_chars))}")

freq, nof_chars = read_freq()
idx, f = max_leter(freq)

print(f"Most frequent letter: {chr(ord('A')+idx)} ({f})")
print(nof_chars, freq)
print_histogram(freq, nof_chars)