from collections import Counter


class Solution:
    def getData(self):
        t = input()
        n, m = list(map(int, t.split()))
        scores = input()
        scores = list(map(int, scores.split()))
        idx = input()
        idx = list(map(int, idx.split()))
        return n, m, scores, idx

    def func(self):
        n, m, scores, idx = self.getData()
        # n, m, scores, idx = 2, 3, [50, 60, 70], [1, 2]
        counts = Counter(scores)
        counts = [(k, counts[k]) for k in counts.keys()]
        counts.sort()
        arr = {}
        sum = 0

        for score, cnt in counts:
            sum += cnt
            arr[score] = sum
        for i in idx:
            rate = arr[scores[i-1]]/n
            print("%.6f" % rate + "%")

    def func(self):
        n, m, scores, idx = self.getData()
        prefix = [0 for i in range(151)]
        for score in scores:
            prefix[score] += 1
        sum = 0
        for i in range(151):
            sum += prefix[i]
            prefix[i] = sum
        for i in idx:
            rate = prefix[scores[i-1]]/n
            print("%.6f" % rate + "%")


if __name__ == "__main__":
    Solution().func()
