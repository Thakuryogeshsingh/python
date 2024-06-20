import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from codeswitch.codeswitch import LanguageIdentification
from sympy.solvers.ode.subscheck import checkodesol, checksysodesol
import sympy
from fuzzywuzzy import fuzz
import rapidfuzz as rfuzz


# file_path = filedialog.askopenfilename(title='Hello Data')
# dataset = pd.read_excel(file_path, header=1)

# df = pd.DataFrame(dataset)
# print(df.head())


lid = LanguageIdentification('hin-eng')
# text = "customer khud service kar leta hai"
text = "workshop me free service me bhi oil chnge ke."
result = lid.identify(text) 
print(result)

import pkg_resources
from symspellpy import SymSpell, Verbosity
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)


def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt
                
def correctEngWords(test_str):
    dict_list = lid.identify(test_str)
    index_list = [token['start']  for token in dict_list if token['entity'] == 'en'] 
    word_list = [token['word']  for token in dict_list if token['entity'] == 'en'] 
    # print("Index is:",index_list)
    # print("Word list is:",word_list)
    words = test_str.split(' ')
    print(words)
    len_words = [len(word)+1 for word in words]
    word_index = np.cumsum(np.array(len_words))
    word_index = np.insert(word_index, [0],0)
    word_index = np.delete(word_index, [-1])
    print("Word Index is:",word_index)
    word_corr_array = flatten([[item.term for item in sym_spell.lookup(words[i] , Verbosity.TOP, max_edit_distance=2)] if word_index[i] in index_list else words[i] for i in range(len(words))])

    print(word_corr_array)
    test_str = ' '.join(word_corr_array)
    words = test_str.split(' ')
    print(test_str)
    dict_list = lid.identify(test_str)
    index_list = [token['start']  for token in dict_list if token['entity'] == 'en'] 
    word_list = [token['word']  for token in dict_list if token['entity'] == 'en'] 
    print(index_list)
    
    len_words = [len(word)+1 for word in word_corr_array]
    word_index = np.cumsum(np.array(len_words))
    word_index = np.insert(word_index, [0],0)
    word_index = np.delete(word_index, [-1])
    print(word_index)
    print([words[i] if word_index[i] in index_list else '-' for i in range(len(words))])

    for keyword in auto_keywords_list:
        technical_corrList = [fuzzy_replace(keyword.lower(),words[i].lower()) if word_index[i] in index_list else words[i] for i in range(len(words))]
        
    
    return ' '.join(technical_corrList)

import re
def fuzzy_replace(keyword_str, text_str, threshold=60):
    l = len(keyword_str.split())
    splitted = re.split(r'(\W+)',text_str)
    for i in range(len(splitted)-l+1):
        temp = "".join(splitted[i:i+l])
        if fuzz.ratio(keyword_str, temp) >= threshold:
            before = "".join(splitted[:i])
            after = "".join(splitted[i+l:])
            text_str= before + keyword_str  + after
            splitted = re.split(r'(\W+)',text_str)    
    return text_str


# def fuzzy_replace(keyword_str, text_str, threshold=80):
#     l = len(keyword_str.split())
#     splitted = re.split(r'(\W)+',text_str)
#     for i in range(len(splitted)-l+1):
#         temp = "".join(splitted[i:i+l])
#         temp_next = "".join(splitted[i+1:i])
#         if  rfuzz.fuzz.QRatio(keyword_str, temp+temp_next) >= threshold:
#             before = "".join(splitted[:i])
#             after = "".join(splitted[i+l:])
#             text_str= before + keyword_str  + after
#             splitted = re.split(r'(\W)+',text_str)    
#     return text_str


auto_keywords_list = []

with open("auto_keywords.txt", "r") as f:
    for line in f:
        auto_keywords_list.extend(line.split('\n'))

    
    auto_keywords_list = list(filter(None, auto_keywords_list))
    #auto_keywords_list = [f for f in auto_keywords_list] 


text = 'vehicle ki baterie aur cluch me problem aa gayi thi'

for keyword in auto_keywords_list:
    text = fuzzy_replace(keyword.lower(), text.lower())

text

correctEngWords('vehicle ki baterie aur cluch me problem aa gayi thi')

# with open('auto_keywords.txt','r', encoding='utf-8') as file:
#     for line in file:
        
#         print(line.strip())
