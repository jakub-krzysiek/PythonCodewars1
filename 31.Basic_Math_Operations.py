def basic_op(operator, value1, value2):
    result = ''
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    elif operator == "/":
        result = value1 / value2
    return result