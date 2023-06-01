# copyright 2023
# author: Christian Leininger
# Email: leininic @ tf.uni-freiburg.de
# date: 28.05.2023

# time O(n) space O(n)
def balancedBrackets(string: str):
    """ Computes if the brackets are balanced or not in the string
        Use a stack to store the open brackets and pop
        if the close bracket is the same
    Args:
        param1(str): string with brackets

    Return:
        bool: True if balanced else False

    """
    open_brackets = ["[", "(", "{"]
    close_brackets = ["]", ")", "}"]
    stack = []
    for item in string:
        # case stack is empty

        if item not in close_brackets and item not in open_brackets:
            continue
        if len(stack) == 0:
            # its O(1) since its for all n same size
            if item not in open_brackets:
                return False
            else:
                stack.append(item)
                continue
        # case not empty
        if len(stack) > 0:
            if item in open_brackets:
                stack.append(item)
            else:

                if open_brackets[close_brackets.index(item)] == stack[-1]:

                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False
