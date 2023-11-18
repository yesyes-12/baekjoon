# 숫자 카드 2 / 이분탐색 / 실버4
import sys
from bisect import bisect_left, bisect_right
read = sys.stdin.readline

# 첫 번째 배열 정렬 후 bisect이용하여 원소 개수 찾기
# bisect_left : 리스트에서 이분탐색하여 target을 삽입할 가장 왼쪽 인덱스 반환
# bisect_left : 리스트에서 이분탐색하여 target을 삽입할 가장 오른쪽 인덱스 반환

def count_by_range(array, target):
    left = bisect_left(array, target)
    right = bisect_right(array, target)
    return right-left

N = int(read())
nums = list(map(int, read().split()))
nums.sort()

M = int(read())
nums2 = list(map(int, read().split()))

for n in nums2:
    print(count_by_range(nums, n), end=' ')