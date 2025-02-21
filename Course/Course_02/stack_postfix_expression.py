def postfix_expression(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    for char in expression.split():
        if char not in operators:
            stack.append(float(char))

        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)

    return stack.pop()

# Example usage
postfix_expr = "5 9 3 + 4 2 * * 7 + *"
result = postfix_expression(postfix_expr)
print(f"Result of postfix expression '{postfix_expr}': {result}")