def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        file_words = file_contents.split()
        return str(len(file_words))

def get_num_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read().lower()
    char_count = {}
    for char in file_contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_char_counts(path_to_file):
    char_count = get_num_chars(path_to_file)
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_char_count