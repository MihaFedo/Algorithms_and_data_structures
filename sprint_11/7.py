import sys
import re

def main():
    mas = sys.stdin.readline().rstrip().lower()
    mas = re.sub('\W+','', mas)
    len_string = len(mas)
    if len_string == 1:
        print(True)
    else:
        for i in range(len_string // 2):
            if mas[i] == mas[len_string - 1 - i]:
                res = True
            else:
                res = False
                break
        print(res)


if __name__ == '__main__':
    main()