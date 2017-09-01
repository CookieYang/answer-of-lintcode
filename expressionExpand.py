def expressionExpand(s):
   string, a = helpExpression(s)
   return string

def helpExpression(s, depth = 0):
    result = ''
    lenght = 0
    repeat = 0
    if depth == len(s) - 1:
        return  result
    while depth < len(s):
        if s[depth].isdigit():
            repeat = repeat* 10 + int(s[depth])
            depth += 1
            lenght += 1
        elif s[depth] == '[':
            depth += 1
            lenght += 1
            tmp, l = helpExpression(s, depth)
            depth += l
            lenght += l
            while repeat >= 1:
                result = result + tmp
                repeat -= 1
        elif s[depth].isalpha():
            result = result + s[depth]
            depth += 1
            lenght += 1
        else:
            depth += 1
            lenght += 1
            return  result, lenght
    return result, lenght

print(expressionExpand('2[4[ab3[a]]5[6[abc10[a]]xy]uw]k'))