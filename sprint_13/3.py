import sys

def input_data():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    return a, b


def rec(a_1, b_1):
    i, s = 0, 0
    while s < len(a_1) and i < len(b_1):
        if a_1[s] == b_1[i]:
            s += 1
        i += 1        
    return len(a_1) == s

def main():
    a, b = input_data()
    
    print(rec(a, b))

if __name__ == '__main__':
    main()
