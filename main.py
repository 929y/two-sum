from typing import List

def twoSum(nums:List[int], target: int):
    flag = 1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target :
                flag = 0
                break
        if flag == 0:
            break
    output = [i,j]
    return output

