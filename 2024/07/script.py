import sys

mul = lambda a,b: a*b
add = lambda a,b: a+b
concat = lambda a,b: int(str(a)+str(b))

p1_ops = (mul,add)
p2_ops = (mul,add,concat)

def is_computable(target: int, nums: list[int],ops) -> bool:
    if len(nums) == 1:
        return nums[0] == target
    if nums[0] > target:
        return False

    slug = nums[2:]
    (a,b) = nums[0:2]

    vals = [op(a,b) for op in ops]
    new_nums = lambda v: [v] + slug

    return any( is_computable(target,new_nums(v),ops) for v in vals )

p1_sum = 0
p2_sum = 0

for i,line in enumerate(sys.stdin):
    (target,nums) = line.rstrip().split(':')
    target = int(target)
    nums = [int(x) for x in nums.split(' ') if x]
    
    if is_computable(target,nums,p1_ops):
        p1_sum += target
        p2_sum += target
    elif is_computable(target,nums,p2_ops):
        p2_sum += target

print(p1_sum,p2_sum)

