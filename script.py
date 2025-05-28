import re
import csv

def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def remove_duplicate_chars(s):
    return re.sub(r'(.)\1+', r'\1', s)

def remove_continuous_vowels_consonants(s):
    vowels = "AEIOUaeiou"
    results = set()

    # Remove continuous vowels
    result = re.sub(r'([AEIOUaeiou])\1+', r'\1', s)
    if result != s:
        results.add(result)

    # Remove continuous consonants
    result = re.sub(r'([^AEIOUaeiou])\1+', r'\1', s)
    if result != s:
        results.add(result)

    return results

def remove_stopwords(s, stopwords):
    words = s.split()
    filtered = [word for word in words if word.upper() not in stopwords]
    return " ".join(filtered)

def apply_similar_words(s, similar_dict):
    results = set()
    for key, replacements in similar_dict.items():
        if key in s:
            for repl in replacements:
                results.add(s.replace(key, repl))
    return results

def remove_vowels(s):
    return ''.join(c for c in s if c.upper() not in "AEIOU")

def number_to_words(n):
    num_map = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    return ''.join(num_map.get(c, c) for c in n)

def words_to_number(s):
    word_map = {
        'Zero': '0', 'One': '1', 'Two': '2', 'Three': '3', 'Four': '4',
        'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9'
    }
    for word, num in word_map.items():
        s = re.sub(r'\b' + word + r'\b', num, s, flags=re.IGNORECASE)
    return s

def main():
    names = read_file_lines('names.txt')
    stopwords = set(word.upper() for word in read_file_lines('stopwords.txt'))

    # Load similar words
    similar_lines = read_file_lines('similar.txt')
    similar_dict = {}
    for line in similar_lines:
        if '=' in line:
            key, variants = line.split('=')
            similar_dict[key.strip()] = [v.strip() for v in variants.split(',')]

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['originalstring', 'Listofgenerated'])

        for name in names:
            variants = set()

            # 1. Remove duplicate characters
            variants.add(remove_duplicate_chars(name))

            # 2. Remove continuous vowels or consonants
            variants.update(remove_continuous_vowels_consonants(name))

            # 3. Remove stopwords
            no_stop = remove_stopwords(name, stopwords)
            if no_stop != name:
                variants.add(no_stop)

            # 4. Apply similar words
            variants.update(apply_similar_words(name, similar_dict))

            # 5. Remove vowels
            variants.add(remove_vowels(name))

            # 6. Number <-> Word conversion
            variants.add(number_to_words(name))
            variants.add(words_to_number(name))

            # To avoid duplicates and empty variants
            variants = {v for v in variants if v and v != name}

            writer.writerow([name] + list(variants))

if __name__ == '__main__':
    main()
