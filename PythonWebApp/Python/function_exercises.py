# arrayCheck([1, 1, 2, 3, 1])

def arrayCheck(nums):

    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

# result = arrayCheck([1, 1, 2, 3, 1])
# result = arrayCheck([1, 1, 2, 4, 1])
result = arrayCheck([1, 1, 2, 1, 2, 3])

# print(result)

def string_bits(mystring):

    result = " "

    for i in range(len(mystring)):
        if i%2 == 0:
            result = result +mystring[i]

    return result

# result = string_bits('Hello')
# result = string_bits('Hi')
result = string_bits('Heeololeo')
# print(result)

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return (b.endswith(a) or a.endswith(b))

    # return a[-(len(b)):] == b or a == b[-(len(a)):]

# result = end_other('Hiabc', 'abc')
result = end_other('AbC', 'HiaBc')
# print(result)
def double_char(mystring):

    result = " "
    for char in mystring:
        result += char*2

    return result

# result = double_char("Tiny")
result = double_char("Uzzie")
# print(result)

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,17,18,19]:
        return 0
    return n

#result = no_teen_sum(1, 2, 3)
#result = no_teen_sum(2, 13, 1)
result = no_teen_sum(2, 1, 17)
#print(result)

def count_evens(nums):
    count = 0

    for element in nums:
        if element % 2 == 0:
            count += 1
    return count
#result = count_evens([2, 1, 2, 3, 4])
result = count_evens([1, 3, 4])
print(result)
