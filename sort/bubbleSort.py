import time


def bubbleSort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                # swap
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
                # draw
                drawData(data, ['#FFB366' if k == j or k == j +
                                1 else "#FF0000" for k in range(len(data))])
                time.sleep(timeTick)
    drawData(data, ["#FFB366" for k in range(len(data))])
