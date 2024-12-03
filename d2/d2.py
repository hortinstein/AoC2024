f = open("input", "r")

def list_minus_one(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]

def is_safe(lst):
    print(lst)
    if (sorted(int_list) == int_list) or (sorted(int_list)[::-1] == int_list):
        for i in range(1, len(int_list)):
            difference = abs(int_list[i] - int_list[i - 1])
            print("difference",difference)
            if difference > 3: return False
            if difference == 0: return False
    else:
        print("not sorted")
        return False
    return True


safe_count = 0
safe_count2 = 0

for line in f:
    nums = line.strip().split(" ")
    
    int_list = [int(x) for x in nums]
    safe = is_safe(int_list)
    
    if safe:
        safe_count+=1
        safe_count2+=1
        print("\033[32mSAFE\033[0m",line)
    else:
        int_lists = list_minus_one(int_list)
        for int_list in int_lists:
            safe = is_safe(int_list)
            if safe:
                safe_count2+=1
                break
        print("\033[31mUNSAFE\033[0m",line)




print (safe_count)
print (safe_count2)