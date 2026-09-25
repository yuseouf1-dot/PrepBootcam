import csv

def load_reference_data(filepath):
    reference_data = {}
    standard_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lang = row['Language']
            freq_dict = {}
            
            for char in standard_alphabet:
                if char in row and row[char].strip() != "":
                    freq_dict[char] = float(row[char])
                    
            reference_data[lang] = freq_dict
            
    return reference_data

def check_percentages(text):
    text = text.lower()
    letter_counts = {}
    total_letters = 0
    percentages = {}
    standard_alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char in standard_alphabet:
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


language_percentages_data = load_reference_data('frequencies.csv')
unknown_string = input("Enter a string: ")
result = check_percentages(unknown_string)

guessed_language = infer_language(result, language_percentages_data)
print(f"[Language]: {guessed_language}")