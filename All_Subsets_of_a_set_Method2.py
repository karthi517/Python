 printAllSubsets(setOfNumbers):
    totalNumberSets = 2 ** (len(setOfNumbers))
    binarySize = len('{0:b}'.format(totalNumberSets - 1))
    binaryMask = '{0:0' + str(binarySize) + 'b}'
    powers = []
    for index in range(totalNumberSets):
        combination = binaryMask.format(index)
        subSet = []
        for i in range(len(combination)):
            if combination[i] == '1':
                subSet += [setOfNumbers[i]]
        powers.append(subSet)
    return powers

if __name__ == "__main__":
    print(printAllSubsets([1, 2, 3]))
