# MERGE SORT DAA
#SORTHING TECNIQUE
print(">>> MERGE SORT")
print("Basically sorting an array using MERGE SORT")
print("""soting the below array using merge sort
       arr = [12,11,13,5,6,7] """)
print("")#...space
def merge_sort(arr):
    if len (arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half , right_half)

def merge (left,right):
    merged = []
    left_index,right_index = 0 , 0


    while left_index < len(left)and right_index < len(right):
        if left [left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1

        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len (right):
        merged.append(right[right_index])
        right_index += 1

    return merged

arr = [12,11,13,5,6,7]
sorted_arr = merge_sort(arr)
print ("--- Sorted array:", sorted_arr)
