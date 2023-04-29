import sys

def binary_search(arr, x, left, right):
    if right <= left:
        return -2
    mid = (left + right) // 2
    mid_value = int(arr[mid])
    mid_value_prev = int(arr[mid-1])
    if mid_value >= x and mid == 0:
        return mid
    elif mid_value >= x and mid_value_prev < x:
        return mid
    elif mid_value >= x and mid_value_prev >= x:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid+1, right)


def main() -> None:
    n_days = int(sys.stdin.readline().rstrip())
    price_list = sys.stdin.readline().rstrip().split()
    # price_list = [int(i) for i in price_list]
    bike_price = int(sys.stdin.readline().rstrip())
    
    index = binary_search(price_list, bike_price, 0, n_days) + 1
    index_2 = binary_search(price_list, bike_price * 2, 0, n_days) + 1
    print(index, index_2)
        


if __name__ == '__main__':
    main()
