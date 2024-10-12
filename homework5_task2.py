#Homework5 task2
"""
Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. 
Написана функція для двійкового пошуку повинна повертати кортеж, де першим
елементом є кількість ітерацій, потрібних для знаходження елемента. 
Другим елементом має бути "верхня межа" — це найменший елемент, який є 
більшим або рівним заданому значенню.
"""

def binary_search(array: list, target: float):
    left = 0  # Ліва межа масиву
    right = len(array) - 1  # Права межа масиву
    count = 0
    high = 0.0

    while left <= right:
        mid = (left + right) // 2  # Знаходимо середину масиву
        print(f"left: {left},\t "
              f"right: {right},\t "
              f"mid: {mid},\t "
              f"target: {target},\t "
              f"arr_mid: {array[mid]},\n"
              f"arr: {array[left:right]}")


        if array[mid] == target:
            count += 1    
            return (count, array[mid])  # Якщо знайдено шуканий елемент, повертаємо його каутн ітерацій та елемент
        elif array[mid] < target:
            left = mid + 1  # Якщо шуканий елемент більший, зміщуємо ліву межу
        else:
            right = mid - 1  # Якщо шуканий елемент менший, зміщуємо праву межу
        
        count += 1

    return (count, array[left])  # Повертаємо верхню межу, якщо елемент не знайдено

# Приклад використання
array = [2.2, 5.5, 8.555, 12.12, 16.111, 23.111, 38.12, 56.15, 72.16, 91.16]
target = 23.111
result = binary_search(array, target)
print(f"Елемент {target} або верхня межа знайдено за {result[0]} ітерацій. Верхня межа {result[1]}")

target = 23
result = binary_search(array, target)
print(f"Елемент {target} або верхня межа знайдено за {result[0]} ітерацій. Верхня межа {result[1]}")

target = 16.2
result = binary_search(array, target)
print(f"Елемент {target} або верхня межа знайдено за {result[0]} ітерацій. Верхня межа {result[1]}")