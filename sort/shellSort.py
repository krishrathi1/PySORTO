def shellSort(data, drawData, timeTick):
    n = len(data)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
                drawData(data, ['#FF0000' if x == j or x == j + gap else '#00FF00' for x in range(len(data))])
                time.sleep(timeTick)
            data[j] = temp
        gap //= 2
        drawData(data, ['#00FF00' for x in range(len(data))])
        time.sleep(timeTick)