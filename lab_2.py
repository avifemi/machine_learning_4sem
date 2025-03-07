print("введите номер задания")
number_task=int(input())
match number_task:
    case 1:
        print("введите список элементов")
        user_list=input().split()
        unique_user_list=set(user_list)
        print("список уникальных элементов:", unique_user_list)
    case 2:
        print("введите список элементов")
        user_list = input().split()
        ch, nch = 0, 0
        user_list_int = [int(char) for char in user_list]
        for i in range(len(user_list_int)):
            if user_list_int[i]%2==0:
                ch+=1
            else:
                nch+=1
        print("кол-во четных элементов списка = ", ch)
        print("кол-во нечетных элементов списка = ", nch)
    case 3:
        print("введите список элементов")
        user_list = input().split()
        user_list_int = [int(char) for char in user_list]
        def most_freq(list):
            freq = {}
            for item in list:
                freq[item] = freq.get(item, 0) + 1
            return max(freq, key=freq.get)

        print("самый частый элемент списка:", most_freq(user_list_int))
    case 4:
        print("введите первый список")
        user_list1 = input().split()
        user_list1_int = [int(char) for char in user_list1]
        print("введите второй список")
        user_list2 = input().split()
        user_list2_int = [int(char) for char in user_list2]
        common_elements = list(set(user_list1_int) & set(user_list2_int))
        print("общие элементы двух списков:", common_elements)
    case 5:
        print("введите список элементов")
        user_list = input().split()
        user_list_int = [int(char) for char in user_list]
        common_elements = list(set(user_list_int))
        print("список без дубликатов:", common_elements)
    case 6:
        print("введите список слов")
        user_list = input().split()
        def palindromes(words):
            return [word for word in words if word == word[::-1]]
        print("список палиндромов:", palindromes(user_list))
    case 7:
        print("сколько кортежей хотите ввести?")
        num = int(input())
        tuples = []
        for i in range(num):
            a, b = input("введите два элемента через пробел:").split()
            tuples.append((a, b))
        sorted_tuples = sorted(tuples, key=lambda x: x[1])
        print("отсортированный кортеж по второму элементу:", sorted_tuples)
    case 8:
        import ast # для преобразования строки в словарь
        print("введите кол-во словарей")
        num = int(input())
        dicts = []
        for i in range(num):
            print("введите содержимое словаря в формате: {'a': 1, 'b': 2}")
            user_input = input()
            parsed_dict = ast.literal_eval(user_input) # строка в словарь
            if isinstance(parsed_dict, dict):
                dicts.append(parsed_dict)  # добавляем в список
        merged_dict = {}
        for j in dicts:
            merged_dict.update(j)
        print("объединенные словари", merged_dict)
    case 9:
        print("введите текст")
        text = input()
        def count_word_freq(text):
            words = text.lower().split() # делим текст на слова и приводим к нижнему регистру
            word_count = {}
            for word in words: # считаем слова
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            return word_count
        print("словарь", count_word_freq(text))



