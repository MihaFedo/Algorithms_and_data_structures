import sys

def input_data():
    n = int(sys.stdin.readline().rstrip())
    input_list = []
    for i in range(n):
        input_str = sys.stdin.readline().rstrip().split()
        input_str = [int(i) for i in input_str]
        input_list.append(input_str)
    input_list.sort()
    return n, input_list


def flowers(n, sort_arr):
    #res = []
    for i in range(n-1):
        if sort_arr[i][1] >= sort_arr[i+1][0]:
            if sort_arr[i][1] <= sort_arr[i+1][1]:
                sort_arr[i+1][0] = sort_arr[i][0]
            else:
                sort_arr[i+1][0] = sort_arr[i][0]
                sort_arr[i+1][1] = sort_arr[i][1]
        else:
            #res.append([sort_arr[i][0], sort_arr[i][1]])
            print(sort_arr[i][0], sort_arr[i][1])
    print(sort_arr[n-1][0], sort_arr[n-1][1])
    #res.append([sort_arr[n-1][0], sort_arr[n-1][1]])
    #return res


def main():
    n, input_list = input_data()
    
    #print(n, input_list)
    #print(merge_sort(input_list))
    #print(flowers(n, merge_sort(input_list)))
    flowers(n, input_list)

if __name__ == '__main__':
    main()