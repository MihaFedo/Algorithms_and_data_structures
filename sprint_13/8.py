import sys

def input_data():
    n = int(sys.stdin.readline().rstrip())
    input_list = sys.stdin.readline().rstrip().split()
    #input_list = [int(i) for i in input_list]
    return n, input_list


def compare(num_1, num_2):  # функция-компаратор
    if len(num_1) == len(num_2):
        return num_1 < num_2
    var_1 = num_1 + num_2
    var_2 = num_2 + num_1
    return var_1 < var_2

# воспользуемся уже знакомой сортировкой вставками
def sort_by_comparator(n, array, less):
    for i in range(1, n):
        item_to_insert = array[i]
        j = i
    # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert

def main():
    n, input_list = input_data()
    sort_by_comparator(n, input_list, compare)
    print(''.join(input_list[::-1]))

if __name__ == '__main__':
    main()
