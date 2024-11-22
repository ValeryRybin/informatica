numbers = list(map(int, input().split()))
num_size = len(numbers)

beauty_quality = [-2]*num_size
beauty_quality[0]=-1

for i in  range (1,num_size):
    if numbers[i]<=numbers[i-1]:
        beauty_quality[i]=i-1
    else:
        beauty_quality[i]=-1
        max_skyscraper=numbers[i]
        for j in range (i-1,-1,-1):
            if numbers[j]>=max_skyscraper:
                max_skyscraper=numbers[j]
                beauty_quality[i]=j
                break
              
            else:
                pass
print(*beauty_quality)