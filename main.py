path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_content = f.read()

def num_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    dict = {}
    for char in lowered_text:
        if char.isalpha():
            dict[char] = dict.get(char, 0) + 1
    return dict

def report(text):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_of_words(text)} words found in the document.")
    for k, v in count_letters(text).items():
        print(f"The '{k}' character as found {v} times")
    print("--- End report ---")

report(file_content)
    