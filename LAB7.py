arr1 = [11,4,7,5,10,9,13,1] #bubblesort
arr2 = [11,4,7,5,10,9,13,1] #selectionsort
arr3 = [11,4,7,5,10,9,13,1] #insertionsort
len_arr = len(arr1)

def bubble_sort(arr,len_arr):
    x = 0
    while x < len_arr*len_arr :
        for i in range(0,len_arr-1):
            if arr1[i] < arr1[i+1]:
                x += 1
            elif arr[i] > arr1[i+1]:
                arr1[i],arr1[i+1] = arr[i+1],arr[i]
                x += 1
            else:
                print("ERROR")

def trade(i, j, arr2):
    if i != j:
        temp = arr2[j]
        arr2[j] = arr2[i]
        arr2[i] = temp

def selection_Sort(arr2):
    for i in range(0, len_arr):
        small = i
        for j in range(i+1, len_arr):
            if arr2[j] < arr2[small]:
                small = j
        trade(i, small, arr2)

def insertion_Sort(arr3):
    for index in range(1, len_arr):
        now = arr3[index]
        now2 = index
        while now2 > 0 and arr3[now2 - 1] > now:
            arr3[now2] = arr3[now2 - 1]
            now2 = now2 - 1
        arr3[now2] = now

print("array :",arr1)
bubble_sort(arr1,len_arr)
print("Bubble sort :",arr1)
print("\n")
print("array :",arr2)
selection_Sort(arr2)
print("Selection sort :",arr2)
print("\n")
print("array :",arr3)
insertion_Sort(arr3)
print("Insertion sort :",arr3)