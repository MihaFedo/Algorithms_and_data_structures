import sys
import math
from typing import Tuple

def input_data() -> Tuple[int, list]:
    n = int(sys.stdin.readline().rstrip())
    lands = sys.stdin.readline().rstrip().split()
    lands_without_houses = [i for (i, elem) in enumerate(lands) if elem == '0']
    return n, lands_without_houses 

def dist_between_zero(count: int) -> list:
    center = math.ceil((count-1)/2)
    dist_between_zero = []
    for i in range(count):
        if i < center:
            dist_between_zero.append(i)
        elif i == center:
            dist_between_zero.append(center)
        else:
            dist_between_zero.append(count-i)
    return dist_between_zero
    
def dist_before_first_zero(first_zero_index: int) -> list:
    return [i for i in range(first_zero_index, 0, -1)]
    
def dist_after_last_zero(last_zero_index: int, n: int) -> list:
    return [i for i in range(n - last_zero_index)]

def result_list(n: int, lands_without_houses: list) -> list:
    result_list = []
    length = len(lands_without_houses)
    for i in range(length - 1):
        res = dist_between_zero(lands_without_houses[i+1]
                                - lands_without_houses[i])
        result_list.extend(res)
    result_list = (dist_before_first_zero(lands_without_houses[0])
                   + result_list
                   + dist_after_last_zero(lands_without_houses[length - 1], n))
    return result_list
    

def main() -> None:
    n, lands_without_houses = input_data()
    result = result_list(n, lands_without_houses)
    print(*result)


if __name__ == '__main__':
    main()