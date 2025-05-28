n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

for t in targets:
    print(1 if binary_search(a, t) else 0)