# python3
def runningTime(arr):
    z = 0
    if arr == sorted(arr):
        return (0)
    else:
        for i in range(1, len(arr)):
            x = arr[i]
            for j in range(i):
                if arr[j] > x:
                    (arr[i], arr[j]) = (arr[j], arr[i])
                    z += 1

        return z