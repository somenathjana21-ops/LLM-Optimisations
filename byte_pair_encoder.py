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

def bpe_A(batch_):
    print("")
    #calculation of adjucent character and saving into a tupple
    #calculation for the 353 words in the list then be carried out
    tup_list = []
    for i,c  in enumerate(batch_) :#i is the index and c is the word there
        chars_c = list(c)#converts c(i.e the word in batch_ to character list)
        for n , ch in enumerate(chars_c):#n being the index and ch being the character of the current word in n index
            if n != (len(chars_c)-1):#check to not give a error because char_c[n+1] would not exist if n = len(char_c)-1
                m_t = (ch,chars_c[n+1])#it would exist on if n = len(char_c) - 2,so chars_c[n+1] gives the last ch
                #m_t would thus be the tupple for adjucent letter for word c
                #appending to a list now 
                tup_list.append(m_t)#contains tupples for adjucent letters for word c 
            
         



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
#batch_root list contains the matrix of the words in the sentences arranged 
for i in range(1 , 354):#sends the row i of the matrix to bpe 
    bpe_A(batch_=batch_root[i])
    



