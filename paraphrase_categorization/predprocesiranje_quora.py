'''
# Define the file path
input_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/para-nmt-50m-small_test_translations_GPT3.5.txt'  # Replace with your file path
output_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paranmt_preprocessed.txt'  # Replace with your desired output path

# Open the file and read its contents
with open(input_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Save the file with utf-8-sig encoding
with open(output_file_path, 'w', encoding='utf-8-sig') as file:
    file.write(content)

print(f"File has been saved with utf-8-sig encoding to {output_file_path}")
'''

import pandas as pd

def clean_excel_file(input_file_path, output_file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file_path)

    # Function to check if a row is empty or contains only '-'
    def is_empty_or_dash(row):
        #return row.isnull().all() or all(str(cell).strip() == '-' for cell in row)
        return all(str(cell).strip() == '-' for cell in row if pd.notnull(cell))
        

    # Apply the function to filter out unwanted rows
    df = df[~df.apply(is_empty_or_dash, axis=1)]

    # Save the cleaned DataFrame to a new Excel file
    df.to_excel(output_file_path, index=False)

    print(f"Cleaned file has been saved to {output_file_path}")

# Example usage
input_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/predprocesiranje_quora.xltx'  # Replace with your file path
output_file_path = '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/predprocesiranje_quora_clean.xlsx'  # Replace with your desired output path
clean_excel_file(input_file_path, output_file_path)


