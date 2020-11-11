def sort_recipe(list_element):
 return list_element[1], list_element[2]

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort.sort(key=sort_recipe, reverse=False)
print("Posortowana lista nr 1:")
print(list_to_sort, "\n")

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
list_to_sort_2.sort(key=sort_recipe, reverse=False)
print("Posortowana lista nr 2:")
print(list_to_sort_2, "\n")

"""
Wersja 2 przy użyciu sorted
"""

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
print("Posortowana lista nr 1:")
print(sorted(list_to_sort, key=lambda list_element: (list_element[1], list_element[2])), "\n")

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
print("Posortowana lista nr 2:")
print(sorted(list_to_sort_2, key=lambda list_element: (list_element[1], list_element[2])), "\n")
