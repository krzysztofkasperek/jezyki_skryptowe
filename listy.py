def sort_recipe(list_element):
 return list_element[1], list_element[2]

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort.sort(key=sort_recipe, reverse=True)
print(list_to_sort)