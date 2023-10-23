class LLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None

    def __repr__(self):
        return str(self.contents)

    def addAfter(self, contents):
        new = LLN(contents)
        if self.next is not None:
            jump = self.next
            new.next = jump
        self.next = new
        return new

    def toList(self):
        ans = []
        current = self
        while current is not None:
            ans.append(current.contents)
            # ans.append(current.next)
            current = current.next
        return ans

    def findAfter(self, needle):
        if self.next.contents == needle:
            return self.next
        else:
            raise KeyError(needle)


    def findLast(self):
        current = self
        while current is not None:
            if current.next is not None:
                current = current.next
            else:
                return current


def main():
    print("\n** init and repr **")
    first = LLN("alice")
    print("first should have a repr() (or a str()) so that it can be printed:", first)
    second = first.addAfter("bob")
    print("now second should exist too:", second)

    print("\n** toList **")
    print("I'd like to be able to print them out in a normal list")
    print("Everything starting from second:", second.toList())
    print("But starting from first:", first.toList())

    print("\n** more checking of longer LinkedLists **")
    third = second.addAfter("dog")
    print("the whole thing after adding dog at the end:", first.toList())
    print("starting at second:", second.toList())
    print("starting at third:", third.toList())

    print("\n** findLast **")
    print("this should get the dog (which is last): ", first.findLast())

    print("\n** inserting works in the middle **")
    twopointfive = second.addAfter("cat")
    print("I added a cat after bob, it should appear before the dog:", first.toList())

    print("\n** findAfter **")
    print("I can find bob after the alice:", first.findAfter("bob"))
    print("But if I try to find alice after bob, I get an exception")
    try:
        print(second.findAfter("alice"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("Similarly I cannot find cat AFTER cat, I get an exception")
    try:
        print(twopointfive.findAfter("cat"))
    except KeyError as ke:
        print("KEY ERROR", ke)
    print("But the dog is after the cat, that's fine:", twopointfive.findAfter("dog"))

    ### This whole main() function has this output, for me:
    """
    ** init and repr **
    first should have a repr() (or a str()) so that it can be printed: LLN(alice)
    now second should exist too: LLN(bob)
    ** toList **
    I'd like to be able to print them out in a normal list
    Everything starting from second: ['bob']
    But starting from first: ['alice', 'bob']
    
    ** more checking of longer LinkedLists **
    the whole thing after adding dog at the end: ['alice', 'bob', 'dog']
    starting at second: ['bob', 'dog']
    starting at third: ['dog']
    ** findLast **
    this should get the dog (which is last):  LLN(dog)
    ** inserting works in the middle **
    I added a cat after bob, it should appear before the dog: ['alice', 'bob', 'cat', 'dog']
    ** findAfter **
    I can find bob after the alice: LLN(bob)
    But if I try to find alice after bob, I get an exception
    KEY ERROR 'alice'
    Similarly I cannot find cat AFTER cat, I get an exception
    KEY ERROR 'cat'
    But the dog is after the cat, that's fine: LLN(dog)    
    """


if __name__ == "__main__":
    main()