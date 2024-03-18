# 初始数组
nums = [3,3,3,4]
# 目标数字
target = 10
res = [nums[0],nums[1],nums[2]]
s = abs(sum(res)-target)
# 三重循环遍历
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            # 找出所有的三数组合
            t = [nums[i],nums[j],nums[k]]
            # 比较和之前的最小三数组合差距
            if abs(sum(t) - target) < abs(s - target):
                # 若小于，则更新新的最小三数组合
                s = sum(t)
                res = t
# 输出结果三数组合
print(res)