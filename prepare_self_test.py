import jsonlines, json
import os
import re
import numpy as np
#import spacy
#from spacy.tokenizer import Tokenizer
# nlp = spacy.load("en_core_web_sm")
#from spacy.lang.en import English
#nlp = English()

from tqdm import tqdm

def prepare_dataset():
    
    with open("./data/SNLI/self_designed_test.tsv", "w+") as writer:
        writer.write("index\t captionID\t pairID\t sentence1_binary_parse\t sentence2_binary_parse\t sentence1_parse\t sentence2_parse\t sentence1\t sentence2\t label1\t  label2\t  label3\t  label4\t  label5\t  gold_label\n")

        premise = "A cat is sleeping under the couch."
        hypothesis = "There is an animal present."
        label = "entailment"
        index = "0"
        writer.write("{}\tdummy\tdummy\tdummy\tdummy\tdummy\tdummy\t{}\t{}\t1\t2\t3\t4\t5\t{}\n".format(index, premise, hypothesis, label)) 

        premise = "A cat is sleeping under the couch."
        hypothesis = "There is a dog present."
        label = "contradiction"
        index = "1"
        writer.write("{}\tdummy\tdummy\tdummy\tdummy\tdummy\tdummy\t{}\t{}\t1\t2\t3\t4\t5\t{}\n".format(index, premise, hypothesis, label)) 

        premise = "An animal is sleeping under the couch."
        hypothesis = "There is a cat present."
        label = "neutral"
        index = "2"
        writer.write("{}\tdummy\tdummy\tdummy\tdummy\tdummy\tdummy\t{}\t{}\t1\t2\t3\t4\t5\t{}\n".format(index, premise, hypothesis, label)) 


print("Preparing the data...\n")

prepare_dataset()
