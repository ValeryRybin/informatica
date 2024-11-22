numbers = list(map(int, input().split()))
def sum_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def merge_sort(nums): 
    if len(nums) > 1:  # из пункта 1 помним, если в массиве 1 элемент, то он уже отсортирован
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        left = merge_sort(left)  
        right = merge_sort(right)  

        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
                '''
                два отсортированных подмассива превратим в
                один отсортированный массив nums. i для left, j для right и k для nums. 
                Сравним элементы в left и right и копируем меньший элемент в nums.
                '''
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1
#добавим оставшиеся элементы из left и right в nums
        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1

        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1

    return nums

sorted_numbers = merge_sort(numbers)

lst = []
for i in range (len(sorted_numbers)):
    lst.append(sum_digits(sorted_numbers[i]))

n=1
while n < len(lst):
    for i in range(len(lst)-n):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            sorted_numbers[i], sorted_numbers[i+1] = sorted_numbers[i+1], sorted_numbers[i]
    n+=1
print(*sorted_numbers)