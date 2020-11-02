"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
(c) Team Coach


"""

import random
import sys

def generate_new_text(first_word, dict):
    print(first_word)
    if first_word in dict:
        nextWord = random.sample(dict[first_word], 1)[0]
        generate_new_text(nextWord, dict)

def mem_dict(filename):
    word_dict = dict()
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            for i in range(0, len(words) - 1):
                if words[i] in word_dict:
                    word_dict[words[i]].add(words[i + 1].rstrip())
                else:
                    word_dict[words[i]] = {words[i + 1].rstrip()}
    return word_dict

def main():
    if sys.argv[1] != "--file" and len(sys.argv[2]) < 1:
        print('use: [--file] file')
        sys.exit(1)
    
    first_word = "He"#input('Enter first word: ')
    generate_new_text(first_word, mem_dict(sys.argv[2]))

if __name__ == '__main__':
  main()
