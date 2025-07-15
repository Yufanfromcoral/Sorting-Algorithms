def bubble_sort(input_list: list) -> list:
    """
    Sorts a list via bubble sort algorithm
    """
    for n in range(len(input_list)):
        for index in range(len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                temp = input_list[index]
                input_list[index] = input_list[index + 1]
                input_list[index + 1] = temp    
    return input_list



def bubble_sort2(input_list):
    """
    Sorts a list using the bubble sort algorithm
    """
    for i in range(len(input_list)):
        for j in range(len(input_list) -  1):
            if input_list[j] > input_list[j + 1]:
                smaller_element = input_list[j + 1]
                input_list[j + 1] = input_list[j]
                input_list[j] = smaller_element
    return input_list


lst = [2,4,5,54,4,23,2,7,7,6,3,3,4,6,6,7,8,3,2,1,11,1,43,6,9,95,436,3,3,3,5,68,79,8,7,3]

print(bubble_sort(lst))

print(bubble_sort2(lst))