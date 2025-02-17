def combSort(data, drawData, timeTick):
    n = len(data)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False

        for i in range(n - gap):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                swapped = True
                drawData(data, ['#FF0000' if x == i or x == i + gap else '#00FF00' for x in range(len(data))])
                time.sleep(timeTick)