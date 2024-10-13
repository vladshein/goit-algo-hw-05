#Homework5 task3
"""
Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, 
Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів 
(стаття 1, стаття 2). Використовуючи timeit, треба виміряти час виконання
кожного алгоритму для двох видів підрядків: одного, що дійсно існує в
тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
На основі отриманих даних визначте найшвидший алгоритм для кожного 
тексту окремо та в цілому.
"""

import timeit

print("Test article 1")
print("==================================")
setup_code1 = '''
# Open the file in read mode
with open('стаття_1.txt', 'r') as file:
# Read the entire file content into a string
    file1_content = file.read()

search_string1 = "Двійковий"
'''

setup_code2 = '''
# Open the file in read mode
with open('стаття_2.txt', 'r', encoding='utf-8') as file:
# Read the entire file content into a string
    file2_content = file.read()

search_string2 = "Визначаються предмети, які буде рекомендовано"
'''

# Пошук по статті 1 реальної строки в тексті
test_code1 = '''
import boyer_moore_search
boyer_moore_search.boyer_moore_search(file1_content, search_string1)
'''

test_code2 = '''
import kmp_search
kmp_search.kmp_search(file1_content, search_string1)
'''

test_code3 = '''
import rabin_karp_search
rabin_karp_search.rabin_karp_search(file1_content, search_string1)
'''

execution_time = timeit.timeit(stmt=test_code1, setup=setup_code1, number=10)
print(f"Execution time of boyer_moore_search in article 1: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code2, setup=setup_code1, number=10)
print(f"Execution time of kmp_search in article 1: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code3, setup=setup_code1, number=10)
print(f"Execution time of rabin_karp_search in article 1: {execution_time} seconds")
print("==================================")


# Пошук по статті 1 відсутньої строки в тексті
setup_code1 = '''
# Open the file in read mode
with open('стаття_1.txt', 'r') as file:
# Read the entire file content into a string
    file1_content = file.read()

search_string1 = "АБАБАГАЛАМАГА АБАБАГАЛАМАГА"
'''
execution_time = timeit.timeit(stmt=test_code1, setup=setup_code1, number=10)
print(f"Execution time boyer_moore_search in article 1 of absent string: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code2, setup=setup_code1, number=10)
print(f"Execution time of kmp_search in article 1 of absent string: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code3, setup=setup_code1, number=10)
print(f"Execution time of rabin_karp_search in article 1 of absent string: {execution_time} seconds")
print("==================================")

print("Test article 2")
print("==================================")
# Пошук по статті 2 реальної строки в тексті
test_code1 = '''
import boyer_moore_search
boyer_moore_search.boyer_moore_search(file2_content, search_string2)
'''

test_code2 = '''
import kmp_search
kmp_search.kmp_search(file2_content, search_string2)
'''

test_code3 = '''
import rabin_karp_search
rabin_karp_search.rabin_karp_search(file2_content, search_string2)
'''

execution_time = timeit.timeit(stmt=test_code1, setup=setup_code2, number=10)
print(f"Execution time of boyer_moore_search in article 2: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code2, setup=setup_code2, number=10)
print(f"Execution time of kmp_search in article 2: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code3, setup=setup_code2, number=10)
print(f"Execution time of rabin_karp_search in article 2: {execution_time} seconds")
print("==================================")



# Пошук по статті 2 відсутньої строки в тексті
setup_code2 = '''
# Open the file in read mode
with open('стаття_2.txt', 'r', encoding='utf-8') as file:
# Read the entire file content into a string
    file2_content = file.read()

search_string2 = "АБАБАГАЛАМАГА АБАБАГАЛАМАГА"
'''

test_code1 = '''
import boyer_moore_search
boyer_moore_search.boyer_moore_search(file2_content, search_string2)
'''

test_code2 = '''
import kmp_search
kmp_search.kmp_search(file2_content, search_string2)
'''

test_code3 = '''
import rabin_karp_search
rabin_karp_search.rabin_karp_search(file2_content, search_string2)
'''

execution_time = timeit.timeit(stmt=test_code1, setup=setup_code2, number=10)
print(f"Execution time of boyer_moore_search in article 2 of absent string: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code2, setup=setup_code2, number=10)
print(f"Execution time of kmp_search in article 2 of absent string: {execution_time} seconds")

execution_time = timeit.timeit(stmt=test_code3, setup=setup_code2, number=10)
print(f"Execution time of rabin_karp_search in article 2 of absent string: {execution_time} seconds")
print("==================================")
