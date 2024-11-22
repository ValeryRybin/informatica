words2 = list(map(str, input().split()))

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

'''def sort_word(word):
    letters = list(word)
    sort_letters = merge_sort(letters)
    sort_word = ''.join(sort_letters)
    return sort_word

words_sort_word = []
for word in words2:
    words_sort_word.append(sort_word(word))
word_count = []
for i in range (len(words_sort_word)):
    word_count.append(words_sort_word.count(words_sort_word[i]))

n=1
while n < len(word_count):
    for i in range(len(word_count)-n):
        if word_count[i] > word_count[i+1]:
            word_count[i], word_count[i+1] = word_count[i+1], word_count[i]
            words_sort_word[i], words_sort_word[i+1] = words_sort_word[i+1], words_sort_word[i]
            words2[i],words2[i+1]=words2[i+1],words2[i]
    n+=1
words_sort_word.reverse()
words2.reverse()
word_count.reverse()
sorted_words=[]
z=[]
'''
groups = {}
for word in words2:
    sorted_word = ''.join(merge_sort(list(word)))
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]
print(groups.values())
sorted_groups = merge_sort(groups.values())
print(sorted_groups)
z=[]
for group in sorted_groups:
    z.append(merge_sort(group))
print(*z)