arr = [5, 3, 7, 9, 2, 5, 2, 6]

min = arr[0]

for i in arr:
    if i+1 < min:
        min = arr[i+1] 
print(min)
