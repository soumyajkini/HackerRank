def countTriplets(arr, r):

    prev = 0
    n = len(arr)
    prev = arr[0]
    count = 1
    totalCount = 0
    print arr
    for num in arr[1:n]:
        if (num == prev * r):
            print (prev, r, num, count, totalCount)
            count += 1
            if count >= 3:
                totalCount += 1
            prev = num
        
    return totalCount
    
ans = countTriplets([1, 2, 2, 4], 2)