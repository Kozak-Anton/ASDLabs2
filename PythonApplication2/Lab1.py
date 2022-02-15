import mod

size, sort, gen = mod.inputConfig()

if gen == "i":
    arr=mod.increaseArray(size)
elif gen == "d":
    arr=mod.decreaseArray(size)
else:
    arr=mod.randomArray(size)

print("\nUp to first 10 numbers of initial array: ")
mod.printArray(arr, size)
if sort=="b":
    compares, swaps = mod.bubbleSort(arr, size)
else:
    compares, swaps = mod.combSort(arr, size)

print("\nUp to first 10 numbers of sorted array: ")
mod.printArray(arr, size)
print("\n\nTotal number of compares:", compares, "Total number of swaps:", swaps)