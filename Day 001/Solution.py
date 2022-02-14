def minMaxFinder(numArray: list[int]) -> dict:
    if len(numArray) == 0: return {}

    if len(numArray) == 1: return {
        'min': numArray[0],
        'max': numArray[0]
    }

    currentMin: int = None
    currentMax: int = None

    startingPoint: int = 0
    endingPoint: int = len(numArray) - 1

    while startingPoint <= endingPoint:
        if (currentMax == None) or (currentMax <= numArray[startingPoint]):
            currentMax = numArray[startingPoint]

        if (currentMin == None) or (currentMin >= numArray[startingPoint]):
            currentMin = numArray[startingPoint]

        if startingPoint == endingPoint:
            startingPoint += 1
            endingPoint -= 1
            continue

        if (currentMax == None) or (currentMax <= numArray[endingPoint]):
            currentMax = numArray[endingPoint]

        if (currentMin == None) or (currentMin >= numArray[endingPoint]):
            currentMin = numArray[endingPoint]

        startingPoint += 1
        endingPoint -= 1

    return {
        'min': currentMin,
        'max': currentMax
    }
