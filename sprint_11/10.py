import sys
import math

def main():
    n = int(sys.stdin.readline().rstrip())
    if round(math.log(n) % math.log(4), 10) == 0:
        print(True)
    else:
        print(False)

    


if __name__ == '__main__':
    main()