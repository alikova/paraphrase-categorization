import json
from jsonschema import validate, ValidationError

def add_example(file_path, schema_path, category_name, subcategory_name, new_example):
    # Load existing data
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Load JSON schema
    with open(schema_path, 'r', encoding='utf-8') as schema_file:
        schema = json.load(schema_file)

    # Validate existing data against the schema
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"Schema validation error: {e.message}")
        return

    # Find the category and subcategory
    for category in data['kategorije']:
        if category['ime'] == category_name:
            for subcategory in category['podkategorije']:
                if subcategory['ime'] == subcategory_name:
                    # Append the new example
                    subcategory['primera'].append(new_example)
                    break
            break

    # Validate the updated data
    try:
        validate(instance=data, schema=schema)
        # Save the updated data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("New example added successfully.")
    except ValidationError as e:
        print(f"Schema validation error after update: {e.message}")

# Example usage
file_path = 'paraphrase_data.json'
schema_path = 'paraphrase_schema.json'
new_example = {
    "id": 2,
    "izvirnik": "Nov primer izvirnika.",
    "parafraza": "Nov primer parafraze.",
    "prompt": "Nov primer prompta."
}

add_example(file_path, schema_path, 'Leksikalno parafraziranje', 'Zamenjava sopomenk', new_example)
