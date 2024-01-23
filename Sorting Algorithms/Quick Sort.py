def quick_sort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p + 1, end)
 
 
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1
 
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j
 
 
if __name__=="__main__":
    arr=[2,3,1,2,4,5,3,3,2,-2,-1,3,4,5,11,12,13,14,9]
    quick_sort(arr,0,len(arr)-1)
    print(arr)
