import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    mas = []
    for i in range(n):
        mas.append(sys.stdin.readline().rstrip())
    n_cur = int(sys.stdin.readline().rstrip())
    m_cur = int(sys.stdin.readline().rstrip())
    result = []
    if m_cur > 0:
        result.append(int(mas[n_cur].split()[m_cur-1]))
    if m_cur < m-1:
        result.append(int(mas[n_cur].split()[m_cur+1]))
    if n_cur > 0:
        result.append(int(mas[n_cur-1].split()[m_cur]))
    if n_cur < n-1:
        result.append(int(mas[n_cur+1].split()[m_cur]))

    print(*sorted(result))

if __name__ == '__main__':
    main()