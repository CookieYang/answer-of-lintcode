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
            depth += 1
        elif s[depth] == '[':
            depth += 1
            tmp = helpExpression(s, depth)
            depth += len(tmp) + 1
            while repeat >= 1:
                result = result + tmp
                repeat -= 1
        elif s[depth].isalpha():
            result = result + s[depth]
            depth += 1
        else:
            depth += 1
            return  result
    return result

print(expressionExpand('3[2[ad]3[pf]]xyz'))