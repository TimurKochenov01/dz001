def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

numbers = [4, 2, 5, 1, 9, 7, 2]
target = 7

result = linear_search(numbers, target)
if result != -1:
    print(f"Элемент {target} найден на позиции {result}")
else:
    print(f"Элемент {target} не найден в списке")