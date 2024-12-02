import pandas as pd
import hazm
from hazm.utils import stopwords_list
import numpy as np
import math

punctuation = [".","|","؟","،","«",'»',"!","<",">",")","(",":","؛","#","$","%","^","&","*","[","]","}","{","_","-","/","+","'","۱","۲","۳","۴","۵","۶","۷","۸","۹","۰"]

dict_cat_1 = {}
dict_cat_2 = {}
dict_cat_3 = {}
dict_cat_4 = {}
dict_cat_5 = {}
dict_cat_6 = {}

df_train = pd.read_csv('books_train.csv')
df_test = pd.read_csv('books_test.csv')

lemmatizer = hazm.Lemmatizer()
normalizer = hazm.Normalizer()
stopwords_list = hazm.stopwords_list()

books_data = ['title', 'description', 'categories']
list_all_words = {}
cats = ["کلیات اسلام", "مدیریت و کسب و کار", "داستان کودک و نوجوانان", "رمان", "داستان کوتاه", "جامعه‌شناسی"]

def simplify_text(string):
    normalized_string = normalizer.normalize(string)
    normalized_string = ''.join(char for char in normalized_string if char not in punctuation)
    tokenized_list = hazm.word_tokenize(normalized_string)
    lemmatized_list = (lemmatizer.lemmatize(" ".join(tokenized_list))).split(" ")
    #final_list = [word for word in lemmatized_list if word not in stopwords_list]
    return lemmatized_list

def get_each_cat_words(categorie, description_list_words, title_list_words, index_category, dict_cat):
    if(categorie == cats[index_category]):
        for word in (description_list_words + title_list_words):
            if word in dict_cat.keys():
                dict_cat[word] = dict_cat[word] + 1
            else:
                dict_cat[word] = 1

def make_bag_of_words():
    for row in range(len(df_train)):
        description_list_words = simplify_text(df_train.loc[row]['description'])
        title_list_words = simplify_text(df_train.loc[row]['title'])
        for i in range(6):
            get_each_cat_words(df_train.loc[row]['categories'], description_list_words, title_list_words, i,get_dict_cat_words(i) )
        #get_each_cat_words(df_train.loc[row]['categories'], description_list_words, title_list_words)
    dict_cat_1.update(dict_cat_2)
    dict_cat_1.update(dict_cat_3)
    dict_cat_1.update(dict_cat_4)
    dict_cat_1.update(dict_cat_5)
    dict_cat_1.update(dict_cat_6)
    return dict_cat_1

def get_dict_cat_words(i):
    if(i == 0):
        return dict_cat_1
    if(i == 1):
        return dict_cat_2
    if(i == 2):
        return dict_cat_3
    if(i == 3):
        return dict_cat_4
    if(i == 4):
        return dict_cat_5
    if(i == 5):
        return dict_cat_6
    
def sum_dict_values(dict_cat):
    count = 0
    for value in dict_cat.values():
        count = count + value
    return count

def calculate_probability_this_cat(list_cat_words, test_words):
    final_probability = 0
    word_count_in_dict = sum_dict_values(list_cat_words)
    for word in test_words:
        if word in list_cat_words.keys():
            final_probability = final_probability + math.log(list_cat_words[word] / word_count_in_dict)
        else:
            final_probability = final_probability + math.log(0.01 / word_count_in_dict)
    return final_probability

def belongs_to_which_cat(book_words):
    probability_all_6_cat = []
    for i in range(6):
        final_probability = calculate_probability_this_cat(get_dict_cat_words(i), book_words)
        probability_all_6_cat.append(final_probability)
    return probability_all_6_cat.index(max(probability_all_6_cat))

list_all_words = make_bag_of_words()
right_choose = 0
for row in range(len(df_test)):
    description_test_words = simplify_text(df_test.loc[row][1])
    title_test_words = simplify_text(df_test.loc[row][0])
    index_max_probable_cat = belongs_to_which_cat(description_test_words + title_test_words)
    if cats[index_max_probable_cat] == df_test.loc[row][2]:
        right_choose = right_choose + 1
print(right_choose / len(df_test))