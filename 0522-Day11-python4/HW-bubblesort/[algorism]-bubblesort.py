import random


s_list = [x for x in range(10)]
random.shuffle(s_list)

# def bubble_sort(sample_list):
#     list_len = len(sample_list)
#
#     for i in range(list_len - 1):
#         for j in range(list_len - 1 -i):
#             if sample_list[i] > sample_list[j]:
#                 sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
#     return sample_list
#


def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        print(data)

result = bubble_sort(s_list)

## [2, 2, 3, 3, 4, 6, 7, 7, 9]