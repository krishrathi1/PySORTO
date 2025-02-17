import time 
def heapSort(data, drawData, timeTick):
    n = len(data)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # swap
        heapify(data, i, 0, drawData, timeTick)
        drawData(data, ['#FF0000' if x == i else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)

def heapify(data, n, i, drawData, timeTick):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and data[i] < data[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and data[largest] < data[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap
        drawData(data, ['#FF0000' if x == i or x == largest else '#00FF00' for x in range(len(data))])
        time.sleep(timeTick)
        # Heapify the root.
        heapify(data, n, largest, drawData, timeTick)
