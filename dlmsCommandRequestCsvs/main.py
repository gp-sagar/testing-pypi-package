def greet():
    return "welcome to polarisgrids ⚜️"

def calculate(a, b, o):
    if o == '+':
        result = a + b
    elif o == '-':
        result = a - b
    elif o == '*':
        result = a * b
    elif o == '/':
        result = a / b
    else:
        return 'Invalid operation'
    
    return f'The Value is :: {result}'

def printbysagar():
    print('Hello')
    return 'Hello ji'