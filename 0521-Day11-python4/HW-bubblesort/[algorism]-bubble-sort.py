s_list = [2, 3, 7, 4, 9, 6, 2, 7, 3]

def bubble_sort(sample_list):
    list_len = len(sample_list)

    for i in range(list_len-1):
        for j in range(i+1, list_len):
            if sample_list[i] > sample_list[j]:
                sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
    return sample_list

result = bubble_sort(s_list)
print(result)


## [2, 2, 3, 3, 4, 6, 7, 7, 9]