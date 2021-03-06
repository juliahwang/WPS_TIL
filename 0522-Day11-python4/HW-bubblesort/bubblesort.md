## 버블정렬

"두 원소를 비교해서 가장 큰 값을 맨 뒤로 보내면서 정렬" 이라고 접근하면 쉽다.

if 왼쪽 요소 > 오른쪽 요소 일 때 두 위치를 바꾼다.

else 그대로 놔둔다.

대상 리스트 : [1, 4, 5, 2, 9, 6 ] 

[1, 4, 5, 2, 9, 6] => 맨 앞으로 1,4를 비교, 그대로 놔둔다.

[1, 4, 5, 2, 9, 6] => 4, 5를 비교, 그대로 놔둔다.

[1, 4, 5, 2, 9, 6] => 5, 2를 비교, 왼쪽 요소가 더 크므로 위치를 바꾼다.

[1, 4, 2, 5, 9, 6] => 5, 9를 비교, 그대로 놔둔다.

[1, 4, 2, 5, 9, 6] => 9, 6을 비교, 왼쪽 요소가 더 크므로 위치를 바꾼다.

[1, 4, 2, 5, 6, 9] 1회 정렬 끝 9가 제일 크므로 맨 뒤로 정렬이 되었다.

이 것을 배열요소의 수만큼 반복하면 맨 뒤로 순차적으로 정렬이 된다.

1회차는 0번째 ~ 5번째 요소

2회차는 0번째 ~ 4번째 요소

3회차는 0번째 ~ 3번째 요소

4회차는 0번째 ~ 2번째 요소

5회차는 0번째 ~ 1번째 요소

6회차는 0번째 ~ 0번째 요소

까지 정렬을 한다.

 라고 생각하면 이해가 될 것이다.

1회차 : 9

2회차 : 6

3회차 : 5

4회차 : 4

5회차 : 2

6회차 : 1

순으로 위치에 맞게 정렬이 된다.

~~~pyhton
s_list = [2, 3, 7, 4, 9, 6, 2, 7, 3]

def bubble_sort(sample_list):
    list_len = len(sample_list)-1

    for i in range(list_len):
        for j in range(list_len-i):
            if sample_list[i] > sample_list[j]:
                sample_list[i], sample_list[j] = sample_list[j], sample_list[i]
    return sample_list

result = bubble_sort(s_list)
print(result)


## [2, 2, 3, 3, 4, 6, 7, 7, 9]
~~~

<br>

#### range 이해

~~~python
l = [3, 1 ,4, 2] 
len = len(l)-1 = 3
i in range(len)
j in range(i + 1, len-i)

[0] in range(3)
	[1] in range(3)

[1] in range(3)
	[2] in range(2)

[2] in range(3)
	[3] in range(1)
~~~

<br>

#### 버블 정렬의 비교 횟수 
= (n-1)+(n-2)+(n-3)+...+(n-(n-2))+(n-(n-1)) = (n-1)+(n-2)+(n-3)+...+3+2+1 = n(n-1)/2



출처: http://blog.eairship.kr/35 [누구나가 다 이해할 수 있는 프로그래밍 첫걸음]

[글 출처][ㅁ]
[ㅁ] : http://gompangs.tistory.com/46