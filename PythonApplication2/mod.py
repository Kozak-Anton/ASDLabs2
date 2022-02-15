import random

def inputConfig():
    size=input("Input array size: ")
    while not size.isdigit() or int(size)<=0:
        size=input("Incorect input, try again: ")
    size=int(size)

    sort=input("Input sorting algorithm (Input 'b' - for bubble sort, 'c' - for comb sort): ")
    while sort!="c" and sort!="b":
        sort=input("Incorect input, try again: ")

    gen=input("Input generation method(Input 'i' - for increasing order, 'd' - for decreasing order, 'r' - for random generation): ")

    while True:
        if gen=="i" or gen=="d" or gen=="r":
             break
        gen=input("Incorect input, try again: ")
    
    return size, sort, gen
    


def increaseArray(size):
    return list(range(1, size+1))

def decreaseArray(size):
    temp=list(range(1, size+1))
    temp.reverse()
    return temp

def randomArray(size):
    return random.sample(range(1, size+1), size)

def printArray(arr, size):
    if size>=10:
        for i in range(10):
            print(arr[i], " ", end="")
    else:
        for i in range(size):
            print(arr[i], " ", end="")

def bubbleSort(arr, size):
    compares=0
    swaps=0
    swapped = True
    while swapped:
        swapped = False
        for i in range(size-1):
            compares+=1
            if arr[i]>arr[i+1]:
                swaps+=1
                arr[i], arr[i+1]=arr[i+1], arr[i]
                swapped = True
    return compares, swaps

def combSort(arr, size):
    compares=0
    swaps=0
    gap=size
    sorted = False
    shrink = 1.3
    while not sorted:
        gap = int(gap//shrink)
        if gap<=1:
            gap=1
            sorted = True

        for i in range(size-gap):
            compares+=1
            if arr[i]>arr[i+gap]:
                swaps+=1
                arr[i], arr[i+gap]=arr[i+gap], arr[i]
                sorted = False
    return compares, swaps



