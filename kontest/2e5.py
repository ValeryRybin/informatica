words = list(map(str, input().split()))

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
                i += 1
                '''
                два отсортированных подмассива превратим в
                один отсортированный массив nums. i для left, j для right и k для nums. 
                Сравним элементы в left и right и копируем меньший элемент в nums.
                '''
            else: 
                nums[k] = right[j] 
                j += 1
            k += 1
#добавим оставшиеся элементы из left и right в nums
        while i < len(left): 
            nums[k] = left[i] 
            i += 1
            k += 1

        while j < len(right): 
            nums[k] = right[j] 
            j += 1
            k += 1

    return nums

def sort_word(word):
    letters = list(word)
    sort_letters = merge_sort(letters)
    sort_word = ''.join(sort_letters)
    return sort_word

word_frequency = {}
sorted_words_dict = {}

for word in words:
    sorted_word = sort_word(word)
    if sorted_word in word_frequency:
        word_frequency[sorted_word] += 1
    else:
        word_frequency[sorted_word] = 1
        sorted_words_dict[sorted_word] = []
    sorted_words_dict[sorted_word].append(word)

# Сортировка ключей по частоте
sorted_keys = list(word_frequency.keys())
n = 1
while n < len(sorted_keys):
    for i in range(len(sorted_keys) - n):
        if word_frequency[sorted_keys[i]] > word_frequency[sorted_keys[i + 1]]:
            sorted_keys[i], sorted_keys[i + 1] = sorted_keys[i + 1], sorted_keys[i]
    n += 1

sorted_keys.reverse()

sorted_words = []
unique_sorted_words = []

for key in sorted_keys:
    if word_frequency[key] == 1:
        unique_sorted_words += merge_sort(sorted_words_dict[key])
    else:
        group = merge_sort(sorted_words_dict[key])
        sorted_words += group

sorted_words += merge_sort(unique_sorted_words)
print(*sorted_words)