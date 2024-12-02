f = open("input", "r")
safe_count = 0
for line in f:
    nums = line.strip().split(" ")
    int_list = [int(x) for x in nums]
    if sorted(int_list) == int_list or sorted(int_list)[::-1] == int_list:
        safe = True
        int_list = sorted(int_list)
        for i in range(1, len(int_list)):
            difference = int_list[i] - int_list[i - 1]
            if difference >= 2: safe = False
            if difference == 0: safe = False
        if safe:
            safe_count+=1
            print("\033[32mSAFE\033[0m",line)
        else:
            print("\033[31mUNSAFE\033[0m",line)
print (safe_count)