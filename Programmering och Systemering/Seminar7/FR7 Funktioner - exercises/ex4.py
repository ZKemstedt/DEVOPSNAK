# # Funktionen sort som tar emot en list (unsorted_list):
#     p = ett element i unsorted_list
#     for element in unsorted_list (except p):
#         if element <= p:
#             put lägg element i en list (smaller)
#         else:
#             lägg elementet i en list (larger)
#     if smaller innehåller mer än ett tal:
#         sort(smaller)
#     if larger innehåller mer än ett tal:
#         sort(larger)
#     sorted_list ´list som innehåller smaller -> p -> larger
#     return sorted_list

def sort(unsorted: list) -> list:
    p = unsorted.pop()
    smaller = []
    larger = []
    for value in unsorted:
        if value <= p:
            smaller.append(value)
        else:
            larger.append(value)
    if len(smaller) > 1:
        smaller = sort(smaller)
    if len(larger) > 1:
        larger = sort(larger)

    return smaller + [p] + larger


print(sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
