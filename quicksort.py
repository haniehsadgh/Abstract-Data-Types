def partition_naive(seq, pivot):
    ans = [[],[],[]]
    for item in seq:
        if item < pivot:
            ans[0].append(item)
        elif item == pivot:
            ans[1].append(item)
        else:
            ans[2].append(item)
    return ans


def pivot_naive(seq):
    return seq[len(seq)-1]


def quicksort_naive(seq):
    if len(seq) <= 1:
        return seq
    pivot = pivot_naive(seq)
    partition = partition_naive(seq, pivot)

    lesser = quicksort_naive(partition[0])
    greater = quicksort_naive(partition[2])

    seq[:] = lesser + partition[1] +  greater
    return seq


def pivot_upgrade(seq, lo, hi):
    min = (lo + hi) //2
    return seq[min]

def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))

def __quicksort_upgrade(seq, lo, hi):
    if hi - lo <= 1:
        return
    pivot = pivot_upgrade(seq, lo, hi)
    partitions = partition_upgrade(seq, pivot, lo, hi)

    __quicksort_upgrade(seq, 0, lo + partitions[0])
    __quicksort_upgrade(seq, lo + partitions[0]+ partitions[1], hi)

def partition_upgrade(seq, pivot, lo, hi):
    [one, two, three] = partition_naive(seq[lo:hi], pivot)
    seq[lo:hi] = one + two + three
    return [len(one), len(two), len(three)]

# def partition_upgrade(seq, pivot, lo, hi):
    pass        ### TODO