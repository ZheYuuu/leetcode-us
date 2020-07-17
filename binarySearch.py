class BinarySearch1:
    def bisect(self, target, l):
        l.sort()
        left = 0
        right = len(l)
        while left < right:
            mid = left + (right - left) // 2
            if l[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


class BinarySearch2:
    def bisect(self, target, l):
        l.sort()
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if l[mid] < target:
                left = mid + 1
            elif l[mid] > target:
                right = mid - 1
            else:
                return mid
        return -(left + 1)


if __name__ == "__main__":
    bs = BinarySearch1()
    target = 61 
    a = [0, 10, 10,60]
    left = bs.bisect(target, a)
    # import ipdb;ipdb.set_trace(context=20)
    # left = bisect.bisect_left(a, target)
    print(left)
