def cumulative_sum(lst):
    cumulative = []
    total = 0
    for num in lst:
        total += num
        cumulative.append(total)
    return cumulative
