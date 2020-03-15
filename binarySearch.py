class BinarySearch:
    def bisect(self, target, l):
        l.sort()
        left = 0
        right = len(l) - 1
        while left < right:
            mid = left + (right - left) // 2
            if l[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left, l[left]


import bisect

if __name__ == "__main__":
    bs = BinarySearch()
    target = 61
    a = [0, 10, 60]
    # left, lowerBound = bs.bisect(target, l)
    import ipdb;ipdb.set_trace(context=20)
    left = bisect.bisect_left(a, target)
    print(left)
