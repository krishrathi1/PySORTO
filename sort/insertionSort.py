def insertionSort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['#FF0000' if x == j or x == j + 1 else '#00FF00' for x in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key
        drawData(data, ['#FF0000' if x == j + 1 else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)