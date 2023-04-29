import sys
from typing import Tuple


def input_data() -> Tuple[int, list]:
    n = int(sys.stdin.readline().rstrip())
    input_list = []
    for i in range(n):
        string = sys.stdin.readline().rstrip().split()
        string[0], string[1], string[2] = int(string[1]) * (-1), int(string[2]), string[0]
        input_list.append(string)
    return n, input_list


def partition(array, pivot) -> Tuple[list, list]:
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] < pivot and array[right] > pivot:
            left += 1
            right -= 1
        elif array[left] < pivot and array[right] <= pivot:
            left += 1
        elif array[left] >= pivot and array[right] > pivot:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
    return array[0:left], array[right:len(array)]
        
    
def pivot_choose(array) -> int:
    return array[len(array) // 2]


def effect_sort(sort_list) -> list:
    if len(sort_list) < 2:
        return sort_list
    pivot = pivot_choose(sort_list)
    sort_list_left, sort_list_right = partition(sort_list, pivot)
    return effect_sort(sort_list_left) + effect_sort(sort_list_right)
        


def main() -> None:
    n, input_list = input_data()
    
    result_list = effect_sort(input_list)
    for elem in result_list:
        print(elem[2])
   

if __name__ == '__main__':
    main()
