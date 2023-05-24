


# time O(n**2) space O(1)
def twoNumberSumNaive(array, targetSum):
    """ find two Numbers that sum up to targetSum 
    Naive solution use two for loops to iterate through the array
    param: array: list of numbers
    param: targetSum: int
    return: list of two numbers that sum up to targetSum
    """
    # edge case if array is empty
    if len(array) == 0:
        return []
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
    

# time O(n) space O(n)
def twoNumberSumDict(array, targetSum):
    """ use the fact that targetSum = firstNum + secondNum 
        so secondNum = targetSum - firstNum
        use a dictionary to store the secondNum and check if it is in the dictionary
        param: array: list of numbers
        param: targetSum: int
        return: list of two numbers that sum up to targetSum
        """
    # edge case if array is empty
    if len(array) == 0:
        return []
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# time O(nlog(n)) space O(1)
def twoNumberSumSort(array, targetSum):
    """ sort the array first value of
    left pointer and right pointer and compare with targetSum to move the pointers
    if numSum > targetSum move right pointer to the left else move left pointer to the right
    until left pointer is greater than right pointer then return empty list 
    
        param: array: list of numbers
        param: targetSum: int
        return: list of two numbers that sum up to targetSum
    """
    # edge case if array is empty
    if len(array) == 0:
        return []
    lelft_pointer = 0
    right_pointer = len(array) - 1
    array.sort()
    while lelft_pointer < right_pointer:
        numSum = array[lelft_pointer] + array[right_pointer]
        if numSum == targetSum:
            return [array[lelft_pointer], array[right_pointer]]
        elif numSum > targetSum:
            right_pointer -= 1
        elif numSum < targetSum:
            lelft_pointer += 1
    return []