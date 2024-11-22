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

def sort_word(word):
    letters = list(word)
    sort_letters = merge_sort(letters)
    sort_word = ''.join(sort_letters)
    return sort_word

words_sort_word = []
for word in words:
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
    n+=1
words_sort_word.reverse()

sorted_words=[]
z2=[]
z=[]
z.append(words_sort_word[0])
for word_sort_word in words_sort_word:
    if words_sort_word.count(word_sort_word)==1: z2.append(word_sort_word)
    elif z[-1] == word_sort_word: pass
    else: z.append(word_sort_word)


for i in range (len(z)):
    newgroup=[]
    for word in words:
        if sort_word(word) == z[i]:
            newgroup.append(word)
    sorted_newgroup = merge_sort(newgroup)
    sorted_words += sorted_newgroup
sorted_newgroup=[]
sorted_words2=[]
for i in range (len(z2)):
    newgroup=[]
    for word in words:
        if sort_word(word) == z2[i]:
            newgroup.append(word)
    sorted_newgroup = merge_sort(newgroup)
    sorted_words2 += sorted_newgroup
merge_sort(sorted_words2)
sorted_words+=sorted_words2
print(*sorted_words)