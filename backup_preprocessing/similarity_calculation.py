'''
import pandas as pd
from transformers import T5Tokenizer, T5Model
import torch
import torch.nn.functional as F
import sentencepiece as spm

def load_sloT5_model():
    # Load the SloT5 tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("EMBEDDIA/sloT5")
    model = T5Model.from_pretrained("EMBEDDIA/sloT5")
    return tokenizer, model

def compute_similarity(row, tokenizer, model):
    sentence1 = row['B']
    sentence2 = row['C']
    if pd.notnull(sentence1) and pd.notnull(sentence2):
        # Tokenize the sentences
        inputs1 = tokenizer(sentence1, return_tensors="pt", padding=True, truncation=True)
        inputs2 = tokenizer(sentence2, return_tensors="pt", padding=True, truncation=True)

        # Generate embeddings using the encoder part of the T5 model
        with torch.no_grad():
            outputs1 = model.encoder(**inputs1)
            outputs2 = model.encoder(**inputs2)

        # Use the mean of the last hidden states as the sentence embedding
        embeddings1 = outputs1.last_hidden_state.mean(dim=1)
        embeddings2 = outputs2.last_hidden_state.mean(dim=1)

        # Compute cosine similarity
        similarity = F.cosine_similarity(embeddings1, embeddings2)
        return similarity.item()
    else:
        return None

def compare_sentences_in_excel(input_file_path, output_file_path):
    # Load the SloT5 model and tokenizer
    tokenizer, model = load_sloT5_model()

    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file_path)

    # Apply the function to each row and store the similarity score in a new column
    df['Similarity'] = df.apply(compute_similarity, axis=1, tokenizer=tokenizer, model=model)

    # Save the updated DataFrame to a new Excel file
    df.to_excel(output_file_path, index=False, engine='openpyxl')

    print(f"File with similarity scores has been saved to {output_file_path}")

# Example usage
input_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_nepodvojene_filtrirane_parafraze.xlsx'
output_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_similarity.xlsx'
compare_sentences_in_excel(input_file_path, output_file_path)
'''

# Usage of METEOR
import pandas as pd
import spacy
from nltk.translate.meteor_score import meteor_score

# Naložite slovenski model
nlp = spacy.load("sl_core_news_sm")

def preprocess_and_evaluate(input_file_path, output_file_path):
    # Naložite Excel datoteko v DataFrame
    df = pd.read_excel(input_file_path)

    # Izpišite imena stolpcev za preverjanje
    print("Stolpci v DataFrame:", df.columns)

    # Zagotovite pravilna imena stolpcev
    original_column = 'original'
    paraphrase_column = 'parafraza'

    # Funkcija za tokenizacijo s SpaCy
    def tokenize_slovenian(text):
        doc = nlp(str(text))
        return [token.text for token in doc]

    # Funkcija za izračun METEOR ocene
    def compute_meteor(row):
        try:
            original = str(row[original_column])
            paraphrase = str(row[paraphrase_column])
            
            # Tokenizacija z uporabo SpaCy za slovenščino
            tokenized_original = tokenize_slovenian(original)
            tokenized_paraphrase = tokenize_slovenian(paraphrase)
            
            return meteor_score([tokenized_original], tokenized_paraphrase)
        except Exception as e:
            print(f"Napaka pri obdelavi vrstice: {row}")
            print(f"Podrobnosti napake: {e}")
            return None

    # Uporabite funkcijo za vsako vrstico in shranite oceno v nov stolpec
    df['METEOR_Score'] = df.apply(compute_meteor, axis=1)
    
    # Odstranite vrstice z vrednostmi None, če je potrebno
    df = df.dropna(subset=['METEOR_Score'])

    # Shranite posodobljen DataFrame v novo Excel datoteko
    df.to_excel(output_file_path, index=False, engine='openpyxl')

    print(f"Datoteka z METEOR ocenami je bila shranjena na {output_file_path}")

# Primer uporabe
input_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_nepodvojene_filtrirane_parafraze.xlsx'
output_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_similarity.xlsx'
preprocess_and_evaluate(input_file_path, output_file_path)