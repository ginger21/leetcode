#============= 题目：七进制数 ==========#
'''
给定一个整数，将其转化为7进制，并以字符串形式输出。
示例 1:
输入: 100
输出: "202"
示例 2:
输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
'''

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >=0:
            if num < 7:
                return str(num)
            else:
                div_, res_= self.div(num)
                if div_ < 7:
                    return str(div_) + str(res_)
                else:
                    return self.convertToBase7(div_) + str(res_)
        else:
            sev = '-' + self.convertToBase7(abs(num))
            return sev

    def div(self, num):
        '''
        :type num: int
        :rtype: int
        '''
        div = num // 7
        res = num % 7
        return div, res