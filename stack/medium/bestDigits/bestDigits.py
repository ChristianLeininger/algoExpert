# copyright 2023
# author: Christian Leininger
# Email: leininic@tf.uni-freiburg.de
# date: 28.06.2023


# O(n) time | O(n) space
def bestDigits(number, numDigits):
    """ Compute the highest number with numDigits

    Args:
        param1(str): number
        param2(int): numDigits
    Return: str with highest number
    """
    # edge case remove no digits
    if numDigits == 0:
        return number
    # edge case remove all digits
    if numDigits >= len(number):
        return ""
    # create a stack
    stack = []
    # loop through the number
    for digit in number:
        # if the stack is empty or
        # the last element is smaller than the current digit
        while len(stack) > 0 and stack[-1] < digit and numDigits > 0:
            # pop the last element
            stack.pop()
            # decrement numDigits
            numDigits -= 1
        # append the current digit
        stack.append(digit)
    # convert the stack to a string
    return "".join(stack[:len(stack) - numDigits])


if __name__ == "__main__":
    number = "462839"
    number = "991199"
    number = "998159"
    numDigits = 2
    print(bestDigits(number, numDigits))
