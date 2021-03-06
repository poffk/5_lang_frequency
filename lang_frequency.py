import re
from collections import Counter


NUMBER_OF_OUTPUT_WORDS = 10


def load_data(filepath):
    with open(filepath) as data_file:
        return data_file.read()


def get_most_frequent_words(text):
    text = text.lower()
    refined_text = re.findall(r'[^ \W|\d]+', text)
    counter = Counter(refined_text)
    return counter.most_common(NUMBER_OF_OUTPUT_WORDS)


if __name__ == '__main__':
    data = (load_data(input('Введите путь до файла: ')))
    data = get_most_frequent_words(data)
    print(data)