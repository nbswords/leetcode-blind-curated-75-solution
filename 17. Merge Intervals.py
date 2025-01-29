class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 對 intervals 中的第 0 維做 ascending sorting
        intervals.sort(key=operator.itemgetter(0))
        ans = []
        # Sweep Line
        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans
