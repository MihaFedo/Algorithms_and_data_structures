import sys

def input_data():
    a = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    #input_list = list(bytes(sys.stdin.readline().rstrip(), 'ascii'))
    input_list = sys.stdin.readline().rstrip()
    return a, m, input_list

def polinom_mod(a, m, input_list):
    P = 0
    for i in input_list:
        P = ord(i) % m + (P * a) % m
    return P 
    
def main():
    a, m, input_list = input_data()
    
    #print(a, m, input_list)
    print(polinom_mod(a, m, input_list))
    

if __name__ == '__main__':
    main()