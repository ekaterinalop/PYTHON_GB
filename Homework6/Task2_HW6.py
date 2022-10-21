# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
#  список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:  [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

import collections

lst = [1, 2, 3, 5, 1, 5, 3, 10]


def no_duplicates1(nums):
    unique_lst = []
    unique_numbers = set(nums)

    for i in unique_numbers:
        unique_lst.append(i)

    return unique_lst

# 2 вариант решения как уникальные элементы оставить только


def no_duplicates2(nums):
    unique_lst = list(collections.Counter(nums))
    return unique_lst


def unique(nums):
    copy = nums[:]
    copy.sort()
    unique_items = []

    for i in range(1, len(copy)):
        if copy[i] != copy[i-1]:
            unique_items.append(copy[i-1])

    return unique_items


def repeat(nums):
    duplicates = [item for item, count in collections.Counter(
        nums).items() if count > 1]
    return duplicates


print(f'список {lst}\nуникальные элементы {unique(lst)}\nсписок повторяемых {repeat(lst)}\nбез дубликатов {no_duplicates2(lst)}')
