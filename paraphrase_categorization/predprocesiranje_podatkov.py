import pandas as pd

# Read the file content
file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_paraphrase_test_3.1_translations_GPT3.5.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into lines
lines = content.strip().split('\n')

# Initialize lists to store the data
filtered_originals = []
filtered_translations = []

# Iterate over the lines and process pairs
for line in lines:
    if ' - ' in line:
        # Split into pairs based on even occurrences of '-'
        pairs = line.split(' - ')
        for i in range(0, len(pairs), 2):
            if i + 1 < len(pairs):
                original = pairs[i].strip()
                translation = pairs[i + 1].strip()

                if original != translation:
                    filtered_originals.append(original)
                    filtered_translations.append(translation)

# Create a DataFrame with filtered data
filtered_df = pd.DataFrame({
    'original': filtered_originals,
    'parafraza': filtered_translations
})

# Save with proper column formatting
output_file_path = 'paws_nepodvojeni_filtered_paraphrases.csv'
filtered_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

# Display preview
print("\nFirst few rows of saved data:")
print(filtered_df.head())
print(f"\nFiltered data saved to {output_file_path}")