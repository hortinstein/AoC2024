from termcolor import colored
from collections import defaultdict, deque

f = open("input", "r")


def check_valid(order, page_ordering_before):
    valid = True
    invalid_pairs = []
    for i in range(len(order) - 1):
        if order[i] in page_ordering_before:

            if order[i+1] not in page_ordering_before[order[i]]:
                # print (colored((order[i], order[i+1]),'red')) 
                invalid_pairs.append((order[i], order[i+1]))
                valid = False
            
        if order[i+1] in page_ordering_before:

            for test in order[:i+1]:
                if test in page_ordering_before[order[i+1]]:
                    # print (colored((order[i], order[i+1]),'red')) 
                    invalid_pairs.append((order[i], order[i+1]))
                    valid = False
    return valid, invalid_pairs

page_ordering_before = {}

# get the page ordering rules
for line in f:
    if line == "\n":
        break
    key, value = line.strip().split("|")
    if page_ordering_before.get(key) == None:
        page_ordering_before[key] = [value]
    else:
        page_ordering_before[key].append(value)
  
print(page_ordering_before)

add_middle = 0

invalid_updates = []

#get the updates
for line in f:
    order = line.strip().split(",")
    print(order)
    valid, invalid_pairs = check_valid(order, page_ordering_before)
            
    if valid:
        print (colored(("Valid:",order), "green"))
        add_middle += int(order[len(order) // 2])
    else :
        print (colored(("Invalid:",order), "red"))
        invalid_updates.append((order,invalid_pairs))
        
print("part1",add_middle)

add_middle = 0

def topological_sort(items, ordering_rules):
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Add all items to ensure isolated nodes are included
    all_nodes = set(items)
    
    # Build the graph based on ordering rules
    for item in items:
        if item in ordering_rules:
            for after in ordering_rules[item]:
                graph[item].append(after)
                in_degree[after] += 1
                all_nodes.add(after)
    
    # Initialize queue with nodes that have no prerequisites
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []
    
    # Process the queue
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If result length doesn't match number of nodes, there's a cycle
    if len(result) != len(all_nodes):
        return None
        
    return result

for update in invalid_updates:
    order = update[0]
    sorted_order = topological_sort(order, page_ordering_before)
    
    if sorted_order:
        print(colored(("Valid:", sorted_order), "green"))
        add_middle += int(sorted_order[len(sorted_order) // 2])
    else:
        print(colored(("Invalid: Cycle detected in ordering", order), "red"))

print("part2",add_middle)