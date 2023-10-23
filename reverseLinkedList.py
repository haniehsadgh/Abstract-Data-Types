from linkedList import LLN


def reverse(lln):
    before = None
    while lln is not None:
        next = lln.next
        lln.next = before
        before = lln
        lln = next
    lln = before
    return lln
    


def main():
    first = LLN("one")
    second = first.addAfter("two")
    third = first.findLast().addAfter("three")
    fourth = first.findLast().addAfter("four")

    print("before we reverse the list, starting at first:", first.toList())
    newBegin = reverse(first)
    print("now that we have reversed, the list from first is very short: ", first.toList())
    print("but the list from the new beginning is longer:", newBegin.toList())
    print("and since newBegin is fourth, here it is again:", fourth.toList())

    ### Here's the output:
    """
    before we reverse the list, starting at first: ['one', 'two', 'three', 'four']
    now that we have reversed, the list from first is very short:  ['one']
    but the list from the new beginning is longer: ['four', 'three', 'two', 'one']
    and since newBegin is fourth, here it is again: ['four', 'three', 'two', 'one']
    """


if __name__ == "__main__":
    main()