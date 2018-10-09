#================ 题目 717： 1比特与2比特字符 =================#
'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
示例 1:
输入: 
bits = [1, 0, 0]
输出: True
解释: 
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:
输入: 
bits = [1, 1, 1, 0]
输出: False
解释: 
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
'''

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        self.que_ = []
        for _element in bits[:-1]:
            self.que_ = self._pair(self.que_, _element)
        if self.que_ == []:
            return True
        else:
            return False
        
    def _pair(self, que, num):
        if len(que) > 1:
            print('the len of que should be 1 or 0')
            return
        if que == []:
            if num == 1:
                que.append(num)
                return que
            elif num == 0:
                return que
        else:
            return []

test1 = Solution()
print(test1.isOneBitCharacter([1,0,0]))
