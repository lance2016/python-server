import random


class SortAlgorithm:
    def __init__(self, nums:list=None):
        if nums is None or len(nums)==0:
            self.nums = [random.randint(0,10) for i in range(10)]

    def quick_sort(self, nums, start, end):
        if start>=end:
            return
        mid = self.partition(nums, start, end)
        self.quick_sort(nums, start, mid-1)
        self.quick_sort(nums, mid+1, end)

    def partition(self, nums, start, end):
        # 选择随机基准
        pilot = random.randint(start, end)
        # 基准值移动到最右侧
        nums[pilot], nums[end] = nums[end], nums[pilot]
        # i为小于基准值的下标，一开始为-1
        i = start - 1
        # j为当前指向的数组下标
        for j in range(start, end):
            # 如果找到小于基准值的值，i下标向前，将当前小于基准值的nums[j]替换nums[i]
            if nums[j]<nums[end]:
                i+=1
                nums[i],nums[j] = nums[j], nums[i]
        i+=1
        nums[i], nums[end] = nums[end],nums[i]
        return i

if __name__ =="__main__":
    s = SortAlgorithm()
    s.quick_sort(s.nums, 0, len(s.nums)-1)
    print(s.nums)
