import sys

def is_correct_bracket_seq(skob):
    circle = []
    square = []
    figure = []
    for i in range(len(skob)):
        if skob[i] == '(':
            circle.append(skob[i])
        elif skob[i] == '[':
            square.append(skob[i])
        elif skob[i] == '{':
            figure.append(skob[i])
        elif skob[i] == '(':
            circle.append(skob[i])
        elif skob[i] == ')' and i>0 and (skob[i-1] != '{' and skob[i-1] != '['):
            try:
                circle.pop()
            except:
                return False
        elif skob[i] == ']' and i>0 and (skob[i-1] != '{' and skob[i-1] != '('):
            try:
                square.pop()
            except:
                return False
        elif skob[i] == '}' and i>0 and (skob[i-1] != '(' and skob[i-1] != '['):
            try:
                figure.pop()
            except:
                return False
        else:
            return False
    if len(circle) == 0 and len(square) == 0 and len(figure) == 0:
        return True
    else:
        return False
    
def main():
    skob = list(sys.stdin.readline().rstrip())
    print(is_correct_bracket_seq(skob))
    


if __name__ == '__main__':
    main()