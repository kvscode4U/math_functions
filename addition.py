def addition(*nums):
    Sum = 0
    for n in nums:
        Sum += n
    return Sum


print(addition(4,5))