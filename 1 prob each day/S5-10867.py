# 중복 빼고 정렬하기
import sys
n = int(input())
nums = set(map(int,sys.stdin.readline().split()))
print(' '.join(map(str,sorted(nums))))