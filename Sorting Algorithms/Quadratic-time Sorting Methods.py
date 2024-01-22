
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,i):
            if arr[j] > arr[i]:
                arr[i],arr[j]=arr[j],arr[i]

def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[min_ind],arr[i]=arr[i],arr[min_ind]

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        current=arr[i]
        j=i-1
        while j>=0 and current<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current

if __name__=="__main__":
    arr_1=[2,3,4,4,5,3,2,1,3,4,5,6,9,21,3,2,334,33]
    arr_2=[2,3,4,33,22,2,3,5,6,7,4,3,2,1,-2,-3,-5,2 ,32]
    arr_3=[2,3,4,33,22,11,9,5,6,15,4,3,2,1,24,-3,-5,2 ,32]

    bubble_sort(arr_1)
    selection_sort(arr_2)
    insertion_sort(arr_3)

    print(arr_1)
    print(arr_2)
    print(arr_3)

