#==================== 题目 38： 报数 =================#
'''
报数序列是指一个整照其中的整数的顺序进数序列，按行报数，
得到下一个数。其前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。
 
示例 1:
输入: 1
输出: "1"
示例 2:
输入: 4
输出: "1211"
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0 or n > 30:
            print('n needs to be bigger than 0 or smaller than 30')
            return 0

        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            return self.count_num(self.countAndSay(n - 1))
    
    def count_num(self, num_list):
        next_list = ''
        len_ = len(num_list)
        count_ = 1
        for num_ in range(len_):
            if num_ == len_ - 1:
                next_list = next_list + str(count_) + str(num_list[num_])
                break
            else:
                if num_list[num_ + 1] == num_list[num_]:
                    count_ += 1
                else:
                    next_list = next_list + str(count_) + str(num_list[num_])
                    count_ = 1
            
        return next_list

test = Solution()
print(test.countAndSay(5))