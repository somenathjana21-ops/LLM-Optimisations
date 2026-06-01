#logic redo:the file would take in the file.txt,convert to lowercase,and split to get get the words 

#these words would be saved to a json file list known as "pre_token.json" 
import json
def worder():
    filename = "project gutenburg Pride and Prejudice.txt"
    with open(filename,"r",encoding="utf-8") as file:
        text = file.read()

    text_lower = text.lower()
    #lowercased words  
    txt = text_lower.split()
    #words splited for use
    j_list = "pre_token.json" 
    with open(j_list,"w",encoding="utf-8") as j_file:
        json.dump(txt,j_file)

    