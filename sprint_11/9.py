import sys

def max_len(elem_1, elem_2):
    return max(len(elem_1), len(elem_2))

def add_zero(elem_1, elem_2):
    maxlen = max_len(elem_1, elem_2)
    elem_1 = ('0' * (maxlen - len(elem_1) + 1)) + elem_1
    elem_2 = ('0' * (maxlen - len(elem_2) + 1)) + elem_2
    return elem_1, elem_2

def main():
    elem_1 = sys.stdin.readline().rstrip()
    elem_2 = sys.stdin.readline().rstrip()
    elem_1, elem_2 = add_zero(elem_1, elem_2)
    res = ''
    prom = 0
    for i in range(max_len(elem_1, elem_2)-1, -1, -1):
        if elem_1[i] != elem_2[i] and prom == 0:
            res = '1' + res  
            prom = 0
        elif elem_1[i] != elem_2[i] and prom == 1:
            res = '0' + res  
            prom = 1
            
        elif elem_1[i] == elem_2[i] and elem_1[i] == '0' and prom == 0:
            res = '0' + res
            prom = 0
        elif elem_1[i] == elem_2[i] and elem_1[i] == '0' and prom == 1:
            res = '1' + res
            prom = 0
        
        elif elem_1[i] == elem_2[i] and elem_1[i] == '1' and prom == 0:
            res = '0' + res
            prom = 1
        elif elem_1[i] == elem_2[i] and elem_1[i] == '1' and prom == 1:
            res = '1' + res
            prom = 1
    print(int(res))

if __name__ == '__main__':
    main()