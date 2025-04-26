
import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    num = int(input())
    heapq.heappush(card, num)
    # heapq.heappush: item을 heap에 추가
    # heapq.heappop(heap): heap에서 가장 작은 원소를 pop&return, 비어있는 경우 IndexError 호출
    # heapq.heapify(x): 리스트 x를 즉각적으로 heap으로 변환함

result = 0
while len(card)> 1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    result += n1 + n2
    heapq.heappush(card, n1+n2)

print(result)