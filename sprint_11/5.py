import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    mas = sys.stdin.readline().rstrip().split()
    if n == 1:
        print(1)
    elif n == 2:
        if int(mas[0]) == int(mas[1]):
            print(0)
        else:
            print(1)
    else:
        res = 0
        mas[0] = int(mas[0])
        mas[1] = int(mas[1])
        mas[n-1] = int(mas[n-1])
        mas[n-2] = int(mas[n-2])
        if mas[0] > mas[1]:
            res += 1
        if mas[n-1] > mas[n-2]:
            res += 1
        for i in range(1,n-1):
            mas[i+1] = int(mas[i+1])
            if mas[i] > mas[i+1] and mas[i] > mas[i-1]:
                res += 1
        print(res)

if __name__ == '__main__':
    main()