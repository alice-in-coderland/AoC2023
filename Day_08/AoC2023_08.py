from math import lcm

test_input1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.splitlines()

test_input2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.splitlines()

test_input3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''.splitlines()

with open('input.txt', 'r') as f:
    documents = f.readlines()
    documents = [x.strip() for x in documents]

# inp = test_input1
# inp = test_input2
inp = documents

instruction = [int(x) for x in list(inp[0].replace('R', '1').replace('L', '0'))]

nodes = {}
for line in inp[2:]:
    node, children = line.split(' = ')
    nodes[node] = children.replace('(', '').replace(')', '').split(', ')


nodes_list = list(nodes.keys())

# Part 1

curr_node = 'AAA'
i = 0
counter = 0
while curr_node!='ZZZ':
    curr_node = nodes[curr_node][instruction[i]]
    i = (i+1)%len(instruction)
    counter += 1

print(f'{counter} steps to ZZZ')

# Part 2

# inp = test_input3
inp = documents

instruction = [int(x) for x in list(inp[0].replace('R', '1').replace('L', '0'))]
# print(instruction)

nodes = {}
for line in inp[2:]:
    node, children = line.split(' = ')
    nodes[node] = children.replace('(', '').replace(')', '').split(', ')

nodes_list = list(nodes.keys())

curr_nodes = [x for x in nodes_list if x.endswith('A')]
i = 0
counters = [0]*len(curr_nodes)
print(counters)
for j in range(len(curr_nodes)):
    counter = 0
    while not curr_nodes[j].endswith('Z'):
        curr_nodes[j] = nodes[curr_nodes[j]][instruction[i]]
        i = (i+1)%len(instruction)
        counter += 1
    counters[j] = counter
print(counters)
print(lcm(*counters))

#%%
