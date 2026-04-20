# 1-mashq
def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

print(climb_stairs(5))
# 2-mashq
def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# 3-mashq
def group_by_length(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)

print(group_by_length(["cat","dog","apple","banana","kiwi"]))
