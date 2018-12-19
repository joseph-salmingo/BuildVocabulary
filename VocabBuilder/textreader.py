# this module should return each word in the text with several attributes
# 1: frequency within the material
# 2: definition
# 3: presence in word list frequencies
# not sure but i think i don't need to lemmatize
# next goal is to learn how to use the API for oxford dictionary


from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import os
import string
import wordnet_tag_converter as wtc

wnl=WordNetLemmatizer()

file_path = "./testdocument.txt"
test_file = open(file_path)

big_string = test_file.read()
test_file.close()

#break the string into sentences with no punctuation
no_punctuation_tokenizer = RegexpTokenizer(r'\w+')
base_word_list = no_punctuation_tokenizer.tokenize(big_string)

#get part of speech to get the lemma
pos_list = list()
pos_list = pos_tag(base_word_list)

#get each word's lemma
lemma_list = list()
for words in pos_list:

    #using tag converter for lemmatizer
    if len(wtc.get_wordnet_pos(words[1])) == 0:
        continue
    else:
        lemma_list.append(wnl.lemmatize(words[0],
        wtc.get_wordnet_pos(words[1])))

#count up the frequency of the words after lemmatization
count_dict = {}
for words in lemma_list:
   if words in count_dict:
       count_dict[words] = count_dict[words] + 1
   else:
       count_dict[words] = 1

print(count_dict)
