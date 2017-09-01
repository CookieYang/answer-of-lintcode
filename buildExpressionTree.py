class ExpressionTreeNode:
    def __init__(self,symbol):
        self.symbol = symbol
        self.left, self.right = None, None


def build(expression):

    def isHigher(op1,op2):
        if op1 == '(':
            return True
        elif op1 == '+' or op1 == '-':
            if op2 == '+' or op2 == '-' or op2 == '*' or op2 == '/':
                return True
            else:
                return False
        else:
            if op2 == '*' or op2 == '/':
                return True
            else:
                return False


    def convertMiddleToTrail(middle):
        trail = []
        stack = []
        for i in range(len(middle)):
            if middle[i].isdigit():
                trail.append(middle[i])
            elif len(stack) == 0:
                stack.append(middle[i])
            elif middle[i] == '(':
                stack.append(middle[i])
            elif middle[i] == ')':
                char = stack.pop()
                while char != '(' and len(stack) != 0:
                    trail.append(char)
                    char = stack.pop()
            else:
                char = stack[len(stack) - 1]
                while isHigher(middle[i] , char) and len(stack) != 0:
                    if char != '(':
                        trail.append(char)
                    stack.pop()
                    if len(stack) != 0:
                        char = stack[len(stack) - 1]
                stack.append(middle[i])

        while len(stack) != 0:
            c = stack.pop()
            trail.append(c)
        return trail

    newExpression = convertMiddleToTrail(expression)
    nodeStack = []
    if len(newExpression) == 0:
        return None
    for i in range(len(newExpression)):
        if newExpression[i].isdigit():
            nodeStack.append(ExpressionTreeNode(newExpression[i]))
        else:
            right = nodeStack.pop()
            left = nodeStack.pop()
            node = ExpressionTreeNode(newExpression[i])
            node.left = left
            node.right = right
            nodeStack.append(node)
    return nodeStack[0]

build(["(","(","(","(","(",")",")",")",")",")"])

