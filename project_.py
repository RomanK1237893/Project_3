def sum_of_k(nums, target, k):
    if len(nums) < k:
        return []
    output = []
    current = []
    nums.sort()
    checked = set()
    sum_helper(nums, target, k, output, checked, current, 0)
    return output
def sum_helper(nums, target, k, output, checked, current, prev):
    if k == 0:
        return
    for i in range(prev, len(nums) - k + 1):
        current.append(nums[i])
        if k == 1 and target - nums[i] == 0:
            code = str(current[0])
            for n in range(1, len(current)):
                code += "&" + str(current[n])
            if code not in checked:
                output.append(current.copy())
                checked.add(code)
        sum_helper(nums, target - nums[i], k - 1, output, checked, current, i + 1)
        current.pop()
nums1 = input("Введите список чисел, разделенных пробелом: ").split()
nums = list(map(int, nums1))
target = int(input("Введите сумму которую вы хотите получить:"))
k = int(input("Введите количество элементов в выводе: "))
print(sum_of_k(nums, target, k))