import time 
def cocktailShakerSort(data, drawData, timeTick):
    n = len(data)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                drawData(data, ['#FF0000' if x == i or x == i + 1 else '#00FF00' for x in range(len(data))])
                time.sleep(timeTick)

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                drawData(data, ['#FF0000' if x == i or x == i + 1 else '#00FF00' for x in range(len(data))])
                time.sleep(timeTick)

        start += 1
