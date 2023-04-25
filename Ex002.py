def raiseToPower (baseNumber, powNumber):
    result = 1
    for i in range(powNumber):
        result = result * baseNumber
    return result

print(raiseToPower(3, 2))