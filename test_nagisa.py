import nagisa
import csv

text = 'Pythonで簡単に使えるツールです'
title = [['キーワード','品詞']]
top_list=[]
words=nagisa.tagging(text)
list_words=words.words
list_property=words.postags
if len(list_words)==len(list_property):
    for i in range(len(list_words)):
        top_list.append([list_words[i],list_property[i]])
    with open(r'D:/nagisa.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(title)
        writer.writerows(top_list)
