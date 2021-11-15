#!/bin/bash

#n           = 4
#words       = [ 'bcdef', 'abcdefg', 'bcde', 'bcdef' ]
count = int(input())
words = []
while count > 0:
    word = str(input())
    words.append(word)
    count = count - 1
    
word_dict = {}
for word in words:
    word_dict.setdefault(word,0)
    word_dict[word] = word_dict[word] + 1
words_unique = len(word_dict.keys())
words_counts = list(word_dict.values())
print(words_unique)
print(' '.join([str(count) for count in words_counts]))


