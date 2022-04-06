def Binary_Search(numbers:list, target:int):
    l = 0
    r = len(numbers) - 1
    while l <= r:
        middle = l + (r - l) // 2
        if numbers[middle] == target:
            return target
        elif numbers[middle] > target:
            r = middle - 1
        else:
            l = middle + 1
    return "no such number"  
