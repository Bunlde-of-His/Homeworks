from collections import Counter
import re

with open('text.txt', 'r') as file:
    content = file.read()

content = re.sub(r'[^\w\s]', ' ', content)

words = content.lower().split()

word_frequency = Counter(words)

sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)


for word, frequency in sorted_word_frequency:
    print(f'{word}: {frequency}')




















