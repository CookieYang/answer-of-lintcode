def expressionExpand(s):
    return helpExpression(s)

def helpExpression(s, depth = 0):
    result = ''
    repeat = 1
    if depth == len(s):
        return  result
    while depth < len(s):
        if s[depth].isdigit():
            repeat = int(s[depth])
        elif s[depth] == '[':
            result = result + helpExpression(s, depth)
        elif s[depth].isalpha():
            result = result + s[depth]
        else:
            while repeat > 1:
                result += result
                repeat -= 1
            return  result

