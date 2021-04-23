def Swap(arr, i , j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
    return arr

def Partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    print("Start Partition with: " ,arr)
    print("Selected Pivot: ", pivot)
    for j in range(l , h):
        if arr[j] <= pivot:
                i = i + 1
                print("Array[",j,"] =" , arr[j] ,  "<= pivot , Swap ", arr[i], " with ", arr[j], "( i: ", i,  " j: ", j , ")")
                arr = Swap(arr, i, j)
        else:
            print("Array[",j,"] >= pivot , Do Nothing ", "( i: ", i,  " j: ", j , ")")

    print("Before Swapping with pivot : ", arr)
    arr = Swap(arr, i+1, h)
    print("After Swapping ", arr[i+1] ," with pivot : ", arr)
    return arr, i+1

def QuickSort(arr, l , h):
    if l < h :
        _, p = Partition(arr, l, h)
        print("After Partition: ", arr)
        print("Doing QS on A[", l , "..." , (p-1), "]")
        QuickSort(arr, l , (p-1))
        print("Doing QS on A[", l , "..." , (p-1), "]")
        QuickSort(arr, p+1 , h)


if __name__ == '__main__':
    arr = [106, 107, 101, 108, 111, 109, 112, 115, 114, 113]
    # arr = [29, 70, 85, 40, 47, 26, 13, 59]
    h = len(arr)-1
    l = 0
    QuickSort(arr, l , h)
    print(arr)

