def toList(string):
    """
    Converts a string to a list of strings.
    """
    return string.strip().split(" ")

def sumOfStrList(list):
    """
    Sums the values of a list of strings.
    """
    nums = []
    for i in list:
        nums.append(int(i))
    return sum(nums)