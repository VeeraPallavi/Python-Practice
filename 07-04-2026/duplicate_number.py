'''Find duplicate in array of n+1 integers'''

def find_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

print(find_duplicate([1,3,4,2,2]))