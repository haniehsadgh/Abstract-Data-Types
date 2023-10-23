class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
        self.before = None

    def __repr__(self):
        return str(self.contents)

    def addAfter(self, contents):
        new = DLLN(contents)
        if self.next is not None:
            next = self.next
            next.before = new
        new.next = self.next
        new.before = self
        self.next = new
        return new


    def addBefore(self, contents):
        new = DLLN(contents)
        if self.before is not None:
            before = self.before
            before.next = new
        new.before = self.before
        self.before = new
        new.next = self
        return new

    def toList(self):
        ans = []
        current = self
        while current is not None:
            ans.append(current.contents)
            current = current.next
        return ans
    
            
    def findLast(self):
        current = self
        while current is not None:
            if current.next is not None:
                current = current.next
            else:
                return current

    def findFirst(self):
        current = self
        while current is not None:
            if current.before is not None:
                current = current.before
            else:
                return current

    def findAfter(self, needle):
        current = self
        while current.next is not None:
            if current.next.contents == needle:
                return current.next
            else:
                current = current.next
        raise KeyError(needle)

    def findBefore(self, needle):
        current = self
        while current.before is not None:
            if current.before.contents == needle:
                return current.before
            else:
                current = current.before
        raise KeyError(needle)


def main():
    one = DLLN("one")
    two = one.addAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().addAfter('five')
    print("should be one two five:", one.toList())

    three = two.addAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.addBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').addBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)

    print("should fail to find two:")
    try:
        print(two.findBefore('two'))
    except KeyError as ke:
        print("KEY ERROR", ke)


if __name__ == "__main__":
    main()