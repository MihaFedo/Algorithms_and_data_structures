import sys

def input_data():
    a = int(sys.stdin.readline().rstrip())
    input_str = sys.stdin.readline().rstrip().split()
    input_str = [int(i) for i in input_str]
    return a, input_str


def counting_sort(array):
    counted_values = [0, 0, 0]
    for value in array:
        counted_values[value] += 1
    return '0' * counted_values[0] + '1' * counted_values[1] + '2' * counted_values[2]

def main():
    a, input_str = input_data()
    
    print(' '.join(counting_sort(input_str)))

if __name__ == '__main__':
    main()
