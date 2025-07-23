class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ''.join(map(str, l1))
        num2 = ''.join(map(str, l2))
        new_num = int(num1) + int(num2)
        total = []
        for i in str(new_num):
            total.append(int(i))
        total.reverse()
        return total


# example 1:

l1 = [2,4,3]
l2 = [5,6,4]

# expected Output: [7,0,8]
#======================================
# example 2:

# l1 = [0]
# l2 = [0]

# expected Output: [0]
#======================================
# example 3:

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]

# expected Output: [8,9,9,9,0,0,0,1]

solution = Solution()

print(solution.addTwoNumbers(l1,l2))




