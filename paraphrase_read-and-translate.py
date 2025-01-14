# parafraziranje - učne množice

import random
import os
import csv

# Quora Question Pairs dataset - https://huggingface.co/datasets/quora-competitions/quora/blob/main/quora.py

file_path_quora = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/paraphrase_dataset/quora_duplicate_questions.tsv'

with open(file_path_quora, 'r') as file:
    for index, line in enumerate(file):
        print(line)

        if index >= 10:
            break

data_quora = {}

with open(file_path_quora, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 5:
            sentence = parts[3].strip()
            paraphrase = parts[4].strip()
            data_quora[sentence] = paraphrase

if not data_quora:
    print("No valid sentences found.")

random_quora = dict(random.sample(data_quora.items(), 300))
if not random_quora:
    print("No valid sentences found.")

for sentence, paraphrase in data_quora.items():
    print(f"Stavek: {sentence}\nParafraza: {paraphrase}\n")
