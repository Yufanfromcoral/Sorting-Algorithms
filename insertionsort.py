def insertion_sort(inputlist):
    """
    Sorts a list via insertion sort algorithm
    """
    #Assume first element is sorted
    for i in range(len(inputlist)):
    
        target = inputlist[i]
        j = i - 1
        while j > 0 and inputlist[j] > target:
            inputlist[j + 1] = inputlist[j]
            j = j - 1

        inputlist[j + 1] = target
                
    
    return inputlist
                
            
def insertion_sort2(input_list):
    """
    Returns a sorted list sorted using the insertion sort algorithm
    """
    #assume that the first element is sorted
    next_ = input_list[0]
    for i in range(1, len(input_list)):
        target = input_list[i]
        j = i - 1
        while j > 0 and input_list[j] > target:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j] = target
    return input_list

lst = [1, 3, 2, 50, 22, 2, 12,312,3,12,42, 523,412,4321,41,341]
# print(lst)
print(insertion_sort(lst))
print(insertion_sort2(lst))                                                                             