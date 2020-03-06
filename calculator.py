import re

def add(numberString):
    if len(numberString) == 0:
      return 0

    numbers = re.findall(r"-?\d+", numberString)
    result = 0
    negatives = []
    for num in numbers:
        num = int(num)
        if num < 0:
            negatives.append(num)
        if num < 1000:
            result = result + int(num)
    if len(negatives) > 0:
        message = "-numbers not allowed! "
        for i in range(len(negatives)):
            if i != len(negatives)-1:
                message += str(negatives[i]) + ", "
            else:
                message += str(negatives[i]) + "."
        raise Exception(message)

    return result
