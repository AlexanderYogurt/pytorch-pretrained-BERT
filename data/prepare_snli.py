import jsonlines, json
import os
import re
import numpy as np
import spacy
from spacy.tokenizer import Tokenizer
# nlp = spacy.load("en_core_web_sm")
from spacy.lang.en import English
nlp = English()

from tqdm import tqdm

def prepare_dataset(dataset):
    
    with jsonlines.open(dataset) as reader, open("advesarial_test.tsv", "w") as writer:
        writer.write("index captionID   pairID  sentence1_binary_parse  sentence2_binary_parse  sentence1_parse sentence2_parse sentence1   sentence2   label1  label2  label3  label4  label5  gold_label\n")
        
        idx = 0
        for t in tqdm(reader, desc="loading "+dataset):
            premise = t['sentence1']
            hypothesis = t['sentence2']
            label = t['gold_label']
            index = str(idx)
            idx += 1

            writer.write("{} dummy dummy dummy dummy dummy dummy {} {} {}\n".format(index, premise, hypothesis, label)) 

print("Transforming the data...\n")

prepare_dataset("./data/data/dataset.jsonl")