import pandas as pd

# Function to process format one: pairs delimited by ' - '
def process_format_one(lines):
    filtered_originals = []
    filtered_translations = []

    for line in lines:
        if ' - ' in line:
            pairs = line.split(' - ')
            for i in range(0, len(pairs), 2):
                if i + 1 < len(pairs):
                    original = pairs[i].strip()
                    translation = pairs[i + 1].strip()

                    if original != translation:
                        filtered_originals.append(original)
                        filtered_translations.append(translation)

    return filtered_originals, filtered_translations

# Function to process format two: tab-separated values
def process_format_two(lines):
    filtered_originals = []
    filtered_translations = []

    for line in lines:
        parts = line.split('\t')
        if len(parts) >= 2:
            original = parts[1].strip()
            translation = parts[2].strip()

            if original != translation:
                filtered_originals.append(original)
                filtered_translations.append(translation)

    return filtered_originals, filtered_translations

# Function to process format three: pairs separated by '-' on new lines
def process_format_three(lines):
    filtered_originals = []
    filtered_translations = []

    i = 0
    while i < len(lines):
        original = lines[i].strip()
        i += 1
        if i < len(lines) and lines[i].strip() == '-':
            i += 1
            if i < len(lines):
                translation = lines[i].strip()
                i += 1
                if original != translation:
                    filtered_originals.append(original)
                    filtered_translations.append(translation)

    return filtered_originals, filtered_translations

# Function to process format four: tabular format with columns
def process_format_four(file_path):
    try:
        df = pd.read_csv(file_path, delimiter='\t', encoding='utf-8', on_bad_lines='skip')
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return pd.DataFrame(columns=['original', 'parafraza'])

    # Check if the 'ali_podvojeno' column exists
    if 'ali_podvojeno' in df.columns:
        # Filter out rows where 'ali_podvojeno' is 1
        filtered_df = df[df['ali_podvojeno'] == 0]
    else:
        print(f"Column 'ali_podvojeno' not found in {file_path}. Skipping filtering.")
        filtered_df = df

    # Select relevant columns
    if 'vprašanje1' in filtered_df.columns and 'vprašanje2' in filtered_df.columns:
        filtered_df = filtered_df[['vprašanje1', 'vprašanje2']]
    else:
        print(f"Columns 'vprašanje1' or 'vprašanje2' not found in {file_path}. Returning empty DataFrame.")
        return pd.DataFrame(columns=['original', 'parafraza'])

    # Rename columns to match the expected output format
    filtered_df.columns = ['original', 'parafraza']

    return filtered_df

# Main function to process files
def process_files(file_paths, output_file_paths):
    for file_path, output_file_path in zip(file_paths, output_file_paths):
        try:
            # Add debug print to verify file exists
            print(f"Attempting to process: {file_path}")

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            lines = content.strip().split('\n')

            # Check if file is empty
            if not lines:
                print(f"Empty file: {file_path}")
                continue

            # Add debug print to show first few lines
            print(f"First few lines of {file_path}:")
            print('\n'.join(lines[:3]))

            # Try to determine format and process
            try:
                filtered_df = None
                if ' - ' in lines[0]:
                    filtered_originals, filtered_translations = process_format_one(lines)
                elif '\t' in lines[0]:
                    # Try format two first, if fails, try format four
                    try:
                        filtered_originals, filtered_translations = process_format_two(lines)
                    except:
                        filtered_df = process_format_four(file_path)
                elif '-' in lines[0]:
                    filtered_originals, filtered_translations = process_format_three(lines)
                else:
                    # Try format four as fallback
                    try:
                        filtered_df = process_format_four(file_path)
                    except Exception as e:
                        print(f"Unknown format in file: {file_path}")
                        print(f"Error details: {str(e)}")
                        continue

                # Create DataFrame if not already created
                if filtered_df is None:
                    filtered_df = pd.DataFrame({
                        'original': filtered_originals,
                        'parafraza': filtered_translations
                    })

                # Save to file
                filtered_df.to_csv(output_file_path, index=False, encoding='utf-8-sig', sep='\t')
                print(f"\nProcessed {len(filtered_df)} pairs from {file_path}")
                print(f"Saved to {output_file_path}")

            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
                print("Full error details:", e.__class__.__name__)

        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")

# Example usage
file_paths = [
    '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/para-nmt-50m-small_test_translations_GPT3.5.txt',
    '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/msr_paraphrase_test_translations_GPT3.5.txt',
    '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/paws_paraphrase_test_3.1_translations_GPT3.5.txt',
    '/Users/alenka/Desktop/study/Programiranje/datoteke/Ontologija parafraz_mag delo/Github/paraphrase_categorization/quora_test_translations_GPT3.5.txt'
]

output_file_paths = [
    'para_nmt_filtered_paraphrases.csv',
    'msr_filtered_paraphrases.csv',
    'paws_filtered_paraphrases.csv',
    'quora_filtered_paraphrases.csv'
]

process_files(file_paths, output_file_paths)