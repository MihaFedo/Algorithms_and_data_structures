import sys

NOKIA = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def glue(input_str):
    #print(input_str)
    if input_str == '':
        return ['']
    
    output_str = []
    last_word = NOKIA[input_str[-1]]
    #print(last_word)
    
    for elem in glue(input_str[:-1:]):
        #print(elem)
        for letter in last_word:
            output_str.append(elem + letter)
            #print(output_str)
    return output_str        


def main():
    input_str = sys.stdin.readline().rstrip()
    
    print(' '.join(glue(input_str)))
    


if __name__ == '__main__':
    main()