"""CPE 202 project 2 Jae Park"""
from queues import QueueArray
from stacks import StackArray


def op_prec(op):
    """gets the precedence of the operator
    Args:
        op(str): operator
    Returns:
        int: precedence of operator

    """
    if op == '+':
        return 3
    elif op == '-':
        return 3
    elif op == '*':
        return 2
    elif op == '/':
        return 2
    elif op == '^':
        return 0
    elif op == '~':
        return 1
    elif op == '(':
        return 10


def infix_to_postfix(infix):
    """turns infix string into postfix string
    Args:
        infix(str): input string
    Returns:
        str: postfix string

    """
    infix_array = infix.split()
    output_queue = QueueArray(20)
    op_stack = StackArray()

    arr_len = len(infix_array)

    for i in range(0, arr_len):
        if infix_array[i] in ('+', '-', '*', '/', '^', '~'):
            while op_stack.num_items != 0 and op_prec(infix_array[i]) >= op_prec(op_stack.peek()):
                output_queue.enqueue(op_stack.pop())
            op_stack.push(infix_array[i])
        elif infix_array[i] == ')':
            while op_stack.num_items != 0 and op_stack.peek() != '(':
                output_queue.enqueue(op_stack.pop())
            op_stack.pop()  # ignore (
        elif infix_array[i] == '(':
            op_stack.push(infix_array[i])
        else:
            output_queue.enqueue(infix_array[i])

    while op_stack.num_items != 0:
        output_queue.enqueue(op_stack.pop())
    temp = [None] * output_queue.num_items
    i = 0
    while not output_queue.is_empty():
        temp[i] = output_queue.dequeue()
        i += 1
    return ' '.join(temp)


def postfix_eval(postfix_str):
    """Evaluates postfix string
    Args:
        postfix_str(str): input string
    Returns:
        float: the evaluated result of the expression

    """
    postfix = postfix_str.split()
    eval_stack = StackArray()
    arr_len = len(postfix)

    for i in range(0, arr_len):
        if postfix[i] not in ('+', '-', '*', '/', '^', '~'):
            eval_stack.push(float(postfix[i]))
        elif postfix[i] == '+':
            second = eval_stack.pop()
            first = eval_stack.pop()

            eval_stack.push(first + second)

        elif postfix[i] == '-':
            second = eval_stack.pop()
            first = eval_stack.pop()

            eval_stack.push(first - second)

        elif postfix[i] == '*':
            second = eval_stack.pop()
            first = eval_stack.pop()

            eval_stack.push(first * second)

        elif postfix[i] == '/':
            second = eval_stack.pop()
            first = eval_stack.pop()

            eval_stack.push(first / second)

        elif postfix[i] == '^':
            second = eval_stack.pop()
            first = eval_stack.pop()

            eval_stack.push(first ** second)

        elif postfix[i] == '~':
            first = -eval_stack.pop()
            eval_stack.push(first)
    return eval_stack.pop()


def postfix_valid(postfix):
    """ Validates postfix string
    Args:
        postfix(str): input string
    Returns: bool

    """
    postfix_arr = postfix.split()
    nums_in_stack = 0

    for i in range(0, len(postfix_arr)):
        if postfix_arr[i] not in ('+', '-', '*', '/', '^', '~'):
            nums_in_stack += 1
        elif postfix_arr[i] in ('+', '-', '*', '/', '^'):
            if nums_in_stack < 2:
                return False
            nums_in_stack -= 1
        elif postfix_arr[i] == '~':
            if nums_in_stack == 0:
                return False
    if nums_in_stack != 1:
        return False
    return True
