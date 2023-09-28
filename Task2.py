def find_matching_lines(file_name, search_words):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words_in_line = line.lower().split()
            for word in search_words:
                if word.lower() in words_in_line:
                    yield line.strip()
                    break


file_name = 'your_file.txt'
search_words = ['роза', 'Азора']

for line in find_matching_lines(file_name, search_words):
    print(line)
