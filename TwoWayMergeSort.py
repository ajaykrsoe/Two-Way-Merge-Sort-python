import  random as rd

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]


    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def twoWayMergeSort(arr) :
    n=len(arr)
    size=1
    while(size<n)  :
        l=0
        m=size-1
        r=2*size-1
        while(r<n)   :
            merge(arr,l,m,r)
            l = r+1
            m = r+size
            r = r+2 * size
        if(l<=n-1 and m<n-1)  :
            merge(arr,l,m,n-1)

        size*=2

ns=[rd.randint(1,50) for e in range(10)]
l=[ [rd.randint(0,100) for x in range(e)]for e in ns]
for el in l :
    twoWayMergeSort(el)
    print(el)



