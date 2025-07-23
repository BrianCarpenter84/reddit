class Solution(object):
    def addTwoNumbers(self, l1, l2):

        def add_lists(l1, l2):
            num1 = ''.join(map(str, l1))
            num2 = ''.join(map(str, l2))
            new_num = int(num1) + int(num2)
            new_list = []
            for i in str(new_num):
                new_list.append(int(i))
            return new_list

        if len(l1) > len(l2) or len(l2) > len(l1):
            total = add_lists(l1, l2)
            total.reverse()
            return total

        if len(l1) == len(l2):
            return add_lists(l1, l2)

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

solution = Solution()

print(solution.addTwoNumbers(l1,l2))




