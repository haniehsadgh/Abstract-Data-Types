class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        # self.parent = None
        self.children = []
      
    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        # for child in children:
        #     child.parent = self
        self.children.extend(children)
        return children

    def dfs_stack_of_pairs(self):
        ### This is a hint, which you might use or ignore, as you choose
        ans = []
        s = Stack()
        s.push([self, 0])
        while s.isNotEmpty():
            current = s.pop()
            if current[0].contents not in ans:
                ans.append(current[0].contents)
            if len(current[0].children) > current[1]:
                s.push([current[0], current[1] + 1])
                s.push([current[0].children[current[1]], 0])
        return ans
    
    def dfs_todos_badorder(self):
        ### This is a hint, which you might use or ignore, as you choose
        ans = []
        s = Stack()
        s.push(self)
        while s.isNotEmpty():
            current = s.pop()
            if current.contents not in ans:
                ans.append(current.contents)
            for child in current.children:
                s.push(child)
                
        return ans

    def dfs_todos_goodorder(self):
        ans = []
        s = Stack()
        s.push(self)
        while s.isNotEmpty():
            current = s.pop()
            if current.contents not in ans:
                ans.append(current.contents)
            for child in reversed(current.children):
                s.push(child)
        return ans




'''
A tree could look like this:
               Z
           /   |   \ 
        Q      R      S
      / | \   / \   / | \ 
    A   B  C  D E  F  G  H
   / \        |      / \ 
  T   U       W     X   Y
              |
              J
'''

root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren('Q', 'R', 'S')
[A, B, C] = Q.addChildren('A', 'B', 'C')
[D, E] = R.addChildren('D', 'E')
[F, G, H] = S.addChildren('F', 'G', 'H')
[T, U] = A.addChildren('T', 'U')
[W] = D.addChildren('W')
[X, Y] = G.addChildren('X', 'Y')
[J] = W.addChildren('J')

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(' ')
# print("\nDFS should be: [", ', '.join(correct_dfs), "]")
weird_correct_dfs = "Z S H G Y X F R E D W J Q C B A U T".split(' ')
# print("\nweird-order DFS should be: [", ', '.join(weird_correct_dfs), "]")

part1_ans = root1.dfs_stack_of_pairs()
print("\npart 1 goal:   ", correct_dfs)
if part1_ans == correct_dfs:
    print("part 1 successful match")
else:
    print("part 1 actual: ", part1_ans)

part2_ans = root1.dfs_todos_badorder()
print("\npart 2 goal:   ", weird_correct_dfs)
if part2_ans == weird_correct_dfs:
    print("part 2 successful match")
else:
    print("part 2 actual: ", part2_ans)


part3_ans = root1.dfs_todos_goodorder()
print("\npart 3 goal:   ", correct_dfs)
if part3_ans == correct_dfs:
    print("part 3 successful match")
else:
    print("part 3 actual: ", part3_ans)