def swap(numArray: list[int], pos1: int, pos2: int) -> None:
    temp: int = numArray[pos1]
    numArray[pos1] = numArray[pos2]
    numArray[pos2] = temp

def partition(numArray: list[int], low: int, high: int) -> int:
    pivot: int = numArray[low]
    i: int = low
    j: int = high

    while i < j:
        while numArray[i] <= pivot: i += 1
        while numArray[j] > pivot: j -= 1

        if i < j: swap(numArray, i, j)

    swap(numArray, j, low)
    return j

def QuickSort(numArray: list[int], low: int, high: int) -> None:
    if low < high:
        pivot: int = partition(numArray, low, high)

        QuickSort(numArray, low, pivot - 1)
        QuickSort(numArray, pivot + 1, high)


numArray: list[int] = [4, 6, 2, 5, 7, 9, 1, 3, 61, 23, 66, 24, 44, 21, 89 ,205]
QuickSort(numArray, 0, len(numArray) - 1)
print(numArray)