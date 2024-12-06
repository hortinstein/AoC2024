from termcolor import colored

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

def do_swaps(order, invalid_pairs):
    for pair in invalid_pairs:        
        # Find their indices
        index1 = order.index(pair[0])
        index2 = order.index(pair[1])

        # Swap the items
        order[index1], order[index2] = order[index2], order[index1]
    print(colored(order,'green'))
    return order,invalid_pairs

for update in invalid_updates:
    print(update)
    order = update[0]
    invalid_pairs = set(update[1]) #eliminate duplicates so it doesnt swap twice
    valid = False
    while not valid:
        order, invalid_pairs = do_swaps(order, invalid_pairs)
        valid, invalid_pairs = check_valid(order, page_ordering_before)
    if valid:
        print (colored(("Valid:",order), "green"))
    else :
        print (colored(("Invalid:",order,invalid_pairs), "red"))
        continue    
    add_middle += int(order[len(order) // 2])

print("part2",add_middle)