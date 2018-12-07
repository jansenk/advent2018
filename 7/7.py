import re, string
t = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."
f = open("in.txt")
reqs = [re.match(t, line.strip()).groups() for line in f]

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.parents = set()
        self.children = set()

    def add_parent(self, parent):
        self.parents.add(parent)

    def add_child(self, child):
        self.children.add(child)

    def unused(self):
        return (not self.parents) and (not self.children)

    def __repr__(self):
        return self.letter

class Worker:
    def __init__(self):
        self.letter = None
        self.seconds = 0

    def tick(self):
        if not self.letter:
            return None


nodes = {l: Node(l) for l in string.ascii_uppercase}
def loadNodes():
    for req in reqs:
        step1 = nodes[req[0]]
        step2 = nodes[req[1]]
        step1.add_child(step2)
        step2.add_parent(step1)

loadNodes()
result = ""
s = [node for node in nodes.values() if not node.parents]
while s:
    l_node = s.pop(0)
    result += str(l_node)
    for c_node in l_node.children:
        c_node.parents.remove(l_node)
        if not c_node.parents:
            s.append(c_node)
    s.sort()

print(result)
print(len(result))

loadNodes()
workers = [Worker() for _ in range(5)]
s = [node for node in nodes.values() if not node.parents]
time = 0
result = ""
while len(result) < 26:
    for worker in workers:
