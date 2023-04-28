import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        res = 0
        print(res)
    else:
        res = ''
        while n > 0:
            remainder = n % 2
            res = str(remainder) + res
            n = n // 2
        print(int(res))


if __name__ == '__main__':
    main()