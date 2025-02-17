def countingSort(data, drawData, timeTick):
    max_val = max(data)
    m = max_val + 1
    count = [0] * m
                
    for a in data:
        count[a] += 1           
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            data[i] = a
            i += 1
            drawData(data, ['#FF0000' if x == i else '#00FF00' for x in range(len(data))])
            time.sleep(timeTick)