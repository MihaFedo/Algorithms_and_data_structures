import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    mas = sys.stdin.readline().rstrip().split()
    len_ind_max = [len(mas[0]),0]
    for i in range(1,len(mas)):
        if len(mas[i]) > len_ind_max[0]:
            len_ind_max[0] = len(mas[i])
            len_ind_max[1] = i
    print(mas[len_ind_max[1]])
    print(len_ind_max[0])


if __name__ == '__main__':
    main()