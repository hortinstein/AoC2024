def check_equation(test_value, operators, i, cur_res,part2 = False):
    # Base case: all operators processed
    if i == len(operators):
        return cur_res == test_value

    # Recursive case: try both addition and multiplication
    if check_equation(test_value, operators, i + 1, cur_res + operators[i],part2):
        return True
    if check_equation(test_value, operators, i + 1, cur_res * operators[i],part2):
        return True
    if part2 and check_equation(test_value, operators, i + 1, int(str(cur_res) + str(operators[i])),part2):
        return True
    
    return False

# Read input and parse equations
with open("input", "r") as f:
    equations = []
    for line in f:
        # Parse each line as `test_value: op1 op2 op3 ...`
        test_value = int(line.split(":")[0])
        operators = list(map(int, line.split(":")[1].strip().split()))
        equations.append((test_value, operators))

# Compute the sum of matching test values
total_sum = 0
for test_value, operators in equations:
    if check_equation(test_value, operators, 1, operators[0]):
        total_sum += test_value

print(total_sum)

###########################
# Part 2
###########################

# Compute the sum of matching test values
total_sum = 0
for test_value, operators in equations:
    if check_equation(test_value, operators, 1, operators[0], True):
        total_sum += test_value

print(total_sum)
