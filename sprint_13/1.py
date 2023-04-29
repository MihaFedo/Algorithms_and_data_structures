import sys

def gen_binary(n, prefix, t = 0):
    if t < 0:
        prefix = ')' + prefix

    if n == 0 and prefix == '':
        print('')
    elif n == 0 and t == 0 and prefix[0:1] == '(':
        print(prefix)
    elif n == 0 and ((t == 0 and prefix[0:1] == ')') or t != 0):  # 
        prefix = ''
    else:
        gen_binary(n - 1, prefix + '(', t + 1)
        gen_binary(n - 1, prefix + ')', t - 1)

def main() -> None:
    n = int(sys.stdin.readline().rstrip())
    gen_binary(n*2, '')

if __name__ == '__main__':
    main()