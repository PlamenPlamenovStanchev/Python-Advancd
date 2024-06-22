def num_sums(*args):
    n_sum = sum(num for num in args if num < 0)
    p_sum = sum(num for num in args if num > 0)

    return n_sum, p_sum

nums = [int(x) for x in input().split()]
neg_sum, pos_sum = num_sums(*nums)

print(neg_sum)
print(pos_sum)

if abs(neg_sum) > pos_sum:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')

