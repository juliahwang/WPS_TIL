#### 퀴즈  - 데코레이터

> 두 숫자를 인자로 받는 print_plus 함수를 정의하고 plus함수에 연결하여 "함수시작", 연산값, "함수끝"을 출력하는 코드를 작성하라.

~~~python
def print_plus(func):
	inner_func(a, b):
		print("함수사작")
		print(func(a, b)) 
		print("함수 끝")
	return inner_func

@print_plus
def plus(a, b):
	return a + b

print_plus(plus(3, 5))
## 결과
# 함수시작
# 8
# 함수 끝
~~~


## 선택정렬

> 정렬방법 중의 하나로, 첫 수와 나머지 수의 최솟값을 비교하여 정렬하는 정렬법

~~~python 
def selection_sort(sample_list):
	list_len = len(sample_list)
	for i in range(list_len - 1): 
		min_index = i
		for j in range(i + 1, list_len):
			if sample_list[min_index] > sample_list[j]:
				min_index = j
			
		sample_list[min_index], sample_list[i] = sample_list[i], sample_list[min_index]
	return sample_list

sam_list = [5, 3, 7, 2, 6, 4]
selection_sort(sam_list)

## 결과 
# [2, 3, 4, 5, 6, 7]
~~~ 