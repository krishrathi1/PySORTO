import time 
def countingSort(data, exp, drawData, timeTick):
    n = len(data)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data[i] // exp
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        data[i] = output[i]
        drawData(data, ['#FF0000' if x == i else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)

def radixSort(data, drawData, timeTick):
    max1 = max(data)
    exp = 1
    while max1 // exp > 0:
        countingSort(data, exp, drawData, timeTick)
        exp *= 10
