import heapq
def maintain_median(filename):
    file = open(filename,'r')
    raw_data = file.readlines()
    h_low = []
    h_high = []
    total_sum = 0
    for data in raw_data:
        numb = int(data.strip().split("\n")[0])
        if not h_low or -h_low[0]>numb:
            heapq.heappush(h_low,-numb)
        else:
            heapq.heappush(h_high,numb)
        if len(h_low)>=len(h_high):
            heapq.heappush(h_high,-heapq.heappop(h_low))
        else:
            heapq.heappush(h_low,-heapq.heappop(h_high))
        if len(h_low) >= len(h_high):
            median = -h_low[0]
            print(median)
        else:
            median = h_high[0]
        total_sum+=median
    return total_sum%10000
print(maintain_median('Median.txt'))
