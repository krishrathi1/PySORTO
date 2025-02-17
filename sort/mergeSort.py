import time


def mergeSort(data, drawData, timeTick):
    mergeSortAlgo(data, 0, len(data) - 1, drawData, timeTick)


def mergeSortAlgo(data, left, right, drawData, timeTick):
    if left < right:
        # divide array in half
        middle = (left + right) // 2
        mergeSortAlgo(data, left, middle, drawData, timeTick)
        mergeSortAlgo(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    leftIndex = 0
    rightIndex = 0

    for dataIndex in range(left, right + 1):
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                data[dataIndex] = leftPart[leftIndex]
                leftIndex += 1
            else:
                data[dataIndex] = rightPart[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftPart):
            data[dataIndex] = leftPart[leftIndex]
            leftIndex += 1
        else:
            data[dataIndex] = rightPart[rightIndex]
            rightIndex += 1

    drawData(data, ["green" if x >= left and x <=
                    right else "white" for x in range(len(data))])
    time.sleep(timeTick)


'''
# driver for testing
data = [5, 66, 85, 3, 111, 45, 0]

mergeSort(data, 0, 0)
print(data)
'''


def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray
