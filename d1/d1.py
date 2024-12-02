f = open("input", "r")


l1, l2 = [], []

for line in f:

    i1,i2 = line.strip().split('   ')
    l1.append(int(i1))
    l2.append(int(i2))
    

    #sort the lists
def part1(l1,l2):
    l1.sort()
    l2.sort()

    distance = 0

    for i in range(len(l1)):
        distance += abs(l1[i] - l2[i])

    print(distance)

def part2(l1,l2):
    similarity = 0 
    for i in range(len(l1)):
        value = l1[i]
        similarity += value * l2.count(value)
    print(similarity)
part1(l1,l2)
part2(l1,l2)