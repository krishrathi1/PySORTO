import time 
def bucketSort(data, drawData, timeTick):
    max_val = max(data)
    size = max_val/len(data)

    buckets = [[] for _ in range(len(data))]
    for i in range(len(data)):
        j = int(data[i]/size)
        if j != len(data):
            buckets[j].append(data[i])
        else:
            buckets[len(data) - 1].append(data[i])

    for i in range(len(data)):
        insertionSort(buckets[i], drawData, timeTick)
        drawData(data, ['#FF0000' if x == i else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)

    result = []
    for i in range(len(data)):
        result = result + buckets[i]

    for i in range(len(data)):
        data[i] = result[i]
        drawData(data, ['#FF0000' if x == i else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)

def insertionSort(bucket, drawData, timeTick):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
