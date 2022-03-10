#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import string

input_text = open('idz2.txt', 'r').read().lower().split(' ')
alphabet = list(string.ascii_lowercase)
unique_words = []

for word in input_text:
    if word not in unique_words:
        unique_words.append(word)
unique_words = re.sub(r'[^\w\s]', '', str(unique_words)).split()

min_value = len(unique_words)
min_char = 0
for char in alphabet:
    counter = 0
    for word in unique_words:
        if char in word:
            counter += 1
    if counter < min_value:
        min_value = counter
        min_char = char
    print(f'Буква {char.upper()} встречается в {round(counter / len(unique_words) * 100, 2)}% слов.')

print(f'\tБуква {min_char.upper()} встречалась в {round(min_value / len(unique_words) * 100, 2)}% слов.'
      f'ЭТО САМАЯ РЕДКАЯ БУКВА В ТЕКСТЕ')