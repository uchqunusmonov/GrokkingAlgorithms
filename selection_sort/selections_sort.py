def find_smallest(arr: list):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []

    for i in range(len(arr)):
        smallest_element = find_smallest(arr)
        new_arr.append(arr.pop(smallest_element))
    return new_arr

