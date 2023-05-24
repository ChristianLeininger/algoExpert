


# time O(n**2) space O(1)
def twoNumberSumNaive(array, targetSum):
    """ find two Numbers that sum up to targetSum 
    Naive solution use two for loops to iterate through the array
    param: array: list of numbers
    param: targetSum: int
    return: list of two numbers that sum up to targetSum
    """
    
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
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []