'''
Створити text.txt файл в каталозі з файлом ДЗ. Заповнити його текстом, що розміщений за цим посиланням
Створити програму, яка запитує у користувача назву файла. Якщо такий файл існує - читає вміст, та виводить його в
термінал. Якщо ж ні - виводить інформацію, що файла не існує
Якщо файл відкрився - програма запитує у користувача, що зробити з файлом. Можливі наступні опції:
Прочитати останні 10 строк (read_last_10_lines)
Прочитати перші 10 строк (read_first_10_lines)
Прочитати весь файл (read_all_file)
Знайти найбільше (найдовше) слово у файлі (find_longest_word)
Вивести кількість строк (lines_number)
Вийти з програми (exit)
Якщо користувач опцію, яка не передбачена вище - запитуємо в нього ще раз
Додати опцію words_frequency, яка виводить число повторень кожного слова в коді
'''

import os


file_input = input("Enter file name to open: ")

if os.path.exists(file_input):

    file = open(file_input, mode="r", encoding="UTF-8")

    def reading_func(data):
        reading_content = data.read()
        file.seek(0)
        return reading_content

    def number_of_lines(data):
        all_lines = data.readlines()
        some_len = len(all_lines)
        file.seek(0)
        return some_len

    def from_str_to_list(data):
        string = data.read()
        my_list = string.replace('.', ' ').replace(',', ' ').replace('...', ' ').replace('\"', ' ').split()
        file.seek(0)
        return my_list


    reading = reading_func(file)
    print(reading)

    options = "[read_last_10_lines/read_first_10_lines/read_all_file/find_longest_word/lines_number/words_frequency/" \
              "exit/]"

    while True:
        decision = input(f"What should I do?{options}: ")

        if decision == "read_last_10_lines":
            len_list = number_of_lines(file)
            last_10_lines = file.readlines()[len_list-10:]
            print(last_10_lines)
            file.seek(0)

        elif decision == "read_first_10_lines":
            first_10_lines = file.readlines()[:10]
            print(first_10_lines)
            file.seek(0)

        elif decision == "read_all_file":
            read_all_file = reading_func(file)
            print(read_all_file)

        elif decision == "find_longest_word":
            text = from_str_to_list(file)
            longest = ""
            for word in text:
                if len(word) > len(longest):
                    longest = word
            print(f"The longest word is    {longest}")
            file.seek(0)

        elif decision == "lines_number":
            lines_number = number_of_lines(file)
            print(f"{lines_number} lines in the text")
            file.seek(0)

        elif decision == "words_frequency":
            search_area = from_str_to_list(file)
            frequency = {}
            for i in search_area:
                if i in frequency:
                    frequency[i] += 1
                else:
                    frequency[i] = 1
            for key, value in frequency.items():
                print("The element {0} occurs {1} times".format(key, value))

        elif decision == "exit":
            print("Exiting...")
            file.close()
            break

        else:
            print(f"Please use allowed options! {options}")

else:
    print("The file does not exist")
