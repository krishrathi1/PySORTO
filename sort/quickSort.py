import time 
def quickSort(data, drawData, timeTick):
    quick_sort(data, 0, len(data) - 1, drawData, timeTick)

def quick_sort(data, low, high, drawData, timeTick):
    if low < high:
        pi = partition(data, low, high, drawData, timeTick)
        quick_sort(data, low, pi - 1, drawData, timeTick)
        quick_sort(data, pi + 1, high, drawData, timeTick)

def partition(data, low, high, drawData, timeTick):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            drawData(data, ['#FF0000' if x == i or x == j else '#00FF00' for x in range(len(data))])
            time.sleep(timeTick)
    data[i + 1], data[high] = data[high], data[i + 1]
    drawData(data, ['#FF0000' if x == i + 1 or x == high else '#00FF00' for x in range(len(data))])
    time.sleep(timeTick)
    return i + 1
