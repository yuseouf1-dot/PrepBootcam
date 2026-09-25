import csv

def load_reference_data_utf8(filepath):
    reference_data = {}
    
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lang = row['Language']
            freq_dict = {}
            
            for char, value in row.items():
                if char is not None and char != 'Language' and isinstance(value, str) and value.strip() != "":
                    freq_dict[char] = float(value)
                    
            reference_data[lang] = freq_dict
            
    return reference_data

def check_percentages_utf8(text):
    text = text.lower()
    letter_counts = {}
    total_letters = 0
    percentages = {}

    for char in text:
        if char.isalpha():
            total_letters += 1
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    if total_letters == 0:
        return {}

    for char, count in letter_counts.items():
        percentages[char] = (count / total_letters) * 100

    return percentages

def infer_language(text_percentages, reference_data):
    best_language = "Unknown"
    min_error = float('inf')
    
    for lang, ref_percentages in reference_data.items():
        current_error = 0
        for char, text_percent in text_percentages.items():
            ref_percent = ref_percentages.get(char, 0)
            current_error += abs(text_percent - ref_percent)
            
        if current_error < min_error:
            min_error = current_error
            best_language = lang
            
    return best_language


language_percentages_data = load_reference_data_utf8('frequencies.csv')
unknown_string = input("Enter a string: ")
result = check_percentages_utf8(unknown_string)


guessed_language = infer_language(result, language_percentages_data)
print(f"[Language]: {guessed_language}")