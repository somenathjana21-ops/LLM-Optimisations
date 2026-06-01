#this file would be tokenizing the said provided json file into tokens 
import json 
import math

#logic:word in list from json -> list lenght is measured -> the nearest it is divided by Number of batches ≈ √N number 
#the divided result would give me the batch word lenght
# a batchword lenght is the lenght in which results are added to the vocab 

def batcher(root_len):
    for i in range(root_Len+1):
        temp_list = word_corpus[(root_Len*(i-1)):(root_Len*i)] #each batched list is then added to batch_root
        batch_root.append(temp_list)#appending the temporary list here



filename = "pre_token.json"

with open(filename,"r",encoding="utf-8") as file:
    word_corpus = json.load(file)
#lenght of the word_corpus is sent to closest integer
len = len(word_corpus)#125507 words total 

root_Len = int(math.sqrt(len))
batch_root = []
batcher(root_len=root_Len)#no return value
#root_len now has all the batched words in a 353 by 353 matrix of words

#this gives root_Len as 353 thus batch size would 353 by 353 , however we would be loosing 898 words.This is loss here which we can take for now 



