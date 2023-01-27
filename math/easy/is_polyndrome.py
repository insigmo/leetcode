# https://leetcode.com/problems/palindrome-number/


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     num = str(x)
    #     for i, v in enumerate(num[:len(num)//2]):
    #         if v != num[len(num)-i - 1]:
    #             return False
    #     return True

    def isPalindrome(self, x: int) -> bool:
        return 0 <= x == int(str(x)[::-1])


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
