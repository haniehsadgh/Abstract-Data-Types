def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)

def merge(left, right):
    ans = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            ans.append(left[left_index])
            left_index +=1
        else:
            ans.append(right[right_index])
            right_index += 1
    ans += left[left_index:]
    ans += right[right_index:]

    return ans

def merge_sort(seq):
    if len(seq) <= 1:
        return
    mid = len(seq) //2
    left = seq[:mid]
    right = seq[mid:]

    merge_sort(left)
    merge_sort(right)

    seq[:] = merge(left, right)

# def mergesort():
    pass